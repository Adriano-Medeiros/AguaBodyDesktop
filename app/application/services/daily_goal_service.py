from app.domain.entities.daily_goal import DailyGoal
from app.domain.repositories.daily_goal_repository import DailyGoalRepository


class DailyGoalService:
  def __init__(self, daily_goal_repository: DailyGoalRepository):
    self._daily_goal_repository = daily_goal_repository

  def get_active_goal(self) -> DailyGoal:
    return self._daily_goal_repository.get_active_goal()

  def update_goal(self, goal_ml: int) -> DailyGoal:
    if goal_ml < 500:
      raise ValueError("A meta diária deve ser de pelo menos 500 ml.")

    if goal_ml > 10000:
      raise ValueError("A meta diária deve ser menor ou igual a 10000 ml.")

    return self._daily_goal_repository.update_goal(goal_ml)