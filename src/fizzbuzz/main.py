from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)
