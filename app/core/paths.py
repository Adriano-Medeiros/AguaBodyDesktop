from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "aguabody.db"


def ensure_data_dir_exists():
  DATA_DIR.mkdir(parents=True, exist_ok=True)