from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout

from app.presentation.widgets.icon_widgets import CalendarIcon


class DateCard(QFrame):
  def __init__(self):
    super().__init__()

    self.date_label = QLabel("--/--/----")
    self.weekday_label = QLabel("-")

    self._setup_ui()

  def _setup_ui(self):
    self.setFixedHeight(92)
    self.setMinimumWidth(250)

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

    layout = QHBoxLayout(self)
    layout.setContentsMargins(20, 16, 20, 16)
    layout.setSpacing(14)

    icon = CalendarIcon()

    text_layout = QVBoxLayout()
    text_layout.setSpacing(2)

    self.date_label.setStyleSheet("""
      font-size: 22px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.weekday_label.setStyleSheet("""
      font-size: 13px;
      color: #607D9A;
    """)

    text_layout.addWidget(self.date_label)
    text_layout.addWidget(self.weekday_label)

    layout.addWidget(icon)
    layout.addLayout(text_layout)

  def update_date(self, date_text: str, weekday_text: str):
    self.date_label.setText(date_text)
    self.weekday_label.setText(weekday_text)