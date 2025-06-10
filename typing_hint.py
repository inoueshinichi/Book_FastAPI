
from multiprocessing import Value
import os
import sys

import json
from typing import (
    Optional,
    Callable,
    Annotated,
)

import logging
logging.basicConfig(format="%(asctime)s [%(levelname)s] (Thread:%(thread)d) (Line:%(lineno)d) at %(name)s : %(message)s", datefmt="[%X]")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)

def add(num1: int, num2: int) -> str:
    result: str = "足し算結果=>"
    return result + str(num1 + num2)

def greet(name: str) -> str:
    return f"おはよう!{name}"

def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor

def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

def count_characters(word_list: list[str]) -> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        count_map[word] = len(word)
    return count_map

def get_profile(
        email: str,
        username: Optional[str] = None,
        age: Optional[int] = None,
    ) -> dict:
    profile: dict[str, str | int] = {"email": email}
    if username:
        profile["username"] = username
    if age:
        profile["age"] = age
    return profile

def process_value(
        value: Annotated[int, "範囲: 0 <= value <= 100"]
    ) -> None:
    if 0 <= value <= 100:
        print(f"受け取った値は範囲内です。: {value}")
    else:
        raise ValueError(f"範囲外の値です。受取った値: {value}")
    
def parse_input(value: int | str) -> str:
    if isinstance(value, int):
        return f"値は整数型です=>:{value}"
    elif isinstance(value, str):
        return f"値は文字列型です=>:{value}"
    else:
        raise ValueError("引数が整数型/文字列型ではありません")

def main():    
    result_add = add(10, 20)
    logger.debug(result_add)
    pass
    greeting = greet('TinyTank')
    logger.debug(greeting)
    pass
    result_divide = divide(10., 2.)
    logger.debug(f"割り算の結果=>{result_divide}")
    pass
    process_items(["C/C++", "JavaScript", "Python", "C#", "Rust"])
    pass
    character_counts = count_characters(["apple", "google", "meta", "openai"])
    logger.debug(f"文字に対する文字数は=>{character_counts}")
    pass
    user_profile = get_profile(email="tiny.tank.develop@gmail.com")
    logger.debug(user_profile)
    pass
    complete_profile = get_profile(email="tiny.tnak.develop@gmail.com", username="tiny_tank", age=35)
    logger.debug(complete_profile)
    pass
    process_value(50)
    pass
    try:
        process_value(-1)
    except ValueError as e:
        logger.error(e)
    pass
    logger.debug(parse_input(123))
    pass
    logger.debug(parse_input("abc"))
    pass
    try:
        parse_input(99.9)
    except ValueError as e:
        logger.error(e)

if __name__ == "__main__":
    main()