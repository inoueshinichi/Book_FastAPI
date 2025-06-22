""" DBテーブルファイルの作成
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
    AsyncSession
)

# =====================
# DB作成&テーブル作成
# =====================

# ベースクラスの定義
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)

# DBのURL
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'memodb.sqlite')

# 非同期エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True) # echo=Trueは, 実行されるSQL文をターミナルに出力する

# DB初期化
async def init_db():
    logger.info("=== DB初期化を開始 ===")
    async with engine.begin() as conn:
        # 既存のテーブルを削除
        await conn.run_sync(Base.metadata.drop_all)
        logger.info(">>> 既存のテーブルを削除しました")
        # テーブルを作成
        await conn.run_sync(Base.metadata.create_all)
        logger.info(">>> 新しいテーブルを作成しました")


if __name__ == '__main__':
    asyncio.run(init_db())
