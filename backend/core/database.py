import sqlalchemy
import traceback
from settings import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm


DB_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = sqlalchemy.create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = orm.sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
    finally:
        db.close()
