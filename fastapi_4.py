""" Pydanticの利用によるデータの型チェック
"""
import os
import sys
import json
from typing import Optional
from datetime import datetime
from pydantic import (
    BaseModel,
    ValidationError,
)

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


class Event(BaseModel):
    # クラス変数
    name: str = "未定"
    start_datetime: datetime
    participants: list[str] = []


# ダミーデータ(外部からのイベントデータ想定)
external_data = {
    "name": "FastAPI勉強会",
    "start_datetime": "2025-06-17",
    "participants": ["Tiny", "Tank", "Inoue", "Shinichi"],
}

# 辞書のアンパック
event = Event(**external_data)
logger.debug(f"イベント名: {event.name}, {type(event.name)}")
logger.debug(f"開催日時: {event.start_datetime}, {type(event.start_datetime)}")
logger.debug(f"参加者: {event.participants}, {type(event.participants)}")


error_external_data = {
    "name": "FastAPI勉強会",
    "start_datetime": "abc",
    "participants": ["Tiny", "Tank", "Inoue", "Shinichi"],
}

try:
    event = Event(**error_external_data)
    logger.debug(f"イベント名: {event.name}, {type(event.name)}")
    logger.debug(f"開催日時: {event.start_datetime}, {type(event.start_datetime)}")
    logger.debug(f"参加者: {event.participants}, {type(event.participants)}")

except ValidationError as e:
    logger.error(f"データのバリデーションエラーが発生しました。: {e.errors()}")