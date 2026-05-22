from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget
from PySide6.QtSvgWidgets import QSvgWidget
from app.utils.resource_path import resource_path

class CalendarIcon(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(44, 44)

  def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    pen = QPen(QColor("#1F3A5F"))
    pen.setWidth(2)

    painter.setPen(pen)
    painter.setBrush(Qt.NoBrush)

    painter.drawRoundedRect(9, 10, 26, 25, 4, 4)
    painter.drawLine(9, 17, 35, 17)

    painter.drawLine(16, 7, 16, 13)
    painter.drawLine(28, 7, 28, 13)

    painter.drawPoint(17, 23)
    painter.drawPoint(23, 23)
    painter.drawPoint(29, 23)
    painter.drawPoint(17, 29)
    painter.drawPoint(23, 29)
    painter.drawPoint(29, 29)


class WaterCupIcon(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(64, 64)

  def paintEvent(self, event):
    from PySide6.QtCore import QPointF
    from PySide6.QtGui import QBrush, QLinearGradient, QPainterPath, QPolygonF

    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    outline_color = QColor("#0F8BCB")
    water_top = QColor("#9BE3FF")
    water_bottom = QColor("#1FA8E8")
    glass_fill = QColor("#EAF6FF")

    cup_path = QPainterPath()
    cup_path.moveTo(18, 12)
    cup_path.lineTo(46, 12)
    cup_path.lineTo(41, 52)
    cup_path.quadTo(40, 56, 36, 56)
    cup_path.lineTo(28, 56)
    cup_path.quadTo(24, 56, 23, 52)
    cup_path.lineTo(18, 12)

    painter.setPen(QPen(outline_color, 2))
    painter.setBrush(glass_fill)
    painter.drawPath(cup_path)

    water_path = QPainterPath()
    water_path.moveTo(22, 30)
    water_path.cubicTo(27, 27, 32, 33, 37, 30)
    water_path.cubicTo(40, 28, 42, 29, 43, 30)
    water_path.lineTo(40, 50)
    water_path.quadTo(39, 53, 36, 53)
    water_path.lineTo(28, 53)
    water_path.quadTo(25, 53, 24, 50)
    water_path.lineTo(22, 30)

    gradient = QLinearGradient(22, 28, 22, 54)
    gradient.setColorAt(0, water_top)
    gradient.setColorAt(1, water_bottom)

    painter.setPen(Qt.NoPen)
    painter.setBrush(QBrush(gradient))
    painter.drawPath(water_path)

    painter.setPen(QPen(QColor("#6EC6F5"), 1))
    painter.setBrush(Qt.NoBrush)
    painter.drawLine(21, 21, 43, 21)

    painter.setPen(QPen(QColor("#B7ECFF"), 2))
    painter.drawLine(26, 17, 28, 48)

    painter.setPen(QPen(outline_color, 2))
    painter.setBrush(Qt.NoBrush)
    painter.drawPath(cup_path)

    painter.setPen(QPen(QColor("#FFFFFF"), 2))
    painter.drawLine(30, 34, 29, 47)
    
class ClockIcon(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(46, 46)

  def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    pen = QPen(QColor("#1F3A5F"))
    pen.setWidth(2)

    painter.setPen(pen)
    painter.setBrush(Qt.NoBrush)

    painter.drawEllipse(8, 8, 30, 30)

    painter.drawLine(23, 23, 23, 14)
    painter.drawLine(23, 23, 30, 28)


class BellIcon(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(34, 34)

  def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    pen = QPen(QColor("#1F3A5F"))
    pen.setWidth(2)

    painter.setPen(pen)
    painter.setBrush(Qt.NoBrush)

    painter.drawArc(10, 9, 14, 18, 0, 180 * 16)
    painter.drawLine(10, 18, 8, 25)
    painter.drawLine(24, 18, 26, 25)
    painter.drawLine(8, 25, 26, 25)
    painter.drawArc(14, 25, 6, 5, 180 * 16, 180 * 16)

class SmallWaterCupIcon(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(34, 34)

  def paintEvent(self, event):
    from PySide6.QtCore import QPoint
    from PySide6.QtGui import QBrush, QLinearGradient, QPainterPath, QPolygon

    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    outline_color = QColor("#0F8BCB")
    water_top = QColor("#9BE3FF")
    water_bottom = QColor("#1FA8E8")
    glass_fill = QColor("#EAF6FF")

    cup_path = QPainterPath()
    cup_path.moveTo(8, 5)
    cup_path.lineTo(26, 5)
    cup_path.lineTo(23, 29)
    cup_path.quadTo(22, 31, 20, 31)
    cup_path.lineTo(14, 31)
    cup_path.quadTo(12, 31, 11, 29)
    cup_path.lineTo(8, 5)

    painter.setPen(QPen(outline_color, 1.5))
    painter.setBrush(glass_fill)
    painter.drawPath(cup_path)

    water_path = QPainterPath()
    water_path.moveTo(10, 17)
    water_path.cubicTo(13, 15, 16, 19, 19, 17)
    water_path.cubicTo(21, 16, 23, 16, 24, 17)
    water_path.lineTo(22, 28)
    water_path.quadTo(21, 30, 19, 30)
    water_path.lineTo(15, 30)
    water_path.quadTo(13, 30, 12, 28)
    water_path.lineTo(10, 17)

    gradient = QLinearGradient(10, 16, 10, 31)
    gradient.setColorAt(0, water_top)
    gradient.setColorAt(1, water_bottom)

    painter.setPen(Qt.NoPen)
    painter.setBrush(QBrush(gradient))
    painter.drawPath(water_path)

    painter.setPen(QPen(QColor("#B7ECFF"), 1.2))
    painter.drawLine(14, 9, 15, 27)

    painter.setPen(QPen(outline_color, 1.5))
    painter.setBrush(Qt.NoBrush)
    painter.drawPath(cup_path)

class WaterSplashDecoration(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(260, 110)

  def paintEvent(self, event):
    from PySide6.QtCore import QPointF
    from PySide6.QtGui import (
      QBrush,
      QLinearGradient,
      QPainterPath,
      QRadialGradient,
    )

    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)

    painter.setPen(Qt.NoPen)

    # ----------------------------
    # Onda principal suave
    # ----------------------------

    gradient = QLinearGradient(40, 40, 240, 100)
    gradient.setColorAt(0, QColor(210, 243, 255, 120))
    gradient.setColorAt(0.5, QColor(120, 205, 245, 170))
    gradient.setColorAt(1, QColor(15, 139, 203, 210))

    wave = QPainterPath()

    wave.moveTo(20, 92)

    wave.cubicTo(
      55, 65,
      90, 88,
      120, 96,
    )

    wave.cubicTo(
      155, 104,
      185, 70,
      220, 45,
    )

    wave.lineTo(260, 15)
    wave.lineTo(260, 110)
    wave.lineTo(20, 110)
    wave.closeSubpath()

    painter.setBrush(QBrush(gradient))
    painter.drawPath(wave)

    # ----------------------------
    # Brilho superior
    # ----------------------------

    shine_pen = QPen(QColor(255, 255, 255, 120), 3)

    painter.setPen(shine_pen)

    shine = QPainterPath()

    shine.moveTo(45, 82)

    shine.cubicTo(
      80, 62,
      110, 90,
      140, 92,
    )

    shine.cubicTo(
      170, 95,
      200, 65,
      228, 48,
    )

    painter.drawPath(shine)

    painter.setPen(Qt.NoPen)

    # ----------------------------
    # Bolhas suaves
    # ----------------------------

    bubbles = [
      (58, 38, 5),
      (86, 26, 3),
      (112, 42, 4),
      (148, 20, 6),
      (176, 40, 4),
      (206, 22, 3),
      (228, 14, 5),
    ]

    for x, y, r in bubbles:
      bubble_gradient = QRadialGradient(QPointF(x - 1, y - 1), r)

      bubble_gradient.setColorAt(
        0,
        QColor(255, 255, 255, 200),
      )

      bubble_gradient.setColorAt(
        1,
        QColor(120, 205, 245, 120),
      )

      painter.setBrush(QBrush(bubble_gradient))

      painter.drawEllipse(
        QPointF(x, y),
        r,
        r,
      )

    # ----------------------------
    # Gotas discretas
    # ----------------------------

    drop_gradient = QLinearGradient(0, 0, 0, 18)

    drop_gradient.setColorAt(
      0,
      QColor(220, 248, 255, 200),
    )

    drop_gradient.setColorAt(
      1,
      QColor(50, 175, 235, 220),
    )

    drops = [
      (170, 55, 7),
      (236, 40, 9),
    ]

    painter.setBrush(QBrush(drop_gradient))

    for x, y, r in drops:
      drop = QPainterPath()

      drop.moveTo(x, y - r)

      drop.cubicTo(
        x + r,
        y,
        x + r,
        y + r,
        x,
        y + r + 2,
      )

      drop.cubicTo(
        x - r,
        y + r,
        x - r,
        y,
        x,
        y - r,
      )

      drop.closeSubpath()

      painter.drawPath(drop)
      
class WaterSplashSvgWidget(QSvgWidget):
  def __init__(self):
    super().__init__()

    svg_path = resource_path("app/assets/images/water_splash.svg")

    self.load(svg_path)
    self.setFixedSize(320, 150)
    self.setStyleSheet("""
      background-color: transparent;
      border: none;
    """)