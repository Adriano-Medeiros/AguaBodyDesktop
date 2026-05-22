from abc import ABC, abstractmethod

from app.domain.entities.quick_button_config import QuickButtonConfig


class QuickButtonConfigRepository(ABC):
  @abstractmethod
  def get_config(self) -> QuickButtonConfig:
    pass

  @abstractmethod
  def update_config(
    self,
    button_1_ml: int,
    button_2_ml: int,
    button_3_ml: int,
  ) -> QuickButtonConfig:
    pass