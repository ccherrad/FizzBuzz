from fastapi import FastAPI
import uvicorn

from fizzbuzz.routers import fizzbuzz, stats

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(fizzbuzz.router, prefix="/api/v1")
app.include_router(stats.router, prefix="/api/v1")


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
