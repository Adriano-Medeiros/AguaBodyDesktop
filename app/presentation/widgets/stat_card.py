from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatCard(QFrame):
  def __init__(self, title: str, value: str, subtitle: str = ""):
    super().__init__()

    self.title_label = QLabel(title)
    self.value_label = QLabel(value)
    self.subtitle_label = QLabel(subtitle)

    self._setup_ui()

  def _setup_ui(self):
    self.setMinimumHeight(120)

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

    layout = QVBoxLayout(self)
    layout.setContentsMargins(22, 20, 22, 20)
    layout.setSpacing(8)

    self.title_label.setStyleSheet("""
      font-size: 14px;
      color: #607D9A;
    """)

    self.value_label.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.subtitle_label.setStyleSheet("""
      font-size: 13px;
      color: #607D9A;
    """)

    layout.addWidget(self.title_label)
    layout.addWidget(self.value_label)
    layout.addWidget(self.subtitle_label)

  def set_value(self, value: str):
    self.value_label.setText(value)

  def set_subtitle(self, subtitle: str):
    self.subtitle_label.setText(subtitle)