import os
from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class GlobalConfig(BaseSettings):
    DESCRIPTION = "App description"
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"
    SERVICE_NAME = "AppService"
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "DEV")
    API_V1_STR: str = "/api"

    # Database config
    DATABASE_URL: Optional[PostgresDsn] = os.environ.get(
        "DATABASE_URL", "postgresql://postgresql:postgresql@postgres:5432/twitter_parse"
    )
    DB_MIN_SIZE: int = 2
    DB_MAX_SIZE: int = 15
    DB_FORCE_ROLL_BACK: bool = False

    # app config
    AMOUNT_LAST_TWEETS = 10
    os.environ['https_proxy'] = 'http://uJEM1BHn:HBPjf7Tc@212.193.143.51:48707'

    # assign the values accordingly
    api_key = os.environ.get('api_key', 'J7oizhk4hRPxbCfgxbbrwe7FC')
    api_key_secret = os.environ.get('api_key_secret', 'S8WJtYPW2jwsAXba5NZOHR4s96VfhppD2F0VpuH6VF9SDuwOrS')

    access_token = os.environ.get('access_token', '1511487882145452033-BY2Lf3y4A2EVC40HzFvGstcpbYlRho')

    access_token_secret = os.environ.get('access_token_secret', 'Eta8v5BsuI7npzd9BRJr1yF1FtvFAqFv4TWDORJmcBEpv')

    api_bearer_token = os.environ.get('api_bearer_token', 'AAAAAAAAAAAAAAAAAAAAADFbbgEAAAAAgbDQ72%2BKSSj4LUlfXndxsYyAs1c%3D7rYx14Ozbpzl7dJF4DkCsWxj198YKHM60emOl7bDtZhO24TQ4h')


class DevConfig(GlobalConfig):
    DESCRIPTION = "Dev web description"
    DEBUG = True


class TestConfig(GlobalConfig):
    DESCRIPTION = "Dev web description"
    DEBUG = True
    TESTING = True
    DB_FORCE_ROLL_BACK = True


class FactoryConfig:
    """Returns a config instance depends on the ENV_STATE variable."""

    def __init__(self, environment: Optional[str] = "DEV"):
        self.environment = environment

    def __call__(self):
        if self.environment == "TEST":
            return TestConfig()
        return DevConfig()


def get_configuration():
    return FactoryConfig(GlobalConfig().ENVIRONMENT)()


config = get_configuration()
