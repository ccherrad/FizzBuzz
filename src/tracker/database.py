from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./data/fizzbuzz_stats.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

with engine.connect() as connection:
    connection.exec_driver_sql("PRAGMA journal_mode=WAL;")
    connection.exec_driver_sql("PRAGMA synchronous=NORMAL;")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class RequestStat(Base):
    __tablename__ = "request_stats"

    id = Column(Integer, primary_key=True, index=True)
    params = Column(String, nullable=False, unique=True)
    hits = Column(Integer, default=1, index=True)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
