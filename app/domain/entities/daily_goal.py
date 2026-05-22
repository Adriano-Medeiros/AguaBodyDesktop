from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailyGoal:
  goal_ml: int
  active: bool = True
  id: int | None = None
  created_at: datetime | None = None
  updated_at: datetime | None = None