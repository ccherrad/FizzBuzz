from fastapi import FastAPI
import uvicorn

from fizzbuzz.router import router as fizzbuzz_router
from tracker.router import router as stats_router

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(fizzbuzz_router, prefix="/api/v1")
app.include_router(stats_router, prefix="/api/v1")


def main() -> None:
    import os

    dev = os.getenv("ENV") == "dev"
    uvicorn.run(
        "api.main:app" if dev else app,
        host="0.0.0.0",
        port=8000,
        reload=dev,
    )
