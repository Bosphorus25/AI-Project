from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer  # this library get token from request head
from passlib.context import CryptContext           # this library help to hash password in db
from dotenv import load_dotenv
import jwt
import os

load_dotenv()

secret_key = os.getenv("my_secret_key")
Algorithm = "HS256"
token_expiry_time = 30

# this variable helps in encrypting and dycripting password
password_encrypter = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash password func
def hash_password(password: str):
    return password_encrypter.hash(password)

# verify hash password 
def verify_hash_password(plain_password: str, hashed_password: str):
    return password_encrypter.verify(plain_password, hashed_password)


# get jwt token here to verify from verify token
get_token_from_header = OAuth2PasswordBearer(tokenUrl="token")


def create_jwt_token(data: dict):
    copy_data = data.copy()
    expiry_time = datetime.now() + timedelta(minutes=token_expiry_time)
    copy_data.update({"exp": expiry_time})
    token =  jwt.encode(copy_data, secret_key, algorithm=Algorithm)
    return token


def verify_token(token: str = Depends(get_token_from_header)):
    decode_token = jwt.decode(token, secret_key, algorithms=Algorithm)
    try:
        return decode_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token expire")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
