from abc import ABC, abstractmethod

from app.domain.entities.daily_goal import DailyGoal


class DailyGoalRepository(ABC):
  @abstractmethod
  def get_active_goal(self) -> DailyGoal:
    pass

  @abstractmethod
  def update_goal(self, goal_ml: int) -> DailyGoal:
    pass