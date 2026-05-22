from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
  QCheckBox,
  QLabel,
  QLineEdit,
  QMessageBox,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.reminder_viewmodel import ReminderViewModel


class RemindersView(QWidget):
  reminder_config_updated = Signal()

  def __init__(self):
    super().__init__()

    self.viewmodel = ReminderViewModel()

    self.enabled_checkbox = QCheckBox("Ativar lembretes")
    self.interval_input = QLineEdit()

    self._setup_ui()
    self.reload_data()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(18)

    title = QLabel("Lembretes")
    title.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    subtitle = QLabel("Configure notificações para não esquecer de beber água.")
    subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    self.enabled_checkbox.setStyleSheet("""
      QCheckBox {
        font-size: 16px;
        color: #1F3A5F;
        padding: 8px 0;
      }
    """)

    interval_label = QLabel("Intervalo entre lembretes em minutos")
    interval_label.setStyleSheet("""
      font-size: 15px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.interval_input.setFixedHeight(50)
    self.interval_input.setPlaceholderText("Exemplo: 60")
    self.interval_input.setStyleSheet("""
      QLineEdit {
        background-color: white;
        border: 1px solid #D9E8F2;
        border-radius: 12px;
        padding: 0 14px;
        font-size: 16px;
        color: #1F3A5F;
      }

      QLineEdit:focus {
        border: 1px solid #0F8BCB;
      }
    """)

    save_button = QPushButton("Salvar configurações")
    save_button.setFixedHeight(48)
    save_button.clicked.connect(self._on_save_clicked)
    save_button.setStyleSheet(self._primary_button_style())

    test_button = QPushButton("Testar notificação")
    test_button.setFixedHeight(48)
    test_button.clicked.connect(self._on_test_clicked)
    test_button.setStyleSheet(self._secondary_button_style())

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addSpacing(20)
    layout.addWidget(self.enabled_checkbox)
    layout.addWidget(interval_label)
    layout.addWidget(self.interval_input)
    layout.addWidget(save_button)
    layout.addWidget(test_button)
    layout.addStretch()

  def reload_data(self):
    config = self.viewmodel.get_config()

    self.enabled_checkbox.setChecked(config.enabled)
    self.interval_input.setText(str(config.interval_minutes))

  def _on_save_clicked(self):
    try:
      enabled = self.enabled_checkbox.isChecked()
      interval_minutes = int(self.interval_input.text().strip())

      self.viewmodel.update_config(
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
      QMessageBox.warning(
        self,
        "Valor inválido",
        str(error),
      )

  def _on_test_clicked(self):
    self.viewmodel.show_test_notification()

    QMessageBox.information(
      self,
      "Notificação enviada",
      "A notificação foi enviada para o Windows.",
    )

  def _primary_button_style(self) -> str:
    return """
      QPushButton {
        background-color: #0F8BCB;
        color: white;
        border-radius: 12px;
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
        border-radius: 12px;
        font-size: 15px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #EAF6FF;
      }
    """