import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin@localhost/FastAPI")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
