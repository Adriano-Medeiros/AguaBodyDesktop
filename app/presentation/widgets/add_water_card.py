from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
  QFrame,
  QGridLayout,
  QLabel,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

from app.presentation.widgets.icon_widgets import (
  SmallWaterCupIcon,
  WaterSplashSvgWidget,
)


class QuickWaterButton(QPushButton):
  def __init__(self, amount_ml: int):
    super().__init__()

    self.amount_ml = amount_ml
    self.icon_widget = SmallWaterCupIcon()
    self.text_label = QLabel(f"+{amount_ml} ml")

    self._setup_ui()

  def _setup_ui(self):
    self.setFixedHeight(82)

    self.setStyleSheet("""
      QPushButton {
        background-color: #EAF6FF;
        color: #0F8BCB;
        border: 1px solid #B8DFF5;
        border-radius: 14px;
        font-size: 16px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #D4ECFF;
      }
    """)

    layout = QVBoxLayout(self)
    layout.setContentsMargins(8, 8, 8, 8)
    layout.setSpacing(2)
    layout.setAlignment(Qt.AlignCenter)

    self.text_label.setAlignment(Qt.AlignCenter)
    self.text_label.setStyleSheet("""
      QLabel {
        background-color: transparent;
        border: none;
        color: #0F8BCB;
        font-size: 16px;
        font-weight: bold;
      }
    """)

    layout.addWidget(self.icon_widget, alignment=Qt.AlignCenter)
    layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

  def set_amount(self, amount_ml: int):
    self.amount_ml = amount_ml
    self.text_label.setText(f"+{amount_ml} ml")


class AddWaterCard(QFrame):
  add_water_clicked = Signal(int)
  custom_water_clicked = Signal()
  remove_last_clicked = Signal()

  def __init__(self):
    super().__init__()

    self.quick_amounts = [200, 300, 500]

    self.button_1 = QuickWaterButton(200)
    self.button_2 = QuickWaterButton(300)
    self.button_3 = QuickWaterButton(500)
    self.custom_button = QPushButton("+\nPersonalizado")
    self.remove_button = QPushButton("Remover último registro")
    self.splash = WaterSplashSvgWidget()

    self._setup_ui()

  def _setup_ui(self):
    self.setMinimumHeight(185)

    self.setStyleSheet("""
      QFrame {
        background-color: white;
        border-radius: 18px;
        border: 1px solid #E6EEF5;
      }

      QLabel {
        background-color: transparent;
        border: none;
      }
    """)

    main_layout = QVBoxLayout(self)
    main_layout.setContentsMargins(22, 18, 22, 18)
    main_layout.setSpacing(14)

    title = QLabel("Adicionar água")
    title.setStyleSheet("""
      font-size: 20px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    content = QWidget()
    content.setStyleSheet("""
      QWidget {
        background-color: transparent;
        border: none;
      }
    """)

    buttons_layout = QGridLayout(content)
    buttons_layout.setContentsMargins(0, 0, 0, 0)
    buttons_layout.setSpacing(14)

    self.button_1.clicked.connect(
      lambda: self.add_water_clicked.emit(self.quick_amounts[0])
    )
    self.button_2.clicked.connect(
      lambda: self.add_water_clicked.emit(self.quick_amounts[1])
    )
    self.button_3.clicked.connect(
      lambda: self.add_water_clicked.emit(self.quick_amounts[2])
    )

    self.custom_button.setFixedHeight(82)
    self.custom_button.clicked.connect(self.custom_water_clicked.emit)
    self.custom_button.setStyleSheet("""
      QPushButton {
        background-color: white;
        color: #0F8BCB;
        border: 1px dashed #B8DFF5;
        border-radius: 14px;
        font-size: 16px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #EAF6FF;
      }
    """)

    self.remove_button.setFixedHeight(42)
    self.remove_button.clicked.connect(self._emit_remove_last_clicked)
    self.remove_button.setStyleSheet("""
      QPushButton {
        background-color: #FFEAEA;
        color: #D64545;
        border: 1px solid #F3C1C1;
        border-radius: 12px;
        font-size: 15px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #FFDADA;
      }
    """)

    self.splash.setFixedSize(210, 95)
    self.splash.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    buttons_layout.addWidget(self.button_1, 0, 0)
    buttons_layout.addWidget(self.button_2, 0, 1)
    buttons_layout.addWidget(self.button_3, 0, 2)
    buttons_layout.addWidget(self.custom_button, 0, 3)
    buttons_layout.addWidget(
      self.splash,
      0,
      4,
      alignment=Qt.AlignRight | Qt.AlignBottom,
    )

    buttons_layout.setColumnStretch(0, 1)
    buttons_layout.setColumnStretch(1, 1)
    buttons_layout.setColumnStretch(2, 1)
    buttons_layout.setColumnStretch(3, 1)
    buttons_layout.setColumnStretch(4, 1)

    main_layout.addWidget(title)
    main_layout.addWidget(content)
    main_layout.addWidget(self.remove_button)

  def _emit_remove_last_clicked(self):
    self.remove_last_clicked.emit()

  def update_quick_buttons(self, amounts: list[int]):
    self.quick_amounts = amounts

    self.button_1.set_amount(amounts[0])
    self.button_2.set_amount(amounts[1])
    self.button_3.set_amount(amounts[2])