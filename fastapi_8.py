""" async FastAPI (httpx)
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

from fastapi import (
    FastAPI,
    HTTPException,
)
app = FastAPI()

import httpx

# 郵便番号APIを利用する関数
# 郵便番号APIのURLを指定
# https://zipcloud.ibsnet.co.jp/api/search?zipcode={番号}
async def fetch_address(zipcode: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
        )
        return response.json()
    
@app.get("/addresses/")
async def get_addresses():
    zip_codes = [
        '0600000', # 北海道
        '1000001', # 東京
        '9000000', # 沖縄
        '8112413',
    ]

    return await asyncio.gather(
        *(fetch_address(zipcode) for zipcode in zip_codes) # アンパック
    )