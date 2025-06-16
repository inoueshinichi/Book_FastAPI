""" 同期処理と非同期処理
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

''' 同期関数
'''
def sync_task(name: str):
    print(f"{name} タスク開始")
    time.sleep(2)
    print(f"{name} タスク終了")

def run_sync_tasks():
    sync_task("タスク1")
    sync_task("タスク2")
    sync_task("タスク3")

print("同期処理の例：")
run_sync_tasks()


''' 非同期関数
'''
import asyncio

async def async_task(name: str):
    print(f"{name} タスク開始")
    await asyncio.sleep(2)
    print(f"{name} タスク終了")

async def run_async_tasks():
    await asyncio.gather(
        async_task("タスク1(async)"),
        async_task("タスク2(async)"),
        async_task("タスク3(async)"),
    )

print("¥n非同期処理の例：")
asyncio.run(run_async_tasks())