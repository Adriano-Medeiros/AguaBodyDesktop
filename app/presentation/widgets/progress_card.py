from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout, QWidget


class ProgressCard(QWidget):
  def __init__(self):
    super().__init__()

    self.title_label = QLabel("Progresso diário")
    self.percent_label = QLabel("0%")
    self.progress_bar = QProgressBar()
    self.description_label = QLabel("Você está começando.")

    self._setup_ui()

  def _setup_ui(self):
    self.setStyleSheet("""
      QWidget {
        background-color: white;
        border-radius: 18px;
      }
    """)

    layout = QVBoxLayout(self)
    layout.setContentsMargins(24, 22, 24, 22)
    layout.setSpacing(14)

    self.title_label.setStyleSheet("""
      font-size: 15px;
      color: #607D9A;
    """)

    self.percent_label.setAlignment(Qt.AlignCenter)
    self.percent_label.setStyleSheet("""
      font-size: 48px;
      font-weight: bold;
      color: #0F8BCB;
    """)

    self.progress_bar.setRange(0, 100)
    self.progress_bar.setValue(0)
    self.progress_bar.setFixedHeight(16)
    self.progress_bar.setTextVisible(False)

    self.progress_bar.setStyleSheet("""
      QProgressBar {
        background-color: #EAF6FF;
        border: none;
        border-radius: 8px;
      }

      QProgressBar::chunk {
        background-color: #0F8BCB;
        border-radius: 8px;
      }
    """)

    self.description_label.setAlignment(Qt.AlignCenter)
    self.description_label.setStyleSheet("""
      font-size: 14px;
      color: #607D9A;
    """)

    layout.addWidget(self.title_label)
    layout.addWidget(self.percent_label)
    layout.addWidget(self.progress_bar)
    layout.addWidget(self.description_label)

  def update_progress(self, percent: int):
    self.percent_label.setText(f"{percent}%")
    self.progress_bar.setValue(percent)

    if percent >= 100:
      self.description_label.setText("Parabéns, meta concluída.")
    elif percent >= 70:
      self.description_label.setText("Excelente ritmo de hidratação.")
    elif percent >= 50:
      self.description_label.setText("Você está indo bem.")
    else:
      self.description_label.setText("Você está começando.")