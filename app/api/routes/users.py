import re
from typing import Dict
from fastapi import APIRouter, HTTPException

from app.api.twitter_api import twitter_api
from app.db.repositories.status import StatusRepository
from app.models.status import StatusIn
from app.models.user import UserOut

router = APIRouter()


@router.post("/users")
async def parse_users(links: str) -> Dict:
    status_repo: StatusRepository = StatusRepository()
    links = re.sub('\s+', '', links)
    usernames = links.split('https://twitter.com/')
    accounts_list = []
    for username in usernames:
        if username:
            try:
                print(username)
                await find_user_account(username)
                status = 'success'
            except Exception as e:
                status = 'failed'
            accounts_list.append({'username': username, 'status': status})
    return {'id': await status_repo.create(StatusIn(accounts=accounts_list))}


@router.get("/users/status/{id}")
async def users_status(id: int) -> int:
    status_repo: StatusRepository = StatusRepository()
    status = await status_repo.get(id)
    if status:
        return status
    else:
        raise HTTPException(status_code=404, detail="status with the given Id not found")


@router.get("/user/{username}")
async def find_user_account(username: str) -> UserOut:
    user = twitter_api.get_user(screen_name=username)
    return UserOut(twitter_id=user.id, name=user.name, username=username, following_count=user.friends_count,
                   followers_count=user.followers_count, description=user.description)
