# base64_example.py
import base64

string = 'hello'

# кодуємо: str -> bytes -> base64 bytes -> str
encoded_bytes = base64.b64encode(string.encode('utf-8'))
encoded_str = encoded_bytes.decode('ascii')
print("Encoded (base64):", encoded_str)

# декодуємо: base64 str -> bytes -> декодовані bytes -> str
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')
print("Decoded (original):", decoded_str)

# приклад: якщо кинути b64decode на не-base64 рядок — отримаєш помилку або "сміття"
try:
    print("Trying to decode plain 'hello' as base64:")
    print(base64.b64decode('hello'))
except Exception as e:
    print("Error decoding non-base64 string:", e)