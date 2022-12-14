import tweepy

from app.core.config import config


def get_twitter_api():
    auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    return tweepy.API(auth)


def get_twitter_client():
    return tweepy.Client(bearer_token=config.api_bearer_token, wait_on_rate_limit=True)


client = get_twitter_client()

twitter_api = get_twitter_api()
