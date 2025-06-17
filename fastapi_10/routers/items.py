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
)

router = APIRouter()

from schemas.item import Item


# ===== 商品 =====

# 商品一覧を取得
@router.get("/items/", response_model=dict)
async def read_items():
    return {
        "message": "商品一覧を表示",
        "items": []
    }

# 新しい商品を追加
@router.post("/items/", response_model=dict)
async def create_item(item: Item):
    return {
        "message": "商品を追加しました",
        "item": item
    }

# 商品を更新
@router.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item: Item):
    return {
        "message": "商品を更新しました",
        "item_id": item_id,
        "item": item
    }

# 商品を削除
@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    return {
        "message": "商品を削除しました",
        "item_id": item_id
    }