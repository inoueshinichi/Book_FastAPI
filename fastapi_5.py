""" CRUD
"""
import os
import sys
import json
from turtle import update
from typing import Optional
from datetime import datetime
from pydantic import (
    BaseModel,
    ValidationError,
    Field,
)

import logging

from fastapi_3 import Book
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


class BookSchema(BaseModel):
    title: str #= Field(..., description="タイトルの指定：必須", example="龍が如く")
    category: str #= Field(..., description="カテゴリの指定：必須", example="comics")
    #publish_year: int = Field(..., description="出版年の指定：任意", example=2025)
    #price: float = Field(..., gt=0, le=5000, description="価格の指定：0 < 価格 <= 5000", example=4000)

class BookResponseSchema(BookSchema):
    id: int

# デモ用のデータベース代わりに使うリスト
# ダミーの書籍情報リスト
books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, title="Python入門", category="technical"),
    BookResponseSchema(id=2, title="初めてのプログラミング", category="technical"),
    BookResponseSchema(id=3, title="進撃の巨人", category="comics"),
    BookResponseSchema(id=4, title="DB親父", category="cosmic"),
    BookResponseSchema(id=5, title="週刊ダイヤモンド", category="magazine"),
    BookResponseSchema(id=6, title="ザ・経営者", category="magazine"),
]

@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    # 書籍IDを作成
    new_book_id = max([book.id for book in books], default=0) + 1
    # 新しい書籍を作成
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    # ダミーデータに追加
    books.append(new_book)
    # 登録書籍データを返す
    return new_book

@app.get("/books/", response_model=list[BookResponseSchema])
def read_books():
    # 全ての書籍データを取得
    return books

@app.get("/books/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
    # 特定IDの書籍情報を更新
    for index, exsisting_book in enumerate(books):
        if exsisting_book.id == book_id:
            updated_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
        
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=BookResponseSchema)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

