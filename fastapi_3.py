""" クエリパラメータ
"""
import os
import sys
import json
from typing import Optional

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


class Book:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category

books = [
    Book(id="1", title="Python", category="backend"),
    Book(id="2", title="JavaScript/TypeScript", category="frontend"),
    Book(id="3", title="C/C++", category="embed"),
    Book(id="4", title="HTML/CSS", category="frontend"),
    Book(id="5", title="C#", category="system"),
    Book(id="6", title="Rust", category="embed"),
]

def get_books_by_category(category: Optional[str] = None) -> list[Book]:
    if category is None:
        return books
    else: 
        return [book for book in books if book.category == category]


@app.get("/books/")
async def read_books(category: Optional[str] = None) -> list[dict[str, str]]:
    result = get_books_by_category(category)
    return [{
        "id": book.id,
        "title": book.title,
        "category": book.category
    } for book in result]


