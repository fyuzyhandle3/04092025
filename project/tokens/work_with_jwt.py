import time
import datetime
import jwt

SECRET = 'k-wdqwdqwdqfewfwefwqe'


def make_payload(name, age, city, seconds_valid):
    now = datetime.datetime.utcnow()
    return {
        "user_name": name,
        "age": age,
        "city": city,
        "iat": now,
        "exp": now + datetime.timedelta(seconds=seconds_valid)
    }


def create_token(payload, secret):
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token


def decode_token(token, secret):
    return jwt.decode(token, secret, algorithms=['HS256'])


if __name__ == "__main__":
    name = "Vasyl"
    age = 18
    city = "Lviv"

    p1 = make_payload(name, age, city, 1000)
    t1 = create_token(p1, SECRET)
    print("TOKEN1 (1000s):", t1)
    print("Decode TOKEN1:", decode_token(t1, SECRET))

    p2 = make_payload(name, age, city, 10)
    t2 = create_token(p2, SECRET)
    print("\nTOKEN2 (10s):", t2)
    print("Decoded immediately:", decode_token(t2, SECRET))
    print("Sleeping 15s to let it expire...")
    time.sleep(15)
    print("Try decode after sleep (expect ExpiredSignatureError):")
    try:
        decode_token(t2, SECRET)
        print("Decoded (unexpected) — token still valid")
    except jwt.ExpiredSignatureError as e:
        print("ExpiredSignatureError caught as expected:", e)
    except Exception as e:
        print("Other error:", e)

    p3 = make_payload(name, age, city, 500)
    t3 = create_token(p3, SECRET)
    print("\nTOKEN3 (500s):", t3)
    wrong_secret = "incorrect_secret_key"
    print("Try decode with wrong secret (expect InvalidSignatureError):")
    try:
        decode_token(t3, wrong_secret)
        print("Decoded (unexpected) with wrong secret")
    except jwt.InvalidSignatureError as e:
        print("InvalidSignatureError caught as expected:", e)
    except Exception as e:
        print("Other error:", e)
