from fastapi import APIRouter, BackgroundTasks, Query
from fizzbuzz.service import generate_fizzbuzz

router = APIRouter(prefix="/fizzbuzz", tags=["fizzbuzz"])


@router.get("", status_code=200)
def get_fizzbuzz(
    background_tasks: BackgroundTasks,
    int1: int = Query(..., gt=0),
    int2: int = Query(..., gt=0),
    limit: int = Query(..., gt=0, le=10000),
    str1: str = Query(...),
    str2: str = Query(...),
):
    result = generate_fizzbuzz(int1, int2, limit, str1, str2)
    background_tasks.add_task(persist_stat, int1, int2, limit, str1, str2)
    return {"result": result}


def persist_stat(int1: int, int2: int, limit: int, str1: str, str2: str) -> None:
    pass
