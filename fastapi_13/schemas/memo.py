""" スキーマ
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
    Depends,
)
# app = FastAPI()


"""スキーマ定義"""
# 登録・更新で使用するスキーマ
class InsertAndUpdateMemoSchema(BaseModel):
    # このフィールドは必須
    title: str = Field(...,
                       description="メモのタイトルを入力してください。少なくとも1文字以上必要です。",
                       example="明日のアジェンダ", min_length=1)

    # このフィールドは任意
    description: str = Field(default="",
                             description="メモの内容についての追加情報。任意で記入できます。",
                             example="会議で話すトピック：プロジェクトの進捗状況")


# メモ情報を表すスキーマ
class MemoSchema(InsertAndUpdateMemoSchema):
    # DBで主キーとなる
    memo_id: int = Field(...,
                         description="メモを一位に識別するID番号。DBで自動的に割り当てられます。",
                         example=123)


# レスポンスで使用する結果用スキーマ
class ResponseSchema(BaseModel):
    # このフィールドは必須
    message: str = Field(...,
                         description="API操作の結果を説明するメッセージ。",
                         example="メモの更新に成功しました。")
    

