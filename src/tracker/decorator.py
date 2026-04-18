import inspect
import json
from functools import wraps

import tracker.database as tracker_db
from sqlalchemy.orm import Session


def track_request(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        params = json.dumps(bound.arguments, sort_keys=True)

        db: Session = tracker_db.SessionLocal()
        try:
            existing = db.query(tracker_db.RequestStat).filter_by(params=params).first()
            if existing:
                existing.hits += 1
            else:
                db.add(tracker_db.RequestStat(params=params))
            db.commit()
        finally:
            db.close()

        return fn(*args, **kwargs)

    return wrapper
