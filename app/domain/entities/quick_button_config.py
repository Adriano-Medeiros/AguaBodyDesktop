from dataclasses import dataclass
from datetime import datetime


@dataclass
class QuickButtonConfig:
  button_1_ml: int = 200
  button_2_ml: int = 300
  button_3_ml: int = 500
  id: int | None = None
  updated_at: datetime | None = None