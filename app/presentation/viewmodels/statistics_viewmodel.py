from datetime import date, timedelta

from app.infrastructure.repositories.sqlite_daily_goal_repository import (
  SqliteDailyGoalRepository,
)
from app.infrastructure.repositories.sqlite_water_intake_repository import (
  SqliteWaterIntakeRepository,
)


class StatisticsViewModel:
  def __init__(self):
    self._water_repository = SqliteWaterIntakeRepository()
    self._goal_repository = SqliteDailyGoalRepository()

  def get_summary(self) -> dict:
    goal_ml = self._goal_repository.get_active_goal().goal_ml
    daily_totals = self._water_repository.get_daily_totals(7)

    total_consumed = sum(item["total_ml"] for item in daily_totals)
    average_ml = round(total_consumed / 7)

    best_day = max(
      daily_totals,
      key=lambda item: item["total_ml"],
    )

    streak = self._calculate_streak(goal_ml)

    return {
      "goal_ml": goal_ml,
      "average_ml": average_ml,
      "best_day_ml": best_day["total_ml"],
      "best_day_date": best_day["date"],
      "streak": streak,
      "daily_totals": daily_totals,
    }

  def _calculate_streak(self, goal_ml: int) -> int:
    streak = 0
    current_date = date.today()

    while True:
      total = self._water_repository.get_total_by_date(current_date)

      if total < goal_ml:
        break

      streak += 1
      current_date = current_date - timedelta(days=1)

    return streak