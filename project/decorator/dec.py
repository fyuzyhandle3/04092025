from functools import wraps

def ensure_dict_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {"result": result}
    return wrapper



@ensure_dict_result
def add(a, b):
    return a+b

@ensure_dict_result
def greet(name):
    return f"Hi, {name}"

print(add(2, 3))
print(greet("Olga"))