from sqlalchemy import inspect, text

from app.database.connection import Base, engine
from app.database import models


def create_tables():
  Base.metadata.create_all(bind=engine)
  _add_next_reminder_at_column_if_needed()


def _add_next_reminder_at_column_if_needed():
  inspector = inspect(engine)

  if "reminder_configs" not in inspector.get_table_names():
    return

  columns = [
    column["name"]
    for column in inspector.get_columns("reminder_configs")
  ]

  if "next_reminder_at" not in columns:
    with engine.connect() as connection:
      connection.execute(
        text("ALTER TABLE reminder_configs ADD COLUMN next_reminder_at DATETIME")
      )
      connection.commit()