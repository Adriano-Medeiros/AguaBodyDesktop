from datetime import date, datetime, time, timedelta

from sqlalchemy import desc, func

from app.database.connection import SessionLocal
from app.database.models import WaterIntakeModel
from app.domain.entities.water_intake import WaterIntake
from app.domain.repositories.water_intake_repository import WaterIntakeRepository


class SqliteWaterIntakeRepository(WaterIntakeRepository):
  def add(self, water_intake: WaterIntake) -> WaterIntake:
    with SessionLocal() as session:
      model = WaterIntakeModel(
        amount_ml=water_intake.amount_ml,
        created_at=water_intake.created_at,
      )

      session.add(model)
      session.commit()
      session.refresh(model)

      return WaterIntake(
        id=model.id,
        amount_ml=model.amount_ml,
        created_at=model.created_at,
      )

  def get_total_by_date(self, target_date: date) -> int:
    start_datetime = datetime.combine(target_date, time.min)
    end_datetime = datetime.combine(target_date, time.max)

    with SessionLocal() as session:
      total = session.query(func.sum(WaterIntakeModel.amount_ml)).filter(
        WaterIntakeModel.created_at >= start_datetime,
        WaterIntakeModel.created_at <= end_datetime,
      ).scalar()

      return int(total or 0)

  def get_all(self) -> list[WaterIntake]:
    with SessionLocal() as session:
      results = (
        session.query(WaterIntakeModel)
        .order_by(desc(WaterIntakeModel.created_at))
        .all()
      )

      return [
        WaterIntake(
          id=item.id,
          amount_ml=item.amount_ml,
          created_at=item.created_at,
        )
        for item in results
      ]

  def remove_last(self) -> bool:
    with SessionLocal() as session:
      last_item = (
        session.query(WaterIntakeModel)
        .order_by(desc(WaterIntakeModel.created_at))
        .first()
      )

      if last_item is None:
        return False

      session.delete(last_item)
      session.commit()

      return True

  def delete_by_id(self, water_intake_id: int) -> bool:
    with SessionLocal() as session:
      item = (
        session.query(WaterIntakeModel)
        .filter(WaterIntakeModel.id == water_intake_id)
        .first()
      )

      if item is None:
        return False

      session.delete(item)
      session.commit()

      return True

  def update_amount(self, water_intake_id: int, amount_ml: int) -> bool:
    with SessionLocal() as session:
      item = (
        session.query(WaterIntakeModel)
        .filter(WaterIntakeModel.id == water_intake_id)
        .first()
      )

      if item is None:
        return False

      item.amount_ml = amount_ml
      session.commit()

      return True

  def get_daily_totals(self, days: int = 7) -> list[dict]:
    today = date.today()
    start_date = today - timedelta(days=days - 1)

    result = []

    for index in range(days):
      current_date = start_date + timedelta(days=index)
      total_ml = self.get_total_by_date(current_date)

      result.append({
        "date": current_date,
        "total_ml": total_ml,
      })

    return result