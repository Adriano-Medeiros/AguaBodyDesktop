from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
  QHBoxLayout,
  QInputDialog,
  QLabel,
  QListWidget,
  QListWidgetItem,
  QMessageBox,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.history_viewmodel import HistoryViewModel


class HistoryView(QWidget):
  def __init__(self):
    super().__init__()

    self.viewmodel = HistoryViewModel()
    self.list_widget = QListWidget()

    self._setup_ui()
    self._load_data()

  def _setup_ui(self):
    layout = QVBoxLayout(self)
    layout.setContentsMargins(34, 30, 34, 30)
    layout.setSpacing(20)

    title = QLabel("Histórico de consumo")
    title.setStyleSheet("""
      font-size: 30px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    subtitle = QLabel("Resumo diário e registros individuais de hidratação.")
    subtitle.setStyleSheet("""
      font-size: 16px;
      color: #607D9A;
    """)

    actions_layout = QHBoxLayout()
    actions_layout.setSpacing(12)

    edit_button = QPushButton("Editar registro selecionado")
    edit_button.setFixedHeight(44)
    edit_button.clicked.connect(self._on_edit_selected)
    edit_button.setStyleSheet(self._primary_button_style())

    delete_button = QPushButton("Excluir registro selecionado")
    delete_button.setFixedHeight(44)
    delete_button.clicked.connect(self._on_delete_selected)
    delete_button.setStyleSheet(self._danger_button_style())

    actions_layout.addWidget(edit_button)
    actions_layout.addWidget(delete_button)

    self.list_widget.setStyleSheet("""
      QListWidget {
        background-color: white;
        border-radius: 18px;
        border: none;
        padding: 12px;
      }

      QListWidget::item {
        padding: 12px;
        border-bottom: 1px solid #E5EEF5;
        font-size: 15px;
        color: #1F3A5F;
      }

      QListWidget::item:selected {
        background-color: #D4ECFF;
        color: #1F3A5F;
      }
    """)

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addLayout(actions_layout)
    layout.addWidget(self.list_widget)

  def _load_data(self):
    self.list_widget.clear()

    grouped_items = self.viewmodel.get_grouped_by_day()

    if not grouped_items:
      empty_item = QListWidgetItem("Nenhum registro encontrado.")
      empty_item.setFlags(Qt.NoItemFlags)
      self.list_widget.addItem(empty_item)
      return

    for group in grouped_items:
      date_text = group["date"].strftime("%d/%m/%Y")
      total_ml = group["total_ml"]

      header_item = QListWidgetItem(
        f"📅 {date_text}  —  Total: {total_ml} ml"
      )
      header_item.setFlags(Qt.NoItemFlags)

      font = header_item.font()
      font.setBold(True)
      header_item.setFont(font)

      self.list_widget.addItem(header_item)

      for item in group["items"]:
        time_text = item.created_at.strftime("%H:%M")

        detail_item = QListWidgetItem(
          f"   💧 {time_text}  •  {item.amount_ml} ml"
        )

        detail_item.setData(Qt.UserRole, item.id)
        detail_item.setData(Qt.UserRole + 1, item.amount_ml)

        self.list_widget.addItem(detail_item)

  def _on_edit_selected(self):
    selected_item = self.list_widget.currentItem()

    if selected_item is None:
      self._show_warning("Selecione um registro para editar.")
      return

    water_intake_id = selected_item.data(Qt.UserRole)
    current_amount = selected_item.data(Qt.UserRole + 1)

    if water_intake_id is None:
      self._show_warning("Selecione um registro individual, não o cabeçalho do dia.")
      return

    new_amount, ok = QInputDialog.getInt(
      self,
      "Editar registro",
      "Informe a nova quantidade em ml:",
      int(current_amount),
      1,
      5000,
      50,
    )

    if not ok:
      return

    try:
      updated = self.viewmodel.update_amount(
        water_intake_id=int(water_intake_id),
        amount_ml=new_amount,
      )

      if updated:
        self._load_data()

    except ValueError as error:
      self._show_warning(str(error))

  def _on_delete_selected(self):
    selected_item = self.list_widget.currentItem()

    if selected_item is None:
      self._show_warning("Selecione um registro para excluir.")
      return

    water_intake_id = selected_item.data(Qt.UserRole)

    if water_intake_id is None:
      self._show_warning("Selecione um registro individual, não o cabeçalho do dia.")
      return

    reply = QMessageBox.question(
      self,
      "Excluir registro",
      "Deseja realmente excluir este registro?",
      QMessageBox.Yes | QMessageBox.No,
    )

    if reply != QMessageBox.Yes:
      return

    deleted = self.viewmodel.delete_by_id(
      water_intake_id=int(water_intake_id)
    )

    if deleted:
      self._load_data()

  def _show_warning(self, message: str):
    QMessageBox.warning(
      self,
      "Atenção",
      message,
    )

  def _primary_button_style(self) -> str:
    return """
      QPushButton {
        background-color: #0F8BCB;
        color: white;
        border-radius: 12px;
        font-size: 15px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #0A6FA3;
      }
    """

  def _danger_button_style(self) -> str:
    return """
      QPushButton {
        background-color: #FFEAEA;
        color: #D64545;
        border: 1px solid #F3C1C1;
        border-radius: 12px;
        font-size: 15px;
        font-weight: bold;
      }

      QPushButton:hover {
        background-color: #FFDADA;
      }
    """