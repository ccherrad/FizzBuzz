import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tracker.database import get_db
from tracker.service import get_most_frequent_request

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/")
def get_stats(db: Session = Depends(get_db)):
    stats = get_most_frequent_request(db)
    if not stats:
        return {}
    return {
        "hits": stats[0].hits,
        "requests": [json.loads(s.params) for s in stats],
    }
