"""
CONFIGURATION LOADER
Loads and validates all environment variables
"""

import os
from typing import Dict, Any
from sqlalchemy import create_engine

def load_config() -> Dict[str, Any]:
    """Load and validate all configuration"""
    
    config = {
        # Core secrets
        'openai_api_key': os.getenv('OPENAI_API_KEY', ''),
        'jwt_secret': os.getenv('JWT_SECRET', ''),
        
        # Database
        'postgres_url': os.getenv('POSTGRES_URL', ''),
        'redis_url': os.getenv('REDIS_URL', ''),
        'postgres_password': os.getenv('POSTGRES_PASSWORD', ''),
        'redis_password': os.getenv('REDIS_PASSWORD', ''),
        
        # System parameters
        'veto_rate': float(os.getenv('VETO_RATE', '0.5')),
        'max_replicas': int(os.getenv('MAX_REPLICAS', '5')),
        
        # URLs
        'next_public_backend_url': os.getenv('NEXT_PUBLIC_BACKEND_URL', 'http://localhost:8000'),
        'prometheus_url': os.getenv('PROMETHEUS_URL', 'http://localhost:9090'),
        'grafana_url': os.getenv('GRAFANA_URL', 'http://localhost:3000'),
        
        # Engineering parameters
        'divine_coupling': float(os.getenv('DIVINE_COUPLING', '0.1')),
        'liquid_nu': float(os.getenv('LIQUID_NU', '0.01')),
        
        # AWS (if configured)
        'aws_region': os.getenv('AWS_REGION', ''),
        'aws_access_key': os.getenv('AWS_ACCESS_KEY_ID', ''),
        'aws_secret_key': os.getenv('AWS_SECRET_ACCESS_KEY', ''),
        'k8s_cluster': os.getenv('K8S_CLUSTER', ''),
    }
    
    # Validate critical configs
    errors = []
    
    if not config['openai_api_key'] or config['openai_api_key'].startswith('your-'):
        errors.append("OPENAI_API_KEY not configured")
    
    if not config['jwt_secret'] or config['jwt_secret'].startswith('your-'):
        errors.append("JWT_SECRET not configured")
    
    if not config['postgres_password'] or config['postgres_password'].startswith('your-'):
        errors.append("POSTGRES_PASSWORD not configured")
    
    if errors:
        raise ValueError(f"Configuration errors: {', '.join(errors)}")
    
    # Set default PostgreSQL URL if not provided
    if not config['postgres_url']:
        config['postgres_url'] = 'postgresql://bpo_admin:{}@localhost:5432/bpo_stable'.format(
            config['postgres_password']
        )
    
    if not config['redis_url']:
        config['redis_url'] = 'redis://:{}@localhost:6379/0'.format(
            config['redis_password']
        )
    
    # Test database connection (optional)
    try:
        engine = create_engine(config['postgres_url'])
        with engine.connect() as conn:
            conn.execute("SELECT 1")
    except Exception:
        # Fallback to SQLite for testing
        config['postgres_url'] = 'sqlite:///:memory:'
        print("⚠️  Using SQLite in-memory database (for testing only)")
    
    return config

def get_database_url() -> str:
    """Get database URL with proper formatting"""
    config = load_config()
    return config['postgres_url']

def get_redis_url() -> str:
    """Get Redis URL with proper formatting"""
    config = load_config()
    return config['redis_url']

def is_production() -> bool:
    """Check if running in production"""
    return bool(os.getenv('AWS_ACCESS_KEY_ID') and 
                os.getenv('AWS_SECRET_ACCESS_KEY'))

def get_deployment_type() -> str:
    """Get deployment type"""
    if is_production():
        return "production"
    elif os.getenv('DOCKER_COMPOSE'):
        return "docker"
    else:
        return "development"