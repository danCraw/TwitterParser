from fastapi import APIRouter

from app.api.routes import users, tweets

api_router = APIRouter()

cities_router = APIRouter()
users_router = APIRouter()
tweets_router = APIRouter()
users_router.include_router(users.router)
users_router.include_router(tweets.router, prefix="/tweets")
