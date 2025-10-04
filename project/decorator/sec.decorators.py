from functools import wraps


def round_result(ndigits: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return round(result, ndigits)
            return result

        return wrapper

    return decorator


@round_result(2)
def divide(a, b):
    return a / b


@round_result(3)
def get_pi():
    return 3.1415926535


@round_result(2)
def greet(name):
    return f'hello, {name}'


print(divide(10, 3))
print(get_pi())
print(greet('Anna'))
