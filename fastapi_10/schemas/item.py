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


class Item(BaseModel):
    item_id: int
    item_name: str
    category_id: int