from PySide6.QtWidgets import (
  QFrame,
  QLabel,
  QHBoxLayout,
  QVBoxLayout,
)

from app.presentation.widgets.icon_widgets import BellIcon, ClockIcon


class NextReminderCard(QFrame):
  def __init__(self):
    super().__init__()

    self.time_label = QLabel("--:--")
    self.subtitle_label = QLabel("Lembretes ativos")

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
    main_layout.setContentsMargins(20, 16, 20, 16)
    main_layout.setSpacing(14)

    title = QLabel("Próximo lembrete")
    title.setStyleSheet("""
      font-size: 15px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    content_layout = QHBoxLayout()
    content_layout.setSpacing(12)

    icon = ClockIcon()
    bell_icon = BellIcon()

    text_layout = QVBoxLayout()
    text_layout.setSpacing(2)

    self.time_label.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.subtitle_label.setStyleSheet("""
      font-size: 13px;
      color: #607D9A;
    """)

    text_layout.addWidget(self.time_label)
    text_layout.addWidget(self.subtitle_label)

    content_layout.addWidget(icon)
    content_layout.addLayout(text_layout, 1)
    content_layout.addWidget(bell_icon)

    main_layout.addWidget(title)
    main_layout.addSpacing(4)
    main_layout.addLayout(content_layout)
    main_layout.addStretch()

  def update_reminder(self, time_text: str, subtitle_text: str):
    self.time_label.setText(time_text)
    self.subtitle_label.setText(subtitle_text)