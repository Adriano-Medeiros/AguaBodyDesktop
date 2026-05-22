from app.application.services.hydration_service import HydrationService
from app.application.services.quick_button_service import QuickButtonService
from app.domain.entities.hydration_state import HydrationState
from app.infrastructure.repositories.sqlite_daily_goal_repository import (
  SqliteDailyGoalRepository,
)
from app.infrastructure.repositories.sqlite_quick_button_config_repository import (
  SqliteQuickButtonConfigRepository,
)
from app.infrastructure.repositories.sqlite_water_intake_repository import (
  SqliteWaterIntakeRepository,
)


class DashboardViewModel:
  def __init__(self):
    water_intake_repository = SqliteWaterIntakeRepository()
    daily_goal_repository = SqliteDailyGoalRepository()
    quick_button_repository = SqliteQuickButtonConfigRepository()

    self._hydration_service = HydrationService(
      water_intake_repository,
      daily_goal_repository,
    )

    self._quick_button_service = QuickButtonService(
      quick_button_repository
    )

  def add_water(self, amount_ml: int) -> HydrationState:
    return self._hydration_service.add_water(amount_ml)

  def remove_last_water(self) -> HydrationState:
    return self._hydration_service.remove_last_water()

  def get_state(self) -> HydrationState:
    return self._hydration_service.get_state()

  def get_daily_totals(self, days: int = 7) -> list[dict]:
    return self._hydration_service.get_daily_totals(days)

  def get_quick_button_config(self):
    return self._quick_button_service.get_config()