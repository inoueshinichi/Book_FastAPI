""" APIサーバー
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

import httpx
from pydantic import (
    BaseModel,
    ValidationError,
    Field,
)
from fastapi import (
    FastAPI,
    HTTPException,
    APIRouter,
)
from fastapi.responses import (
    Response,
    FileResponse,
    JSONResponse,
    RedirectResponse,
    PlainTextResponse,
    StreamingResponse,
)


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


'''DB/ORM'''
# ベースクラスの定義
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)


'''Schema'''
from schemas.memo import (
    InsertAndUpdateMemoSchema,
    MemoSchema,
    ResponseSchema,
)


'''EntryPoint'''
app = FastAPI()

# メモ新規登録
# @app.post("/memos", response_model=ResponseSchema)
# async def create_memo(memo: InsertAndUpdateMemoSchema):
#     logger.debug(memo)
#     return ResponseSchema(message="メモが正常に登録されました")


# メモ情報全件取得
# @app.get("/memos", response_model=list[MemoSchema])
# async def get_memos_list():
#     return [
#         MemoSchema(title="タイトル1", description="詳細1", memo_id=1),
#         MemoSchema(title="タイトル2", description="詳細2", memo_id=2),
#         MemoSchema(title="タイトル3", description="詳細3", memo_id=3),
#     ]


# 特定のメモ情報取得
# @app.get('/memos/{memo_id}', response_model=MemoSchema)
# async def get_memo_detail(memo_id: int):
#     return MemoSchema(title=f"タイトル{memo_id}", description=f"詳細{memo_id}", memo_id=memo_id)


# 特定のメモを更新する
# @app.put("/memos/{memo_id}", response_model=ResponseSchema)
# async def get_memo_detail(memo_id: int, memo: InsertAndUpdateMemoSchema):
#     logger.debug(f"{memo_id}: {memo}")
#     return ResponseSchema(message="メモが正常に更新されました")


# 特定のメモを削除する
# @app.delete("/memos/{memo_id}", response_model=ResponseSchema)
# async def remove_memo(memo_id: int):
#     logger.deug(f"{memo_id}")
#     return ResponseSchema(message="メモが正常に削除されました")



# バリデーションエラーのカスタムハンドラ
@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    # ValidationErrorが発生した場合にクライアントに返すレスポンス定義
    return JSONResponse(status_code=422, content={
        "detail": exec.errors(), # Pydanticが提供するエラーリスト
        "body": exec.model, # エラー発生時の入力データ
    })