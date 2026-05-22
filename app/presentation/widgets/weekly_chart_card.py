from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class WeeklyChart(QWidget):
  def __init__(self):
    super().__init__()

    self.data = []
    self.goal_ml = 2000

    self.setMinimumHeight(220)

  def set_data(self, data: list[dict], goal_ml: int):
    self.data = data
    self.goal_ml = goal_ml
    self.update()

  def paintEvent(self, event):
    if not self.data:
      return

    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    width = self.width()
    height = self.height()

    margin_left = 35
    margin_right = 20
    margin_top = 20
    margin_bottom = 45

    chart_width = width - margin_left - margin_right
    chart_height = height - margin_top - margin_bottom

    max_value = max(
      [item["total_ml"] for item in self.data] + [self.goal_ml, 1]
    )

    axis_pen = QPen(QColor("#D9E8F2"))
    axis_pen.setWidth(1)
    painter.setPen(axis_pen)

    baseline_y = margin_top + chart_height

    painter.drawLine(
      margin_left,
      baseline_y,
      margin_left + chart_width,
      baseline_y,
    )

    goal_y = baseline_y - int(
      (self.goal_ml / max_value) * chart_height
    )

    goal_pen = QPen(QColor("#9CCFEA"))
    goal_pen.setWidth(1)
    goal_pen.setStyle(Qt.DashLine)
    painter.setPen(goal_pen)

    painter.drawLine(
      margin_left,
      goal_y,
      margin_left + chart_width,
      goal_y,
    )

    painter.setPen(QColor("#607D9A"))
    painter.drawText(5, goal_y + 4, "Meta")

    bar_count = len(self.data)
    spacing = 12

    bar_width = int(
      (chart_width - spacing * (bar_count - 1)) / bar_count
    )

    for index, item in enumerate(self.data):
      total_ml = item["total_ml"]

      x = margin_left + index * (bar_width + spacing)

      bar_height = int(
        (total_ml / max_value) * chart_height
      )

      y = baseline_y - bar_height

      if total_ml < self.goal_ml:
        bar_color = QColor("#E57373")
      elif total_ml == self.goal_ml:
        bar_color = QColor("#0F8BCB")
      else:
        bar_color = QColor("#81C784")

      value_color = QColor("#FFFFFF")

      painter.setBrush(bar_color)
      painter.setPen(Qt.NoPen)

      painter.drawRoundedRect(
        x,
        y,
        bar_width,
        bar_height,
        8,
        8,
      )

      painter.setPen(QColor("#1F3A5F"))

      day_text = item["date"].strftime("%d/%m")

      painter.drawText(
        x,
        baseline_y + 20,
        bar_width,
        18,
        Qt.AlignCenter,
        day_text,
      )

      painter.setPen(value_color)

      painter.drawText(
        x,
        y + 6,
        bar_width,
        18,
        Qt.AlignCenter,
        f"{total_ml}",
      )


class WeeklyChartCard(QFrame):
  def __init__(self):
    super().__init__()

    self.title_label = QLabel("Consumo dos últimos 7 dias")
    self.subtitle_label = QLabel("Comparativo diário em ml")
    self.chart = WeeklyChart()

    self._setup_ui()

  def _setup_ui(self):
    self.setMinimumHeight(320)

    self.setObjectName("weeklyChartCard")

    self.setStyleSheet("""
      QFrame#weeklyChartCard {
        background-color: white;
        border-radius: 18px;
        border: 1px solid #E6EEF5;
      }

      QLabel {
        background-color: transparent;
        border: none;
      }
    """)

    self.chart.setStyleSheet("""
      background-color: white;
      border: none;
    """)

    layout = QVBoxLayout(self)
    layout.setContentsMargins(24, 22, 24, 22)
    layout.setSpacing(8)

    self.title_label.setStyleSheet("""
      font-size: 18px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.subtitle_label.setStyleSheet("""
      font-size: 14px;
      color: #607D9A;
    """)

    layout.addWidget(self.title_label)
    layout.addWidget(self.subtitle_label)
    layout.addWidget(self.chart)

  def set_data(self, data: list[dict], goal_ml: int):
    self.chart.set_data(data, goal_ml)