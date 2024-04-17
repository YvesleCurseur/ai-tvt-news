from fastapi import FastAPI, status as STATUS, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, time, timedelta
from typing import Optional, List
from database import SessionLocal
import models
import asyncio
from utils import get_last_video_and_transcript

app = FastAPI(
    title="TVTNews FastAPI",
    description="API for TVTNews App to get news from youtube videos transcripts",
    version="0.0.1",
    contact={
        "name": "Fulbert Pognon",
        "email": "pognonyvesfulbert@gmail.com",
    },
)


# Rename Fast API docs


origins = ["http://localhost:3000", "localhost:3000", "https://tvt-news.onrender.com", "https://daily-news-tvt.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class News(BaseModel):
    id: int
    title: str
    video_id: str
    transcript: str
    description: str
    published_at: datetime
    created_at: datetime
    updated_at: datetime


class NewsCreate(BaseModel):
    title: str
    video_id: str
    transcript: str
    description: str
    published_at: datetime


db = SessionLocal()


@app.get("/news", response_model=List[News], status_code=STATUS.HTTP_200_OK)
async def get_news():
    news = db.query(models.News).order_by(models.News.created_at.desc()).all()
    return news


@app.get("/news/{news_id}", response_model=News, status_code=STATUS.HTTP_200_OK)
async def get_news(news_id: int):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if news is None:
        raise HTTPException(
            status_code=STATUS.HTTP_404_NOT_FOUND, detail="Resource Not Found"
        )
    return news

# The others endpoints were to know how done the CRUD operations with FastAPI
@app.post("/news", response_model=News, status_code=STATUS.HTTP_201_CREATED)
async def create_an_news(news: NewsCreate):
    new_news = models.News(
        title=news.title,
        video_id=news.video_id,
        transcript=news.transcript,
        description=news.description,
        published_at=news.published_at,
    )
    db.add(new_news)
    db.commit()
    return new_news


@app.put("/news/{news_id}", response_model=News, status_code=STATUS.HTTP_200_OK)
async def update_an_news(news_id: int, news: News):
    news_to_update = db.query(models.News).filter(models.News.id == news_id).first()
    if news_to_update is None:
        raise HTTPException(
            status_code=STATUS.HTTP_404_NOT_FOUND, detail="Resource Not Found"
        )
    news_to_update.title = news.title
    news_to_update.video_id = news.video_id
    news_to_update.transcript = news.transcript
    news_to_update.description = news.description
    news_to_update.published_at = news.published_at
    db.commit()
    return news_to_update


@app.delete("/news/{news_id}")
async def delete_item(news_id: int):
    news_to_delete = db.query(models.News).filter(models.News.id == news_id).first()
    if news_to_delete is None:
        raise HTTPException(
            status_code=STATUS.HTTP_404_NOT_FOUND, detail="Resource Not Found"
        )
    db.delete(news_to_delete)
    db.commit()
    return news_to_delete

@app.on_event("startup")
async def startup_event():

    async def task1():
        while True:
            await get_last_video_and_transcript()
            # Each 2 mins here but on prod i set it to 24 hours
            await asyncio.sleep(120)

    async def main():
        await asyncio.gather(task1())

    asyncio.create_task(main())






