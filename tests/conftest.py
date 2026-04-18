import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import tracker.database as tracker_db


@pytest.fixture(autouse=True)
def use_test_db(tmp_path, monkeypatch):
    engine = create_engine(
        f"sqlite:///{tmp_path}/test.db", connect_args={"check_same_thread": False}
    )
    tracker_db.Base.metadata.create_all(bind=engine)
    TestSession = sessionmaker(bind=engine)
    monkeypatch.setattr(tracker_db, "SessionLocal", TestSession)
    monkeypatch.setattr(tracker_db, "engine", engine)
