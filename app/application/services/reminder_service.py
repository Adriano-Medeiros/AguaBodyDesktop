from winotify import Notification

from app.domain.entities.reminder_config import ReminderConfig
from app.domain.repositories.reminder_config_repository import ReminderConfigRepository


class ReminderService:
  def __init__(
    self,
    reminder_config_repository: ReminderConfigRepository,
    on_reminder_callback=None,
  ):
    self._repository = reminder_config_repository
    self._on_reminder_callback = on_reminder_callback

  def get_config(self) -> ReminderConfig:
    return self._repository.get_config()

  def update_config(
    self,
    enabled: bool,
    interval_minutes: int,
  ) -> ReminderConfig:
    if interval_minutes < 1:
      raise ValueError("O intervalo mínimo é de 1 minuto.")

    if interval_minutes > 480:
      raise ValueError("O intervalo máximo é de 480 minutos.")

    return self._repository.update_config(
      enabled,
      interval_minutes,
    )

  def show_reminder(self):
    toast = Notification(
      app_id="AguaBody",
      title="💧 Hora de beber água",
      msg="Mantenha sua hidratação em dia.",
      duration="short",
    )

    toast.show()

    if self._on_reminder_callback is not None:
      self._on_reminder_callback()