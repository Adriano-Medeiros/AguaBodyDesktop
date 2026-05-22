from dataclasses import dataclass


@dataclass
class HydrationState:
  consumed_ml: int = 0
  goal_ml: int = 2000

  @property
  def remaining_ml(self) -> int:
    return max(self.goal_ml - self.consumed_ml, 0)

  @property
  def progress_percent(self) -> int:
    if self.goal_ml <= 0:
      return 0

    return min(round((self.consumed_ml / self.goal_ml) * 100), 100)