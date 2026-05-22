from datetime import date, datetime

from app.domain.entities.hydration_state import HydrationState
from app.domain.entities.water_intake import WaterIntake
from app.domain.repositories.daily_goal_repository import DailyGoalRepository
from app.domain.repositories.water_intake_repository import WaterIntakeRepository


class HydrationService:
  def __init__(
    self,
    water_intake_repository: WaterIntakeRepository,
    daily_goal_repository: DailyGoalRepository,
  ):
    self._water_intake_repository = water_intake_repository
    self._daily_goal_repository = daily_goal_repository
    self._state = self._load_state()

  def _load_state(self) -> HydrationState:
    daily_goal = self._daily_goal_repository.get_active_goal()

    return HydrationState(
      consumed_ml=self._water_intake_repository.get_total_by_date(date.today()),
      goal_ml=daily_goal.goal_ml,
    )

  def add_water(self, amount_ml: int) -> HydrationState:
    if amount_ml <= 0:
      return self._state

    water_intake = WaterIntake(
      amount_ml=amount_ml,
      created_at=datetime.now(),
    )

    self._water_intake_repository.add(water_intake)
    self._state = self._load_state()

    return self._state

  def remove_last_water(self) -> HydrationState:
    self._water_intake_repository.remove_last()
    self._state = self._load_state()

    return self._state

  def get_state(self) -> HydrationState:
    self._state = self._load_state()

    return self._state

  def get_daily_totals(self, days: int = 7) -> list[dict]:
    return self._water_intake_repository.get_daily_totals(days)