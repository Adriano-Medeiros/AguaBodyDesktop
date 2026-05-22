from PySide6.QtWidgets import (
  QGridLayout,
  QLabel,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.statistics_viewmodel import StatisticsViewModel
from app.presentation.widgets.stat_card import StatCard
from app.presentation.widgets.weekly_chart_card import WeeklyChartCard


class StatisticsView(QWidget):
  def __init__(self):
    super().__init__()

    self.viewmodel = StatisticsViewModel()

    self.average_card = StatCard("Média diária", "0 ml", "Últimos 7 dias")
    self.best_day_card = StatCard("Melhor dia", "0 ml", "-")
    self.streak_card = StatCard("Sequência", "0 dias", "Consecutivos")
    self.weekly_chart = WeeklyChartCard()

    self._setup_ui()
    self.reload_data()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(22)

    title = QLabel("Estatísticas")
    title.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    subtitle = QLabel("Acompanhe sua evolução de hidratação.")
    subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    cards_layout = QGridLayout()
    cards_layout.setSpacing(16)

    cards_layout.addWidget(self.average_card, 0, 0)
    cards_layout.addWidget(self.best_day_card, 0, 1)
    cards_layout.addWidget(self.streak_card, 0, 2)

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addLayout(cards_layout)
    layout.addWidget(self.weekly_chart)
    layout.addStretch()

  def reload_data(self):
    summary = self.viewmodel.get_summary()

    self.average_card.set_value(f"{summary['average_ml']} ml")
    self.average_card.set_subtitle("Últimos 7 dias")

    self.best_day_card.set_value(f"{summary['best_day_ml']} ml")
    self.best_day_card.set_subtitle(
      summary["best_day_date"].strftime("%d/%m/%Y")
    )

    self.streak_card.set_value(f"{summary['streak']} dias")
    self.streak_card.set_subtitle("Consecutivos")

    self.weekly_chart.set_data(
      summary["daily_totals"],
      summary["goal_ml"],
    )