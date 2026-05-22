from PySide6.QtWidgets import (
  QLabel,
  QLineEdit,
  QMessageBox,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.settings_viewmodel import SettingsViewModel


class GoalsView(QWidget):
  def __init__(self):
    super().__init__()

    self.viewmodel = SettingsViewModel()
    self.goal_input = QLineEdit()

    self._setup_ui()
    self.reload_data()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(18)

    title = QLabel("Metas")
    title.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    subtitle = QLabel("Defina sua meta diária de consumo de água.")
    subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    info = QLabel("A recomendação geral usada no sistema é uma meta personalizada em ml por dia.")
    info.setStyleSheet("""
      font-size: 15px;
      color: #607D9A;
      margin-top: 20px;
    """)

    label = QLabel("Meta diária em ml")
    label.setStyleSheet("""
      font-size: 15px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    self.goal_input.setFixedHeight(50)
    self.goal_input.setPlaceholderText("Exemplo: 2000")
    self.goal_input.setStyleSheet("""
      QLineEdit {
        background-color: white;
        border: 1px solid #D9E8F2;
        border-radius: 12px;
        padding: 0 14px;
        font-size: 18px;
        color: #1F3A5F;
      }

      QLineEdit:focus {
        border: 1px solid #0F8BCB;
      }
    """)

    save_button = QPushButton("Salvar meta")
    save_button.setFixedHeight(48)
    save_button.clicked.connect(self._on_save_clicked)
    save_button.setStyleSheet("""
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
    """)

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addWidget(info)
    layout.addSpacing(20)
    layout.addWidget(label)
    layout.addWidget(self.goal_input)
    layout.addWidget(save_button)
    layout.addStretch()

  def reload_data(self):
    goal_ml = self.viewmodel.get_goal_ml()
    self.goal_input.setText(str(goal_ml))

  def _on_save_clicked(self):
    try:
      goal_ml = int(self.goal_input.text().strip())
      self.viewmodel.update_goal(goal_ml)

      QMessageBox.information(
        self,
        "Meta atualizada",
        "Meta diária atualizada com sucesso.",
      )

    except ValueError as error:
      QMessageBox.warning(
        self,
        "Valor inválido",
        str(error),
      )