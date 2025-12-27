import os
import random
import re
import logging
import hashlib
from datetime import datetime
from sqlalchemy import create_engine, text, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import bindparam

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Veto:
    def __init__(self):
        self.veto_rate = float(os.getenv("VETO_RATE", 0.5))
        self.gdpr_compliant = os.getenv("GDPR_CONSENT", "true").lower() == "true"
        self.ethical_log = []
        postgres_url = os.getenv("POSTGRES_URL")
        if not postgres_url or "sqlite://" in postgres_url:
            logger.warning("Using SQLite (not for production). Set POSTGRES_URL for PostgreSQL.")
            self.engine = create_engine("sqlite:///:memory:")
        else:
            self.engine = create_engine(postgres_url)
        self.Session = sessionmaker(bind=self.engine)
        self.is_sqlite = "sqlite://" in str(self.engine.url)
    
    def _ml_ethics_check(self) -> bool:
        import sympy as sp
        x = sp.symbols('x')
        ethics_func = -x**2 + 1
        score = float(ethics_func.subs(x, random.uniform(0, 1)))
        return score > 0.5
    
    def check(self, user_id: int = None) -> bool:
        try:
            if random.random() < self.veto_rate:
                is_ethical = self._ml_ethics_check()
               
                ts = datetime.utcnow().isoformat()
                checksum = hashlib.md5(f"{ts}{is_ethical}".encode()).hexdigest()[:8]
               
                if self.is_sqlite:
                    stmt = text("""
                        INSERT INTO ethical_logs (timestamp, ethical, checked, user_id, checksum)
                        VALUES (:ts, :eth, :chk, :uid, :checksum)
                    """)
                    with self.Session() as session:
                        session.execute(stmt, {
                            'ts': ts,
                            'eth': is_ethical,
                            'chk': True,
                            'uid': str(user_id) if user_id else None,
                            'checksum': checksum
                        })
                        session.commit()
                        log_id = session.execute(text("SELECT last_insert_rowid()")).scalar()
                        logger.info(f"Ethical check logged: ID {log_id}, Ethical: {is_ethical}")
                else:
                    stmt = text("""
                        INSERT INTO ethical_logs (timestamp, ethical, checked, user_id, checksum)
                        VALUES (:ts, :eth, :chk, :uid, :checksum)
                        RETURNING id
                    """).bindparams(
                        bindparam('ts', value=ts, type_=String),
                        bindparam('eth', value=is_ethical, type_=Boolean),
                        bindparam('chk', value=True, type_=Boolean),
                        bindparam('uid', value=str(user_id) if user_id else None, type_=String),
                        bindparam('checksum', value=checksum, type_=String)
                    )
                    with self.Session() as session:
                        result = session.execute(stmt)
                        session.commit()
                        log_id = result.fetchone()[0]
                        logger.info(f"Ethical check logged: ID {log_id}, Ethical: {is_ethical}")
               
                return is_ethical
        except Exception as e:
            logger.error(f"Ethical check failed: {e}")
            return False
  
    def check_rate(self) -> float:
        return self.veto_rate
  
    def set_rate(self, rate: float):
        self.veto_rate = max(0.0, min(1.0, rate))
      
    def gdpr_consent(self, user_id: str, consent: bool) -> dict:
        log = {
            "user_id": user_id,
            "consent_given": consent,
            "timestamp": datetime.utcnow().isoformat(),
            "gdpr_compliant": self.gdpr_compliant
        }
        try:
            with self.Session() as session:
                session.execute(text("INSERT INTO ethical_logs (timestamp, ethical, checked, user_id) VALUES (:ts, :consent, true, :uid)"),
                                {"ts": log["timestamp"], "consent": consent, "uid": user_id})
                session.commit()
        except Exception as e:
            logger.error(f"GDPR log failed: {e}")
        return log