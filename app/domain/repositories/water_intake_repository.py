from abc import ABC, abstractmethod
from datetime import date

from app.domain.entities.water_intake import WaterIntake


class WaterIntakeRepository(ABC):
  @abstractmethod
  def add(self, water_intake: WaterIntake) -> WaterIntake:
    pass

  @abstractmethod
  def get_total_by_date(self, target_date: date) -> int:
    pass

  @abstractmethod
  def get_all(self) -> list[WaterIntake]:
    pass

  @abstractmethod
  def remove_last(self) -> bool:
    pass

  @abstractmethod
  def delete_by_id(self, water_intake_id: int) -> bool:
    pass

  @abstractmethod
  def update_amount(self, water_intake_id: int, amount_ml: int) -> bool:
    pass

  @abstractmethod
  def get_daily_totals(self, days: int = 7) -> list[dict]:
    pass