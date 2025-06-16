""" asyncio
"""
import os
import sys
import json
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
)

import asyncio

# 非同期でデータを取得するコルーチン
async def fetch_data():
    logger.debug(f"データを取得します...")
    # ネットワーク遅延を想定
    await asyncio.sleep(4)
    logger.debug(f"データが取得されました: [data:xyz]")

# 非同期で計算を実行するコルーチン
async def perform_calculation():
    logger.debug("計算を開始します...")
    # 計算の遅延をシミュレート
    await asyncio.sleep(2)
    logger.debug(f"計算が完了しました! 答え[0120-117-117]")

# メインのコルーチン
async def main():
    logger.debug("[main] データ取得と計算を開始する前")
    # fetch_dataとperform_calculationを同時に実行
    await asyncio.gather(fetch_data(), perform_calculation())
    logger.debug("[main] 全てのタスクが完了")


# メインコルーチンを実行
asyncio.run(main())