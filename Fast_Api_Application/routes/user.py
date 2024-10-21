from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import create_access_token, verify_password
from models import User
from database import get_db
from fastapi import Form
from pydantic import BaseModel


router = APIRouter()

@router.post("/register")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = password  # Log here to ensure no failure in hashing
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()  # Check if it hangs here
    return {"msg": "User registered successfully"}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
