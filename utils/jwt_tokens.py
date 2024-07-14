import jwt

SECRET_KEY = 'KeySecReT'
ALGORITHM = 'HS256'


async def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def decode_access_token(token: str):
    return jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
