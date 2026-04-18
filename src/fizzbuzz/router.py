from fastapi import APIRouter, Query

from fizzbuzz.service import generate_fizzbuzz
from tracker.decorator import track_request

router = APIRouter(prefix="/fizzbuzz", tags=["fizzbuzz"])


@router.get("", status_code=200)
@track_request
def get_fizzbuzz(
    int1: int = Query(..., gt=0),
    int2: int = Query(..., gt=0),
    limit: int = Query(..., gt=0, le=10000),
    str1: str = Query(...),
    str2: str = Query(...),
):
    result = generate_fizzbuzz(int1, int2, limit, str1, str2)
    return {"result": result}
