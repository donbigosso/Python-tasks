from fastapi import FastAPI

from API import get_statistics

app = FastAPI()


@app.get("/stats")
async def stats(url: str):
    statistics = get_statistics(url)
    return statistics
