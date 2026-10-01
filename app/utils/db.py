from sqlalchemy import create_engine
from app.config import settings
from sqlalchemy.orm import sessionmaker
from app.models.model import Base


engine = create_engine(settings.db_url)
Base.metadata.create_all(engine)

with engine.connect() as connection:
    print("Database Connected Successfully 🚀")


LocalSession = sessionmaker(bind=engine)

def get_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

