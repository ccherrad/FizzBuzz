from sqlalchemy import func
from sqlalchemy.orm import Session

from tracker.database import RequestStat


def get_most_frequent_request(db: Session):
    max_hits = db.query(func.max(RequestStat.hits)).scalar()
    if max_hits is None:
        return []
    return db.query(RequestStat).filter(RequestStat.hits == max_hits).all()
