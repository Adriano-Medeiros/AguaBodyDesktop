from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from app.utils.resource_path import resource_path


class Sidebar(QWidget):
  navigate = Signal(str)

  def __init__(self):
    super().__init__()

    self.menu_buttons = {}

    self.setFixedWidth(230)
    self.setStyleSheet("""
      QWidget {
        background-color: #F7FBFF;
      }

      QLabel {
        background-color: transparent;
      }
    """)

    self._setup_ui()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(18, 24, 18, 18)
    layout.setSpacing(10)

    title = QLabel("💧 AguaBody")
    title.setStyleSheet("""
      font-size: 24px;
      font-weight: bold;
      color: #0F4C81;
      padding-bottom: 22px;
    """)

    layout.addWidget(title)

    self._add_menu_button(
      layout,
      key="dashboard",
      text="Dashboard",
      icon_path="app/assets/icons/sidebar/home.svg",
      checked=True,
    )

    self._add_menu_button(
      layout,
      key="history",
      text="Histórico",
      icon_path="app/assets/icons/sidebar/history.svg",
    )

    self._add_menu_button(
      layout,
      key="statistics",
      text="Estatísticas",
      icon_path="app/assets/icons/sidebar/statistics.svg",
    )

    self._add_menu_button(
      layout,
      key="goals",
      text="Metas",
      icon_path="app/assets/icons/sidebar/goals.svg",
    )

    self._add_menu_button(
      layout,
      key="reminders",
      text="Lembretes",
      icon_path="app/assets/icons/sidebar/reminders.svg",
    )

    self._add_menu_button(
      layout,
      key="settings",
      text="Configurações",
      icon_path="app/assets/icons/sidebar/settings.svg",
    )

    layout.addStretch()

    self._add_menu_button(
      layout,
      key="about",
      text="Sobre",
      icon_path="app/assets/icons/sidebar/about.svg",
    )

  def _add_menu_button(
    self,
    layout: QVBoxLayout,
    key: str,
    text: str,
    icon_path: str,
    checked: bool = False,
  ):
    button = QPushButton(text)

    button.setCheckable(True)
    button.setChecked(checked)

    normal_icon = QIcon(
      resource_path(icon_path)
    )

    active_icon = QIcon(
      resource_path(
        icon_path.replace(".svg", "_active.svg")
      )
    )

    button.normal_icon = normal_icon
    button.active_icon = active_icon

    if checked:
      button.setIcon(active_icon)
    else:
      button.setIcon(normal_icon)

    button.setIconSize(QSize(22, 22))
    button.setFixedHeight(54)

    button.setStyleSheet("""
      QPushButton {
        background-color: transparent;
        border: none;
        border-radius: 14px;
        padding: 12px 16px;
        text-align: left;
        font-size: 15px;
        font-weight: 500;
        color: #5E7188;
      }

      QPushButton:hover {
        background-color: #EEF6FF;
        color: #0F8BCB;
      }

      QPushButton:checked {
        background-color: #E3F1FF;
        color: #0F8BCB;
        font-weight: bold;
      }
    """)

    button.clicked.connect(
      lambda: self._on_menu_clicked(key)
    )

    self.menu_buttons[key] = button
    layout.addWidget(button)
    
  def _on_menu_clicked(self, key: str):
    self.set_active(key)
    self.navigate.emit(key)

  def set_active(self, key: str):
    for button_key, button in self.menu_buttons.items():

      is_active = button_key == key

      button.setChecked(is_active)

      if is_active:
        button.setIcon(button.active_icon)
      else:
        button.setIcon(button.normal_icon)