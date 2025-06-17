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

from schemas.category import Category


# ===== カテゴリ =====

# カテゴリ一覧を取得
@router.get("/categories/", response_model=dict)
async def read_categories():
    # 実際にはDBから取得する処理が入る
    return {"message": "カテゴリ一覧を表示", "categories": []}

# 新しいカテゴリを作成
@router.post("/categories/", response_model=dict)
async def create_category(category: Category):
    # 実際にはDBに保存する処理が入る
    return {"message": "カテゴリを作成しました", "category": category}

# カテゴリを更新
@router.put("/categories/{category_id}", response_model=dict)
async def update_category(category_id: int, category: Category):
    # 実際にはDBを更新する処理が入る
    return {
        "message": "カテゴリを更新しました", 
        "category_id": category_id,
        "category": category,
    }

# カテゴリを削除
@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    # 実際にはDBから削除する処理が入る
    return {
        "message": "カテゴリを削除しました",
        "category_id": category_id
    }

