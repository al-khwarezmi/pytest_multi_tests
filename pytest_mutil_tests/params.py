"""load params"""
import json


def get_config() -> dict:
    """load params"""

    with open("params.json", "r", encoding="utf-8") as params:
        return json.loads(params.read())


print(get_config())
