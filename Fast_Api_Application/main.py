from fastapi import FastAPI
from routes import user, data
from models import User
from database import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user.router, prefix="/user")
app.include_router(data.router)

@app.get("/")
def root():
    return {"message": "FastAPI Service is running"}
