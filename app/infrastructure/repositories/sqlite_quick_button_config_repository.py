from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import QuickButtonConfigModel
from app.domain.entities.quick_button_config import QuickButtonConfig
from app.domain.repositories.quick_button_config_repository import (
  QuickButtonConfigRepository,
)


class SqliteQuickButtonConfigRepository(QuickButtonConfigRepository):
  def get_config(self) -> QuickButtonConfig:
    with SessionLocal() as session:
      model = (
        session.query(QuickButtonConfigModel)
        .order_by(QuickButtonConfigModel.id.desc())
        .first()
      )

      if model is None:
        model = QuickButtonConfigModel(
          button_1_ml=200,
          button_2_ml=300,
          button_3_ml=500,
          updated_at=datetime.now(),
        )

        session.add(model)
        session.commit()
        session.refresh(model)

      return QuickButtonConfig(
        id=model.id,
        button_1_ml=model.button_1_ml,
        button_2_ml=model.button_2_ml,
        button_3_ml=model.button_3_ml,
        updated_at=model.updated_at,
      )

  def update_config(
    self,
    button_1_ml: int,
    button_2_ml: int,
    button_3_ml: int,
  ) -> QuickButtonConfig:
    with SessionLocal() as session:
      model = (
        session.query(QuickButtonConfigModel)
        .order_by(QuickButtonConfigModel.id.desc())
        .first()
      )

      if model is None:
        model = QuickButtonConfigModel(
          button_1_ml=button_1_ml,
          button_2_ml=button_2_ml,
          button_3_ml=button_3_ml,
          updated_at=datetime.now(),
        )

        session.add(model)

      else:
        model.button_1_ml = button_1_ml
        model.button_2_ml = button_2_ml
        model.button_3_ml = button_3_ml
        model.updated_at = datetime.now()

      session.commit()
      session.refresh(model)

      return QuickButtonConfig(
        id=model.id,
        button_1_ml=model.button_1_ml,
        button_2_ml=model.button_2_ml,
        button_3_ml=model.button_3_ml,
        updated_at=model.updated_at,
      )