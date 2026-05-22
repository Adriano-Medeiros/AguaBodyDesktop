from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class WaterIntakeModel(Base):
  __tablename__ = "water_intakes"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  amount_ml: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)


class DailyGoalModel(Base):
  __tablename__ = "daily_goals"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  goal_ml: Mapped[int] = mapped_column(Integer, nullable=False, default=2000)
  active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
  updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)


class ReminderConfigModel(Base):
  __tablename__ = "reminder_configs"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  interval_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=60)
  next_reminder_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
  updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)


class QuickButtonConfigModel(Base):
  __tablename__ = "quick_button_configs"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  button_1_ml: Mapped[int] = mapped_column(Integer, nullable=False, default=200)
  button_2_ml: Mapped[int] = mapped_column(Integer, nullable=False, default=300)
  button_3_ml: Mapped[int] = mapped_column(Integer, nullable=False, default=500)
  updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)