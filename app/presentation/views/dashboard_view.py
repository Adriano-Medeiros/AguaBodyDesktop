from datetime import datetime, timedelta

from PySide6.QtWidgets import (
  QHBoxLayout,
  QInputDialog,
  QLabel,
  QMessageBox,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.dashboard_viewmodel import DashboardViewModel
from app.presentation.viewmodels.reminder_viewmodel import ReminderViewModel
from app.presentation.widgets.add_water_card import AddWaterCard
from app.presentation.widgets.date_card import DateCard
from app.presentation.widgets.goal_summary_card import GoalSummaryCard
from app.presentation.widgets.next_reminder_card import NextReminderCard
from app.presentation.widgets.today_consumption_card import TodayConsumptionCard


class DashboardView(QWidget):
  def __init__(self):
    super().__init__()

    self.viewmodel = DashboardViewModel()
    self.reminder_viewmodel = ReminderViewModel(self._show_main_window)

    self.date_card = DateCard()
    self.goal_summary_card = GoalSummaryCard()
    self.next_reminder_card = NextReminderCard()
    self.today_consumption_card = TodayConsumptionCard()
    self.add_water_card = AddWaterCard()

    self._setup_ui()
    self.reload_quick_buttons()
    self._update_cards()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(22)

    header_layout = QHBoxLayout()
    header_layout.setSpacing(18)

    text_header = QVBoxLayout()
    text_header.setSpacing(4)

    title = QLabel("Olá, cuide de você!")
    title.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    subtitle = QLabel("Beba água e mantenha-se hidratado.")
    subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    text_header.addWidget(title)
    text_header.addWidget(subtitle)

    header_layout.addLayout(text_header, 1)
    header_layout.addStretch()
    header_layout.addWidget(self.date_card)

    main_layout = QHBoxLayout()
    main_layout.setSpacing(18)

    left_layout = QVBoxLayout()
    left_layout.setSpacing(0)
    left_layout.addWidget(self.today_consumption_card)

    right_layout = QVBoxLayout()
    right_layout.setSpacing(16)

    self.goal_summary_card.setSizePolicy(
      self.goal_summary_card.sizePolicy().horizontalPolicy(),
      self.goal_summary_card.sizePolicy().verticalPolicy(),
    )

    self.next_reminder_card.setSizePolicy(
      self.next_reminder_card.sizePolicy().horizontalPolicy(),
      self.next_reminder_card.sizePolicy().verticalPolicy(),
    )

    right_layout.addWidget(self.goal_summary_card, 1)
    right_layout.addWidget(self.next_reminder_card, 1)

    main_layout.addLayout(left_layout, 2)
    main_layout.addLayout(right_layout, 1)

    self.add_water_card.remove_last_clicked.connect(self._on_remove_last)
    self.add_water_card.add_water_clicked.connect(self._on_add_water)
    self.add_water_card.custom_water_clicked.connect(self._on_add_custom_water)
    self.goal_summary_card.edit_goal_clicked.connect(self._on_edit_goal_clicked)

    layout.addLayout(header_layout)
    layout.addLayout(main_layout)
    layout.addWidget(self.add_water_card)
    layout.addStretch()

  def reload_quick_buttons(self):
    config = self.viewmodel.get_quick_button_config()

    quick_amounts = [
      config.button_1_ml,
      config.button_2_ml,
      config.button_3_ml,
    ]

    self.add_water_card.update_quick_buttons(quick_amounts)

  def _on_add_water(self, amount_ml: int):
    self.viewmodel.add_water(amount_ml)
    self._update_cards()

  def _on_add_custom_water(self):
    amount_ml, ok = QInputDialog.getInt(
      self,
      "Adicionar água",
      "Informe a quantidade em ml:",
      250,
      1,
      5000,
      50,
    )

    if ok:
      self.viewmodel.add_water(amount_ml)
      self._update_cards()

  def _on_remove_last(self):
    reply = QMessageBox.question(
      self,
      "Remover registro",
      "Deseja remover o último registro de água?",
      QMessageBox.Yes | QMessageBox.No,
    )

    if reply == QMessageBox.Yes:
      self.viewmodel.remove_last_water()
      self._update_cards()

  def _update_cards(self):
    state = self.viewmodel.get_state()

    today = datetime.now()
    weekday_name = self._get_weekday_name(today.weekday())

    self.date_card.update_date(
      today.strftime("%d/%m/%Y"),
      weekday_name,
    )

    self.goal_summary_card.update_goal(state.goal_ml)

    self.today_consumption_card.update_consumption(
      consumed_ml=state.consumed_ml,
      goal_ml=state.goal_ml,
    )

    reminder_config = self.reminder_viewmodel.get_config()

    if reminder_config.enabled:
      next_time_text = self.reminder_viewmodel.get_next_reminder_text()

      self.next_reminder_card.update_reminder(
        next_time_text,
        f"A cada {reminder_config.interval_minutes} min",
      )

    else:
      self.next_reminder_card.update_reminder(
        "Desativado",
        "Lembretes inativos",
      )
  
  
  def _get_weekday_name(self, weekday_index: int) -> str:
    weekdays = [
      "Segunda-feira",
      "Terça-feira",
      "Quarta-feira",
      "Quinta-feira",
      "Sexta-feira",
      "Sábado",
      "Domingo",
    ]

    return weekdays[weekday_index]

  def _on_edit_goal_clicked(self):
    main_window = self.window()

    if hasattr(main_window, "_navigate"):
      main_window._navigate("goals")
      
  def _show_main_window(self):
    main_window = self.window()

    if hasattr(main_window, "show_main_window"):
      main_window.show_main_window()