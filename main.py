import sys

from PySide6.QtWidgets import QApplication

from app.database.migrations import create_tables
from app.presentation.views.main_window import MainWindow


def main():
  create_tables()

  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  sys.exit(app.exec())


if __name__ == "__main__":
  main()