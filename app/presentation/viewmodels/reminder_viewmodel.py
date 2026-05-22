from datetime import datetime, timedelta

from app.application.services.reminder_service import ReminderService
from app.domain.entities.reminder_config import ReminderConfig
from app.infrastructure.repositories.sqlite_reminder_config_repository import (
  SqliteReminderConfigRepository,
)


class ReminderViewModel:
  def __init__(self, on_reminder_callback=None):
    self._repository = SqliteReminderConfigRepository()

    self._service = ReminderService(
      self._repository,
      on_reminder_callback,
 )

  def get_config(self) -> ReminderConfig:
    return self._service.get_config()

  def update_config(self, enabled: bool, interval_minutes: int) -> ReminderConfig:
    return self._service.update_config(enabled, interval_minutes)

  def get_next_reminder_text(self) -> str:
    config = self.get_config()

    if not config.enabled:
      return "Desativado"

    if config.next_reminder_at:
      return config.next_reminder_at.strftime("%H:%M")

    next_reminder_at = datetime.now() + timedelta(
      minutes=config.interval_minutes
    )

    self._repository.update_next_reminder_at(next_reminder_at)

    return next_reminder_at.strftime("%H:%M")

  def schedule_next_reminder(self):
    config = self.get_config()

    if not config.enabled:
      return

    next_reminder_at = datetime.now() + timedelta(
      minutes=config.interval_minutes
    )

    self._repository.update_next_reminder_at(next_reminder_at)

  def show_test_notification(self):
    self._service.show_reminder()

  def show_reminder(self):
    self._service.show_reminder()
    self.schedule_next_reminder()