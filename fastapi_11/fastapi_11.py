""" SQLAlchemy & SQLite
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

import httpx

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    select,
)

from fastapi import (
    FastAPI,
    HTTPException,
    APIRouter,
)
# app = FastAPI()

'''DB/ORM'''

# ベースクラスの定義
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)

# DBのURL
DATABASE_URL = "sqlite+aiosqlite:///" + os.path.join(base_dir, "example.sqlite")

# 非同期エンジンの作成
async_engine = create_async_engine(DATABASE_URL, echo=True)

# 非同期セッションの設定
async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# DBモデル(テーブル)定義
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

# DB初期化
async def init_db():
    logger.debug("SQLite DB の初期化を行います")
    async with async_engine.begin() as connection:
        # 既存のテーブルを削除
        await connection.run_sync(Base.metadata.drop_all)
        logger.debug("既存テーブルを削除しました")
        # テーブル作成
        await connection.run_sync(Base.metadata.create_all)
        logger.debug("新規テーブルを作成しました")


# ユーザー追加関数
async def add_user(name: str):
    logger.debug(f"{name} をDB(SQLite)に追加します")
    async with async_session() as session:
        # このブロック内で行われる変更は1つのトランザクションとして扱われる
        async with session.begin():
            user = User(name=name)
            session.add(user)
            logger.debug(f"{name} をDB(SQLite)に追加しました")


# ユーザー取得関数
async def get_users():
    logger.debug("DB(SQLite)からユーザ一覧を取得します")
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        logger.debug("ユーザーの取得が完了しました")
        return users
    
# メイン関数
async def main():
    await init_db()
    await add_user("TinyTank")
    await add_user("InoueShinichi")
    users = await get_users()
    for user in users:
        print(f"{user.id}: {user.name}")


if __name__ == "__main__":
    asyncio.run(main())