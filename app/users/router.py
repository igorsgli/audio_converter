import uuid

from datetime import datetime
from fastapi import APIRouter
from app.exceptions import UserNotFoundException

from app.users.schemas import SUser, SUserInfo, SUserInfoAll
from app.users.dao import UserDAO

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.post('/')
async def create_user(user: SUser) -> SUserInfo:
    data = {
        'username': user.username,
        'access_token': str(uuid.uuid4()),
        'created_at': datetime.now()
    }
    new_user = await UserDAO.add(**data)
    result = {
        'id': new_user.id,
        'access_token': new_user.access_token
    }
    return result


@router.get('/me')
async def get_user(user_id: uuid.UUID) -> SUserInfoAll:
    user = await UserDAO.find_one_or_none(id=user_id)
    if user is None:
        raise UserNotFoundException
    return user


# @router.get('/get_all')
# async def get_users():
#     return await UserDAO.find_all()
