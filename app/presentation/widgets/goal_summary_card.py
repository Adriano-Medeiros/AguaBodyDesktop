from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
  QFrame,
  QLabel,
  QPushButton,
  QHBoxLayout,
  QVBoxLayout,
)

from app.presentation.widgets.icon_widgets import WaterCupIcon


class GoalSummaryCard(QFrame):
  edit_goal_clicked = Signal()

  def __init__(self):
    super().__init__()

    self.value_label = QLabel("2000 ml")
    self.edit_button = QPushButton("Editar meta")

    self._setup_ui()

  def _setup_ui(self):
    self.setMinimumHeight(150)

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
    main_layout.setContentsMargins(20, 18, 20, 18)
    main_layout.setSpacing(10)

    title_label = QLabel("Meta diária")
    title_label.setAlignment(Qt.AlignLeft)
    title_label.setStyleSheet("""
      font-size: 15px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    content_layout = QHBoxLayout()
    content_layout.setSpacing(16)

    icon = WaterCupIcon()

    text_layout = QVBoxLayout()
    text_layout.setSpacing(4)

    self.value_label.setAlignment(Qt.AlignLeft)
    self.value_label.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.edit_button.setCursor(Qt.PointingHandCursor)
    self.edit_button.clicked.connect(self.edit_goal_clicked.emit)
    self.edit_button.setStyleSheet("""
      QPushButton {
        background-color: transparent;
        color: #0F8BCB;
        border: none;
        text-align: left;
        font-size: 14px;
        font-weight: bold;
        padding: 0;
      }

      QPushButton:hover {
        color: #0A6FA3;
        text-decoration: underline;
      }
    """)

    text_layout.addWidget(self.value_label)
    text_layout.addWidget(self.edit_button)
    text_layout.addStretch()

    content_layout.addWidget(icon)
    content_layout.addLayout(text_layout, 1)

    main_layout.addWidget(title_label)
    main_layout.addLayout(content_layout)

  def update_goal(self, goal_ml: int):
    self.value_label.setText(f"{goal_ml} ml")