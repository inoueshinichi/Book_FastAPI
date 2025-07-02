""" memo Router
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

from datetime import datetime

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
)

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from schemas.memo import (
    InsertAndUpdateMemoSchema,
    MemoSchema,
    ResponseSchema,
)

import cruds.memo as memo_crud
import db


# ルーターを作成し、タグとURLパスのプレフィックスを設定
router = APIRouter(tags=["Memos"], prefix="/memos")

# =================================================
# メモ用のエンドポイント
# =================================================
