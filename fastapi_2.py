""" パスパラメータ
"""
import os
import sys
import json
from typing import Optional

import logging
logging.basicConfig(format="%(asctime)s [%(levelname)s] (Line:%(lineno)d) at %(name)s : %(message)s", datefmt="[%X]")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)

from fastapi import (
    FastAPI,
    HTTPException,
)
app = FastAPI()

# Userクラス
# ユーザのIDと名前を属性として持つ
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

# ダミーデータベース
user_list = [
    User(id=1, name="Tiny"),
    User(id=2, name="Tank"),
    User(id=3, name="Inoue"),
    User(id=4, name="Shinichi"),
]

def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user
    return None





@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    user: Optional[User] = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, 
                            detail="User not found" # Detailは, OpenAPIのエラー時の仕様?
                            )
    return { "user_id": user.id, "username": user.name }

