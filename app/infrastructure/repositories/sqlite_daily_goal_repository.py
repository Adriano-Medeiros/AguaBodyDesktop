from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import DailyGoalModel
from app.domain.entities.daily_goal import DailyGoal
from app.domain.repositories.daily_goal_repository import DailyGoalRepository


class SqliteDailyGoalRepository(DailyGoalRepository):
  def get_active_goal(self) -> DailyGoal:
    with SessionLocal() as session:
      model = (
        session.query(DailyGoalModel)
        .filter(DailyGoalModel.active == True)
        .order_by(DailyGoalModel.id.desc())
        .first()
      )

      if model is None:
        model = DailyGoalModel(
          goal_ml=2000,
          active=True,
          created_at=datetime.now(),
          updated_at=datetime.now(),
        )

        session.add(model)
        session.commit()
        session.refresh(model)

      return DailyGoal(
        id=model.id,
        goal_ml=model.goal_ml,
        active=model.active,
        created_at=model.created_at,
        updated_at=model.updated_at,
      )

  def update_goal(self, goal_ml: int) -> DailyGoal:
    with SessionLocal() as session:
      model = (
        session.query(DailyGoalModel)
        .filter(DailyGoalModel.active == True)
        .order_by(DailyGoalModel.id.desc())
        .first()
      )

      if model is None:
        model = DailyGoalModel(
          goal_ml=goal_ml,
          active=True,
          created_at=datetime.now(),
          updated_at=datetime.now(),
        )
        session.add(model)
      else:
        model.goal_ml = goal_ml
        model.updated_at = datetime.now()

      session.commit()
      session.refresh(model)

      return DailyGoal(
        id=model.id,
        goal_ml=model.goal_ml,
        active=model.active,
        created_at=model.created_at,
        updated_at=model.updated_at,
      )