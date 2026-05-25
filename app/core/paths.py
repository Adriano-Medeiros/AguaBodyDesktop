import os
from pathlib import Path


APP_NAME = "AguaBodyDesktop"


def get_app_data_dir() -> Path:
  local_app_data = os.getenv("LOCALAPPDATA")

  if local_app_data:
    return Path(local_app_data) / APP_NAME

  return Path.home() / APP_NAME


DATA_DIR = get_app_data_dir()
DATABASE_PATH = DATA_DIR / "aguabody.db"


def ensure_data_dir_exists():
  DATA_DIR.mkdir(parents=True, exist_ok=True)