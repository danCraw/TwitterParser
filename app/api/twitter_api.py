import tweepy

from app.core.config import config


def get_twitter_api():
    auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    return tweepy.API(auth)


twitter_api = get_twitter_api()