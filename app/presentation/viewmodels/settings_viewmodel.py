from app.application.services.daily_goal_service import DailyGoalService
from app.application.services.quick_button_service import QuickButtonService
from app.infrastructure.repositories.sqlite_daily_goal_repository import (
  SqliteDailyGoalRepository,
)
from app.infrastructure.repositories.sqlite_quick_button_config_repository import (
  SqliteQuickButtonConfigRepository,
)


class SettingsViewModel:
  def __init__(self):
    daily_goal_repository = SqliteDailyGoalRepository()
    quick_button_repository = SqliteQuickButtonConfigRepository()

    self._daily_goal_service = DailyGoalService(daily_goal_repository)
    self._quick_button_service = QuickButtonService(quick_button_repository)

  def get_goal_ml(self) -> int:
    return self._daily_goal_service.get_active_goal().goal_ml

  def update_goal(self, goal_ml: int):
    return self._daily_goal_service.update_goal(goal_ml)

  def get_quick_button_config(self):
    return self._quick_button_service.get_config()

  def update_quick_buttons(
    self,
    button_1_ml: int,
    button_2_ml: int,
    button_3_ml: int,
  ):
    return self._quick_button_service.update_config(
      button_1_ml,
      button_2_ml,
      button_3_ml,
    )