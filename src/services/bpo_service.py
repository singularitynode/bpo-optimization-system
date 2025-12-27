import asyncio
import random
from datetime import datetime

class BpoService:
    def __init__(self):
        self.queue = []
        self.processed_count = 0
      
    async def process(self, task: str) -> dict:
        await asyncio.sleep(0.1)
        self.processed_count += 1
        result = {
            "task": task,
            "processed_at": datetime.utcnow().isoformat(),
            "status": "completed",
            "ticket_id": f"TICKET-{self.processed_count:06d}",
            "qa_score": round(random.uniform(0.8, 1.0), 2),
            "sentiment": random.choice(["positive", "neutral", "negative"]),
            "translated": task.upper() if random.random() > 0.5 else task
        }
        return result
  
    async def batch_process(self, tasks: list) -> list:
        return [await self.process(task) for task in tasks]