from app.domain.entities.quick_button_config import QuickButtonConfig
from app.domain.repositories.quick_button_config_repository import (
  QuickButtonConfigRepository,
)


class QuickButtonService:
  def __init__(self, repository: QuickButtonConfigRepository):
    self._repository = repository

  def get_config(self) -> QuickButtonConfig:
    return self._repository.get_config()

  def update_config(
    self,
    button_1_ml: int,
    button_2_ml: int,
    button_3_ml: int,
  ) -> QuickButtonConfig:
    values = [button_1_ml, button_2_ml, button_3_ml]

    for value in values:
      if value < 50:
        raise ValueError("Cada botão deve ter no mínimo 50 ml.")

      if value > 5000:
        raise ValueError("Cada botão deve ter no máximo 5000 ml.")

    return self._repository.update_config(
      button_1_ml,
      button_2_ml,
      button_3_ml,
    )