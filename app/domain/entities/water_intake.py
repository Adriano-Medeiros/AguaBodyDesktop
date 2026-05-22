from dataclasses import dataclass
from datetime import datetime


@dataclass
class WaterIntake:
  amount_ml: int
  created_at: datetime
  id: int | None = None