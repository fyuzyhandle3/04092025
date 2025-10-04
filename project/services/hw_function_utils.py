from typing import List, Union
from services.logger import logger


def get_greeting() -> str:
    result = "Hello, buddy"
    logger.info(f'get_greeting() called -> {result}')
    return result


def get_max_number(numbers: List[Union[int, float]]) -> Union[int, float]:
    filtered = [n for n in numbers if isinstance(n, (int, float))]
    result = max(filtered) if filtered else 0
    logger.info(f'get_max_number({numbers})) called -> {result}')
    return result


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    result = a * b
    logger.info(f"multiply_numbers({a}, {b}) called -> {result}")
    return result
