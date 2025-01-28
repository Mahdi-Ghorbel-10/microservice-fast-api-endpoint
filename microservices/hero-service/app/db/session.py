import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError



DATABASE_URL = "postgresql+psycopg2://mahdi:123456789@localhost:5432/fast_api"

# Retry mechanism for database connection
for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        break
    except OperationalError:
        print(f"Database not ready, retrying in 2 seconds... (Attempt {attempt + 1}/10)")
        time.sleep(2)
else:
    raise Exception("Could not connect to the database after 10 retries.")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()