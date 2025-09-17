

def greet_person(name: str = "Гість") -> str:
    return f"Привіт, {name}!"

def is_even(number: int) -> bool:
    return number % 2 == 0

def reverse_string(text: str) -> str:
    return text[::-1]


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Список не повинен бути порожнім")
    return sum(numbers) / len(numbers)

def add_person_to_list(people: list[str], person: str) -> list[str]:
    return people + [person]

def count_vowels(text: str) -> int:
    vowels = "аеєиіїоуюяAEЄИІЇОУЯaeiouyAEIOUY"
    return sum(1 for char in text if char in vowels)

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9
