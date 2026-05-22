from abc import ABC, abstractmethod

from app.domain.entities.reminder_config import ReminderConfig


class ReminderConfigRepository(ABC):
  @abstractmethod
  def get_config(self) -> ReminderConfig:
    pass

  @abstractmethod
  def update_config(self, enabled: bool, interval_minutes: int) -> ReminderConfig:
    pass