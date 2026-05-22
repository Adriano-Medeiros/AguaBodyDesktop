from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout, QWidget


class CircularProgress(QWidget):
  def __init__(self):
    super().__init__()

    self.consumed_ml = 0
    self.goal_ml = 2000
    self.percent = 0

    self.setFixedSize(230, 230)

  def update_progress(self, consumed_ml: int, goal_ml: int):
    self.consumed_ml = consumed_ml
    self.goal_ml = goal_ml

    if goal_ml <= 0:
      self.percent = 0
    else:
      self.percent = min(round((consumed_ml / goal_ml) * 100), 100)

    self.update()

  def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    size = 185
    x = 22
    y = 22

    rect = QRectF(x, y, size, size)

    background_pen = QPen(QColor("#CDEBFF"), 14)
    background_pen.setCapStyle(Qt.RoundCap)
    painter.setPen(background_pen)
    painter.drawArc(rect, 0, 360 * 16)

    progress_pen = QPen(QColor("#0F76E5"), 14)
    progress_pen.setCapStyle(Qt.RoundCap)
    painter.setPen(progress_pen)

    start_angle = 90 * 16
    span_angle = -int((self.percent / 100) * 360 * 16)
    painter.drawArc(rect, start_angle, span_angle)

    font = QFont()
    font.setPointSize(24)
    font.setBold(True)

    painter.setFont(font)
    painter.setPen(QColor("#1F3A5F"))
    painter.drawText(
      QRectF(0, 82, self.width(), 42),
      Qt.AlignCenter,
      f"{self.consumed_ml} ml",
    )

    font.setPointSize(14)
    font.setBold(False)
    painter.setFont(font)

    painter.setPen(QColor("#607D9A"))
    painter.drawText(
      QRectF(0, 126, self.width(), 30),
      Qt.AlignCenter,
      f"de {self.goal_ml} ml",
    )

    font.setPointSize(24)
    painter.setFont(font)
    painter.setPen(QColor("#8BD7FF"))

    painter.drawText(
      QRectF(0, 48, self.width(), 34),
      Qt.AlignCenter,
      "💧",
    )


class TodayConsumptionCard(QFrame):
  def __init__(self):
    super().__init__()

    self.progress = CircularProgress()

    self.percent_label = QLabel("0%")
    self.percent_subtitle = QLabel("da meta")

    self.remaining_label = QLabel("2000 ml")
    self.remaining_subtitle = QLabel("restantes")

    self.footer_label = QLabel("💧 Foco, hidratação e disciplina!")

    self._setup_ui()

  def _setup_ui(self):
    self.setMinimumHeight(320)

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
    main_layout.setContentsMargins(24, 22, 24, 22)
    main_layout.setSpacing(0)

    title = QLabel("Consumo de hoje")
    title.setStyleSheet("""
      font-size: 18px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    content_layout = QHBoxLayout()
    content_layout.setSpacing(26)
    content_layout.setContentsMargins(0, 8, 0, 0)

    right_layout = QVBoxLayout()
    right_layout.setSpacing(4)

    self.percent_label.setStyleSheet("""
      font-size: 38px;
      font-weight: bold;
      color: #0F76E5;
    """)

    self.percent_subtitle.setStyleSheet("""
      font-size: 16px;
      color: #0F76E5;
    """)

    self.remaining_label.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
      margin-top: 22px;
    """)

    self.remaining_subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    right_layout.addStretch()
    right_layout.addWidget(self.percent_label)
    right_layout.addWidget(self.percent_subtitle)
    right_layout.addSpacing(18)
    right_layout.addWidget(self.remaining_label)
    right_layout.addWidget(self.remaining_subtitle)
    right_layout.addStretch()

    content_layout.addWidget(self.progress, alignment=Qt.AlignTop)
    content_layout.addLayout(right_layout, 1)

    self.footer_label.setFixedHeight(34)
    self.footer_label.setStyleSheet("""
      font-size: 15px;
      color: #1F3A5F;
      padding-top: 10px;
    """)

    main_layout.addWidget(title)
    main_layout.addLayout(content_layout)
    main_layout.addSpacing(10)
    main_layout.addWidget(self.footer_label)

  def update_consumption(self, consumed_ml: int, goal_ml: int):
    if goal_ml <= 0:
      percent = 0
    else:
      percent = min(round((consumed_ml / goal_ml) * 100), 100)

    remaining_ml = max(goal_ml - consumed_ml, 0)

    self.progress.update_progress(consumed_ml, goal_ml)

    self.percent_label.setText(f"{percent}%")
    self.remaining_label.setText(f"{remaining_ml} ml")

    if remaining_ml == 0:
      self.remaining_subtitle.setText("meta concluída")
      self.footer_label.setText("💧 Parabéns, meta diária atingida!")
    else:
      self.remaining_subtitle.setText("restantes")
      self.footer_label.setText("💧 Foco, hidratação e disciplina!")