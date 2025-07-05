""" memo CRUD
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

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


import schemas.memo as memo_schema
import models.memo as memo_model

# =====================
# 非同期CRUD処理
# =====================

# 新規登録
async def insert_memo(
        db_session: AsyncSession,
        memo_data: memo_schema.InsertAndUpdateMemoSchema
) -> memo_model.Memo:
    """
        新しいメモをDBに登録する関数
    Args:
        db_session (AsyncSession): 非同期DBセッション
        memo_data (memo_schema.InsertAndUpdateMemoSchema): 作成するメモのデータ

    Returns:
        memo_model.Memo: 作成したメモのモデル
    """

    logger.info("=== 新規登録：開始 ===")
    new_memo = memo_model.Memo(**memo_data.model_dump())
    db_session.add(new_memo)
    await db_session.commit()
    await db_session.refresh(new_memo)
    logger.info(">>> データ追加完了")
    return new_memo


# 全件取得
async def get_memos(db_session: AsyncSession) -> list[memo_model.Memo]:

    logger.info("=== 全件取得：開始 ===")
    result = await db_session.execute(select(memo_model.Memo))
    memos = result.scalars().all()
    logger.info(">>> データ全件取得完了")
    return memos


# 1件取得
async def get_memo_by_id(db_session: AsyncSession,
                         memo_id: int) -> memo_model.Memo | None:
    
    logger.info("=== 1件取得 ===")
    result = await db_session.execute(
        select(memo_model.Memo).where(memo_model.memo_id == memo_id)
    )
    memo = result.scalars().first() # リストの最初
    logger.info(">>> データ取得完了")
    return memo


# 更新処理
async def update_memo(
    db_session: AsyncSession,
    memo_id: int,
    target_data: memo_schema.InsertAndUpdateMemoSchema   
) -> memo_model.Memo | None:
    
    logger.info("=== データ更新：開始 ===")
    memo = await get_memo_by_id(db_session, memo_id)
    if memo:
        memo.title = target_data.title
        memo.description = target_data.description
        memo.updated_at = datetime.now()
        await db_session.commit()
        await db_session.refresh(memo)
        logger.info(">>> データ更新完了")
    return memo


# 削除処理
async def delete_memo(
        db_session: AsyncSession,
        memo_id: int,
) -> memo_model.Memo | None:
    
    logger.info("=== データ削除：開始 ===")
    memo = await get_memo_by_id(db_session, memo_id)
    if memo:
        await db_session.delete(memo)
        await db_session.commit()
        logger.info(">>> データ削除完了")
    
    return memo



