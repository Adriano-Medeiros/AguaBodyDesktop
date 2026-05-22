from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QCloseEvent, QIcon
from PySide6.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QMenu,
  QStackedWidget,
  QSystemTrayIcon,
  QVBoxLayout,
  QWidget,
)

from app.presentation.viewmodels.reminder_viewmodel import ReminderViewModel
from app.presentation.views.dashboard_view import DashboardView
from app.presentation.views.goals_view import GoalsView
from app.presentation.views.history_view import HistoryView
from app.presentation.views.reminders_view import RemindersView
from app.presentation.views.settings_view import SettingsView
from app.presentation.views.statistics_view import StatisticsView
from app.presentation.widgets.sidebar import Sidebar
from app.theme.styles import APP_STYLE
from app.utils.resource_path import resource_path

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("AguaBody Desktop")
    self.setMinimumSize(1100, 760)
    self.setStyleSheet(APP_STYLE)

    self.reminder_viewmodel = ReminderViewModel(self.show_main_window)

    self.reminder_timer = QTimer(self)
    self.reminder_timer.timeout.connect(self._show_automatic_reminder)

    self.stack = QStackedWidget()

    self.dashboard_view = DashboardView()
    self.history_view = HistoryView()
    self.statistics_view = StatisticsView()
    self.goals_view = GoalsView()
    self.reminders_view = RemindersView()
    self.settings_view = SettingsView()
    self.about_view = self._create_about_view()

    self._setup_ui()
    self._setup_tray_icon()
    self._restart_reminder_timer()
  
  def show_main_window(self):
    self.show()
    self.showNormal()
    self.raise_()
    self.activateWindow()

    self._navigate("dashboard")
    
  def _setup_ui(self):
    central_widget = QWidget()

    main_layout = QHBoxLayout(central_widget)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    sidebar = Sidebar()
    self.sidebar = sidebar
    sidebar.navigate.connect(self._navigate)

    self.settings_view.reminder_config_updated.connect(
      self._restart_reminder_timer
    )

    self.reminders_view.reminder_config_updated.connect(
      self._restart_reminder_timer
    )

    self.settings_view.quick_buttons_updated.connect(
      self.dashboard_view.reload_quick_buttons
    )

    self.stack.addWidget(self.dashboard_view)
    self.stack.addWidget(self.history_view)
    self.stack.addWidget(self.statistics_view)
    self.stack.addWidget(self.goals_view)
    self.stack.addWidget(self.reminders_view)
    self.stack.addWidget(self.settings_view)
    self.stack.addWidget(self.about_view)

    main_layout.addWidget(sidebar)
    main_layout.addWidget(self.stack, 1)

    self.setCentralWidget(central_widget)

  def _setup_tray_icon(self):
    icon = QIcon(resource_path("app/assets/icons/water.ico"))

    self.tray_icon = QSystemTrayIcon(self)
    self.tray_icon.setIcon(icon)

    tray_menu = QMenu()

    open_action = QAction("Abrir AguaBody", self)
    open_action.triggered.connect(self._restore_window)

    exit_action = QAction("Sair", self)
    exit_action.triggered.connect(self._exit_application)

    tray_menu.addAction(open_action)
    tray_menu.addSeparator()
    tray_menu.addAction(exit_action)

    self.tray_icon.setContextMenu(tray_menu)
    self.tray_icon.activated.connect(self._on_tray_icon_activated)
    self.tray_icon.show()

    self.setWindowIcon(icon)

  def _navigate(self, page: str):
    if hasattr(self, "sidebar"):
      self.sidebar.set_active(page)

    if page == "dashboard":
      self.dashboard_view.reload_quick_buttons()
      self.dashboard_view._update_cards()
      self.stack.setCurrentWidget(self.dashboard_view)

    elif page == "history":
      self.history_view._load_data()
      self.stack.setCurrentWidget(self.history_view)

    elif page == "statistics":
      self.statistics_view.reload_data()
      self.stack.setCurrentWidget(self.statistics_view)

    elif page == "goals":
      self.goals_view.reload_data()
      self.stack.setCurrentWidget(self.goals_view)

    elif page == "reminders":
      self.reminders_view.reload_data()
      self.stack.setCurrentWidget(self.reminders_view)

    elif page == "settings":
      self.stack.setCurrentWidget(self.settings_view)

    elif page == "about":
      self.stack.setCurrentWidget(self.about_view)

  def _restart_reminder_timer(self):
    self.reminder_timer.stop()

    config = self.reminder_viewmodel.get_config()

    if not config.enabled:
      return

    interval_ms = config.interval_minutes * 60 * 1000
    self.reminder_timer.start(interval_ms)

  def _show_automatic_reminder(self):
    config = self.reminder_viewmodel.get_config()

    if config.enabled:
      self.reminder_viewmodel.show_reminder()
      self.show_main_window()

  def _restore_window(self):
    self.showNormal()
    self.activateWindow()

  def _exit_application(self):
    self.tray_icon.hide()
    QApplication.quit()

  def _on_tray_icon_activated(self, reason):
    if reason == QSystemTrayIcon.Trigger:
      self._restore_window()

  def changeEvent(self, event):
    if self.isMinimized():
      self.hide()

      self.tray_icon.showMessage(
        "AguaBody",
        "O aplicativo continua executando em segundo plano.",
        QSystemTrayIcon.Information,
        3000,
      )

    super().changeEvent(event)

  def closeEvent(self, event: QCloseEvent):
    event.ignore()

    self.hide()

    self.tray_icon.showMessage(
      "AguaBody",
      "O aplicativo continua executando na bandeja do sistema.",
      QSystemTrayIcon.Information,
      3000,
    )

  def _create_about_view(self) -> QWidget:
    widget = QWidget()

    layout = QVBoxLayout(widget)
    layout.setContentsMargins(30, 30, 30, 30)
    layout.setSpacing(14)

    title = QLabel("Sobre o AguaBody")
    title.setStyleSheet("""
      font-size: 28px;
      font-weight: bold;
      color: #1F3A5F;
    """)

    description = QLabel("""
      <b style="color:#1F3A5F; font-size:18px;">
      AguaBody Desktop
      </b><br><br>

      Aplicativo inteligente desenvolvido para auxiliar no controle diário da hidratação, promovendo saúde, bem-estar e qualidade de vida através de uma experiência moderna, intuitiva e eficiente.<br><br>

      O sistema permite acompanhar o consumo diário de água, definir metas personalizadas, receber lembretes automáticos, visualizar estatísticas de consumo e manter uma rotina de hidratação organizada e saudável.<br><br>

      Desenvolvido com foco em desempenho, praticidade e design moderno, utilizando arquitetura profissional MVVM, interface desktop moderna com PySide6 e banco de dados SQLite local.<br><br>

      <b style="color:#1F3A5F;">Recursos principais</b><br>
      • Controle diário de consumo de água<br>
      • Metas personalizadas de hidratação<br>
      • Lembretes automáticos inteligentes<br>
      • Histórico completo de consumo<br>
      • Estatísticas e gráficos de desempenho<br>
      • Funcionamento offline<br>
      • Interface moderna e intuitiva<br><br>
      
      Projeto AguaBody Desktop<br>
      <br>
      <b style="color:#1F3A5F;">Desenvolvido por Adriano Medeiros Alves da Silva</b><br>
      <b style="color:#1F3A5F;">Contato: adrianomedeiros616@gmail.com</b><br>
      
      """)
  
    description.setWordWrap(True)

    description.setStyleSheet("""
      font-size: 15px;
      color: #607D9A;
      line-height: 1.6;
    """)

    version = QLabel("Versão 1.0.0")
    version.setStyleSheet("""
      font-size: 14px;
      color: #607D9A;
    """)

    layout.addWidget(title)
    layout.addWidget(description)
    
    layout.addWidget(version)
    layout.addStretch()

    return widget
  
  def show_main_window(self):
    self.show()

    if self.isMinimized():
      self.showNormal()

    self.raise_()
    self.activateWindow()

    self._navigate("dashboard")
    

    