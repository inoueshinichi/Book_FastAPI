""" DI(依存性注入：Dependency Injection)
"""
import os
import sys
import json
import asyncio
import time
from datetime import datetime
from typing import Optional
from pydantic import (
    BaseModel,
    ValidationError,
    Field,
)

import logging

logging.basicConfig(format="%(asctime)s [%(levelname)s] (Thread:%(thread)d):(Line:%(lineno)d) at %(name)s : %(message)s", datefmt="[%X]")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)

from fastapi import (
    FastAPI,
    HTTPException,
    APIRouter,
    Depends,
)
app = FastAPI()

import httpx

# Userクラス
# ユーザのIDと名前を属性として持つ
class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

# ダミーデータベース
users = [
    User(id=1, name="Tiny", is_active=True),
    User(id=2, name="Tank", is_active=False),
    User(id=3, name="Inoue", is_active=True),
    User(id=4, name="Shinichi", is_active=False),
]

# アクティブなユーザーをフィルタリングする依存関係
def get_active_users():
    active_users = [user for user in users if user.is_active]
    print("===== アクティブなユーザーを取得 =====")
    return active_users

@app.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
    print("=== 【依存】してデータを取得 ===")
    return active_users

