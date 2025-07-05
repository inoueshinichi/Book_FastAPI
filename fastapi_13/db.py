""" DBアクセス
"""
import os
import sys
import json
import asyncio
import time
from datetime import datetime
from typing import Optional

import logging
logging.basicConfig(format="%(asctime)s [%(levelname)s] (Thread:%(thread)d):(Line:%(lineno)d) at %(name)s : %(message)s", datefmt="[%X]")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

# =====================
# DBアクセス
# =====================

# ベースクラスの定義
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)

# DBのURL
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'memodb.sqlite')

# 非同期エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True) # echo=Trueは, 実行されるSQL文をターミナルに出力する

# 非同期セッションの設定
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False, # セッションをコミットした後でも、DBから取得したオブジェクトが無効にならずに使い続けられる設定.
    class_=AsyncSession,
)

# DBとのセッションを非同期的に扱うことができる関数
async def get_dbsession():
    async with async_session() as session:
        yield session
