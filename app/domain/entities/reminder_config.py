from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReminderConfig:
  enabled: bool = True
  interval_minutes: int = 60
  next_reminder_at: datetime | None = None
  id: int | None = None
  updated_at: datetime | None = None