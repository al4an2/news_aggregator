from fastapi import FastAPI, HTTPException
from .models import Article, NewsResponse
import httpx
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise RuntimeError("NEWS_API_KEY environment variable is not set.")


@app.get("/news", response_model=NewsResponse)
async def get_news(query: str):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail="Error fetching news data")
        data = response.json()
        articles = [Article(
            title=article["title"],
            description=article["description"],
            url=article["url"],
            source=article["source"]["name"]
        ) for article in data["articles"]]
        return NewsResponse(total_results=data["totalResults"], articles=articles)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
