from fastapi import APIRouter

from app.api import twitter_api
from app.core.config import config
router = APIRouter()


@router.get("/{twitter_id}")
async def user_tweets(twitter_id: int):
    tweets = twitter_api.user_timeline(user_id=twitter_id, count=config.AMOUNT_LAST_TWEETS)
    tweets_json = []
    for tweet in tweets:
        tweets_json.append(tweet.text)
    return tweets_json
