from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # Import this
from config import DATABASE_URL

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for models
Base = declarative_base()  # Add this

# Dependency to get the DB session
def get_db():
    try:
        print("Creating DB session.")
        db = SessionLocal()
        yield db
    except Exception as e:
        print("Database error: {e}")
        raise
    finally:
        print("Closing DB session.")
        db.close()
