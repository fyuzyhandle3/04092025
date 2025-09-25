def get_ticket_price(age: int) -> float:
    BASE_PRICE = 100.0

    if age < 6:
        return 0.0
    elif age <= age <= 17:
        return BASE_PRICE * 0.5
    elif 18 <= age <= 59:
        return BASE_PRICE
    else:
        return BASE_PRICE * 0.7
