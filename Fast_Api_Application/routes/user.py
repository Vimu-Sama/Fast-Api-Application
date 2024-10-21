from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import create_access_token, verify_password, confirm_password
from models import User
from database import get_db
from fastapi import Form
from pydantic import BaseModel

router = APIRouter()

class UserRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register_user(request: UserRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    confirm_password(request.password)  # Adjust hashing function
    hashed_password = request.password
    new_user = User(username=request.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(request: UserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

