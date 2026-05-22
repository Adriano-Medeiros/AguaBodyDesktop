from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import ReminderConfigModel
from app.domain.entities.reminder_config import ReminderConfig
from app.domain.repositories.reminder_config_repository import ReminderConfigRepository


class SqliteReminderConfigRepository(ReminderConfigRepository):
  def get_config(self) -> ReminderConfig:
    with SessionLocal() as session:
      model = (
        session.query(ReminderConfigModel)
        .order_by(ReminderConfigModel.id.desc())
        .first()
      )

      if model is None:
        model = ReminderConfigModel(
          enabled=True,
          interval_minutes=60,
          next_reminder_at=None,
          updated_at=datetime.now(),
        )

        session.add(model)
        session.commit()
        session.refresh(model)

      return ReminderConfig(
        id=model.id,
        enabled=model.enabled,
        interval_minutes=model.interval_minutes,
        next_reminder_at=model.next_reminder_at,
        updated_at=model.updated_at,
      )

  def update_config(self, enabled: bool, interval_minutes: int) -> ReminderConfig:
    with SessionLocal() as session:
      model = (
        session.query(ReminderConfigModel)
        .order_by(ReminderConfigModel.id.desc())
        .first()
      )

      if model is None:
        model = ReminderConfigModel(
          enabled=enabled,
          interval_minutes=interval_minutes,
          next_reminder_at=None,
          updated_at=datetime.now(),
        )

        session.add(model)

      else:
        model.enabled = enabled
        model.interval_minutes = interval_minutes
        model.next_reminder_at = None
        model.updated_at = datetime.now()

      session.commit()
      session.refresh(model)

      return ReminderConfig(
        id=model.id,
        enabled=model.enabled,
        interval_minutes=model.interval_minutes,
        next_reminder_at=model.next_reminder_at,
        updated_at=model.updated_at,
      )

  def update_next_reminder_at(self, next_reminder_at: datetime) -> ReminderConfig:
    with SessionLocal() as session:
      model = (
        session.query(ReminderConfigModel)
        .order_by(ReminderConfigModel.id.desc())
        .first()
      )

      if model is None:
        model = ReminderConfigModel(
          enabled=True,
          interval_minutes=60,
          next_reminder_at=next_reminder_at,
          updated_at=datetime.now(),
        )
        session.add(model)

      else:
        model.next_reminder_at = next_reminder_at
        model.updated_at = datetime.now()

      session.commit()
      session.refresh(model)

      return ReminderConfig(
        id=model.id,
        enabled=model.enabled,
        interval_minutes=model.interval_minutes,
        next_reminder_at=model.next_reminder_at,
        updated_at=model.updated_at,
      )