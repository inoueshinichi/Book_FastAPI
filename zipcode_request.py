
import os
import sys

import json

import logging
logging.basicConfig(format="%(asctime)s [%(levelname)s] (Line:%(lineno)d) at %(name)s : %(message)s", datefmt="[%X]")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.WARNING)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.CRITICAL)

import requests


def main():

    url = "https://zipcloud.ibsnet.co.jp/api/search"

    zip = input("郵便番号を入力=>")

    param = {"zipcode": zip}

    res = requests.get(url, param)

    data = json.loads(res.text)

    logger.debug(data)
    print("*" * 50)

    if data['results'] is not None:
        address_info = data['results'][0]
        zipcode = address_info['zipcode']
        address = f"{address_info['address1']}{address_info['address2']}{address_info['address3']}"

        logger.info(f"郵便番号: {zipcode} 住所: {address}")

    else:
        logger.error("住所が見つかりませんでした。")


if __name__ == "__main__":
    main()