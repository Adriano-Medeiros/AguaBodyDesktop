from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
  QCheckBox,
  QLabel,
  QLineEdit,
  QMessageBox,
  QPushButton,
  QScrollArea,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.reminder_viewmodel import ReminderViewModel
from app.presentation.viewmodels.settings_viewmodel import SettingsViewModel
from PySide6.QtWidgets import QCheckBox
from app.infrastructure.services.startup_service import StartupService

class SettingsView(QWidget):
  reminder_config_updated = Signal()
  quick_buttons_updated = Signal()

  def __init__(self):
    super().__init__()

    self.viewmodel = SettingsViewModel()
    self.reminder_viewmodel = ReminderViewModel()

    self.goal_input = QLineEdit()
    self.reminder_enabled_checkbox = QCheckBox("Ativar lembretes")
    self.reminder_interval_input = QLineEdit()

    self.quick_button_1_input = QLineEdit()
    self.quick_button_2_input = QLineEdit()
    self.quick_button_3_input = QLineEdit()
    self.startup_checkbox = QCheckBox(
      "Iniciar automaticamente com o Windows"
    )
    self._setup_ui()
    self._load_data()

  def _setup_ui(self):
    main_layout = QVBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("""
      QScrollArea {
        border: none;
        background-color: #F4F9FD;
      }

      QScrollBar:vertical {
        background-color: #EAF6FF;
        width: 10px;
        border-radius: 5px;
      }

      QScrollBar::handle:vertical {
        background-color: #B8DFF5;
        border-radius: 5px;
      }
    """)

    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(18)

    title = QLabel("Configurações")
    title.setStyleSheet("font-size: 28px; font-weight: bold; color: #1F3A5F;")

    subtitle = QLabel("Defina sua meta diária, botões rápidos e lembretes.")
    subtitle.setStyleSheet("font-size: 16px; color: #607D9A;")

    goal_title = self._section_title("Meta diária")
    goal_label = self._field_label("Meta diária em ml")

    self.goal_input.setFixedHeight(45)
    self.goal_input.setPlaceholderText("Exemplo: 2000")
    self.goal_input.setStyleSheet(self._input_style())

    save_goal_button = QPushButton("Salvar meta")
    save_goal_button.setFixedHeight(46)
    save_goal_button.clicked.connect(self._on_save_goal_clicked)
    save_goal_button.setStyleSheet(self._primary_button_style())

    quick_title = self._section_title("Botões rápidos")

    self.quick_button_1_input.setFixedHeight(45)
    self.quick_button_2_input.setFixedHeight(45)
    self.quick_button_3_input.setFixedHeight(45)

    self.quick_button_1_input.setPlaceholderText("Botão 1 — Ex: 200")
    self.quick_button_2_input.setPlaceholderText("Botão 2 — Ex: 300")
    self.quick_button_3_input.setPlaceholderText("Botão 3 — Ex: 500")

    self.quick_button_1_input.setStyleSheet(self._input_style())
    self.quick_button_2_input.setStyleSheet(self._input_style())
    self.quick_button_3_input.setStyleSheet(self._input_style())

    save_quick_buttons_button = QPushButton("Salvar botões rápidos")
    save_quick_buttons_button.setFixedHeight(46)
    save_quick_buttons_button.clicked.connect(self._on_save_quick_buttons_clicked)
    save_quick_buttons_button.setStyleSheet(self._primary_button_style())

    self.startup_checkbox.setChecked(
      StartupService.is_enabled()
    )

    self.startup_checkbox.setStyleSheet("""
      font-size: 15px;
      color: #1F3A5F;
    """)

    self.startup_checkbox.stateChanged.connect(
      self._on_startup_changed
    )

    layout.addWidget(self.startup_checkbox)

    reminder_title = self._section_title("Lembretes")

    self.reminder_enabled_checkbox.setStyleSheet("""
      QCheckBox {
        font-size: 15px;
        color: #1F3A5F;
        padding: 6px 0;
      }
    """)

    interval_label = self._field_label("Intervalo entre lembretes em minutos")

    self.reminder_interval_input.setFixedHeight(45)
    self.reminder_interval_input.setPlaceholderText("Exemplo: 60")
    self.reminder_interval_input.setStyleSheet(self._input_style())

    save_reminder_button = QPushButton("Salvar lembretes")
    save_reminder_button.setFixedHeight(46)
    save_reminder_button.clicked.connect(self._on_save_reminder_clicked)
    save_reminder_button.setStyleSheet(self._primary_button_style())

    test_button = QPushButton("Testar notificação")
    test_button.setFixedHeight(46)
    test_button.clicked.connect(self._on_test_notification)
    test_button.setStyleSheet(self._secondary_button_style())

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addSpacing(18)

    layout.addWidget(goal_title)
    layout.addWidget(goal_label)
    layout.addWidget(self.goal_input)
    layout.addWidget(save_goal_button)

    layout.addSpacing(24)
    layout.addWidget(quick_title)
    layout.addWidget(self.quick_button_1_input)
    layout.addWidget(self.quick_button_2_input)
    layout.addWidget(self.quick_button_3_input)
    layout.addWidget(save_quick_buttons_button)

    layout.addSpacing(24)
    layout.addWidget(reminder_title)
    layout.addWidget(self.reminder_enabled_checkbox)
    layout.addWidget(interval_label)
    layout.addWidget(self.reminder_interval_input)
    layout.addWidget(save_reminder_button)
    layout.addWidget(test_button)

    layout.addSpacing(30)
    layout.addStretch()

    scroll_area.setWidget(container)
    main_layout.addWidget(scroll_area)

  def _section_title(self, text: str) -> QLabel:
    label = QLabel(text)
    label.setStyleSheet("""
      font-size: 20px;
      font-weight: bold;
      color: #1F3A5F;
      padding-top: 8px;
    """)
    return label

  def _field_label(self, text: str) -> QLabel:
    label = QLabel(text)
    label.setStyleSheet("""
      font-size: 15px;
      font-weight: bold;
      color: #1F3A5F;
    """)
    return label

  def _load_data(self):
    goal_ml = self.viewmodel.get_goal_ml()
    self.goal_input.setText(str(goal_ml))

    quick_config = self.viewmodel.get_quick_button_config()
    self.quick_button_1_input.setText(str(quick_config.button_1_ml))
    self.quick_button_2_input.setText(str(quick_config.button_2_ml))
    self.quick_button_3_input.setText(str(quick_config.button_3_ml))

    reminder_config = self.reminder_viewmodel.get_config()
    self.reminder_enabled_checkbox.setChecked(reminder_config.enabled)
    self.reminder_interval_input.setText(str(reminder_config.interval_minutes))

  def _on_save_goal_clicked(self):
    try:
      goal_ml = int(self.goal_input.text().strip())
      self.viewmodel.update_goal(goal_ml)

      QMessageBox.information(
        self,
        "Meta atualizada",
        "Meta diária atualizada com sucesso.",
      )

    except ValueError as error:
      QMessageBox.warning(self, "Valor inválido", str(error))

  def _on_save_quick_buttons_clicked(self):
    try:
      button_1_ml = int(self.quick_button_1_input.text().strip())
      button_2_ml = int(self.quick_button_2_input.text().strip())
      button_3_ml = int(self.quick_button_3_input.text().strip())

      self.viewmodel.update_quick_buttons(
        button_1_ml,
        button_2_ml,
        button_3_ml,
      )

      self.quick_buttons_updated.emit()

      QMessageBox.information(
        self,
        "Botões atualizados",
        "Botões rápidos atualizados com sucesso.",
      )

    except ValueError as error:
      QMessageBox.warning(self, "Valor inválido", str(error))

  def _on_save_reminder_clicked(self):
    try:
      enabled = self.reminder_enabled_checkbox.isChecked()
      interval_minutes = int(self.reminder_interval_input.text().strip())

      self.reminder_viewmodel.update_config(
        enabled=enabled,
        interval_minutes=interval_minutes,
      )

      self.reminder_config_updated.emit()

      QMessageBox.information(
        self,
        "Lembretes atualizados",
        "Configuração de lembretes salva com sucesso.",
      )

    except ValueError as error:
      QMessageBox.warning(self, "Valor inválido", str(error))

  def _on_test_notification(self):
    self.reminder_viewmodel.show_test_notification()

    QMessageBox.information(
      self,
      "Notificação enviada",
      "A notificação foi enviada para o Windows.",
    )

  def _input_style(self) -> str:
    return """
      QLineEdit {
        background-color: white;
        border: 1px solid #D9E8F2;
        border-radius: 10px;
        padding: 0 14px;
        font-size: 15px;
        color: #1F3A5F;
      }

      QLineEdit:focus {
        border: 1px solid #0F8BCB;
      }
    """

  def _primary_button_style(self) -> str:
    return """
      QPushButton {
        background-color: #0F8BCB;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #0A6FA3;
      }
    """

  def _secondary_button_style(self) -> str:
    return """
      QPushButton {
        background-color: white;
        color: #0F8BCB;
        border: 1px solid #0F8BCB;
        border-radius: 10px;
        font-size: 15px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #EAF6FF;
      }
    """
    
  def _on_startup_changed(self, state):
    if self.startup_checkbox.isChecked():
      StartupService.enable()
    else:
      StartupService.disable()