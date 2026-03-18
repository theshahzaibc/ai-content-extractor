from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

fake_db = {}  # Simple in-memory storage for demo purposes


@router.post("/signup")
def signup(user: UserCreate):
    if user.username in fake_db:
        raise HTTPException(400, "User already exists")
    hashed = pwd_context.hash(user.password)
    fake_db[user.username] = {"username": user.username, "hashed_password": hashed}
    return {"msg": "User created"}


@router.post("/login")
def login(user: UserCreate):
    db_user = fake_db.get(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(401, "Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
