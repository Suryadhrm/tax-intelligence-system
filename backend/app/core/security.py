from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(p:str)->str: return pwd.hash(p)
def verify_password(p:str,h:str)->bool: return pwd.verify(p,h)
def create_token(sub:str)->str:
    exp=datetime.now(timezone.utc)+timedelta(minutes=settings.jwt_expire_minutes)
    return jwt.encode({"sub":sub,"exp":exp}, settings.jwt_secret, algorithm=settings.jwt_algorithm)
