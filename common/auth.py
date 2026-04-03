import jwt

SECRET_KEY = "mysecret"

def create_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")