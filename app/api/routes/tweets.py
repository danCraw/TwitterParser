from fastapi import APIRouter

from app.api.twitter_api import client
from app.core.config import config
router = APIRouter()


@router.get("/{twitter_id}")
async def user_tweets(twitter_id: int):
    tweets = client.get_users_tweets(id=twitter_id, max_results=config.AMOUNT_LAST_TWEETS)[0]

    tweets_json = []
    for tweet in tweets:
        tweets_json.append(tweet.text)
    return tweets_json
