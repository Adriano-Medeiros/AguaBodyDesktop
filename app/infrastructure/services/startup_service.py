import os
import sys
from pathlib import Path


APP_NAME = "AguaBodyDesktop"


class StartupService:
  @staticmethod
  def get_startup_folder() -> Path:
    return Path(
      os.getenv("APPDATA")
    ) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

  @staticmethod
  def get_shortcut_path() -> Path:
    return StartupService.get_startup_folder() / f"{APP_NAME}.bat"

  @staticmethod
  def is_enabled() -> bool:
    return StartupService.get_shortcut_path().exists()

  @staticmethod
  def enable():
    startup_file = StartupService.get_shortcut_path()

    executable_path = sys.executable

    content = f'''@echo off
start "" "{executable_path}"
'''

    startup_file.write_text(content, encoding="utf-8")

  @staticmethod
  def disable():
    startup_file = StartupService.get_shortcut_path()

    if startup_file.exists():
      startup_file.unlink()