from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.paths import DATABASE_PATH, ensure_data_dir_exists


ensure_data_dir_exists()

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
  DATABASE_URL,
  echo=False,
  future=True,
)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False,
  autocommit=False,
  future=True,
)

Base = declarative_base()