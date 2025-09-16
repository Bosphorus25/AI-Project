from sqlalchemy import create_engine       # this dependency helps to connect with postgress_sql db and apply crud in db
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("neon_url")
if not db_url:
    raise ValueError("db setup not working")

engine = create_engine(db_url)    # creaate_engine function from sqlalchemy helps to connect with db provider client using url

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)    # stop from lossing connection

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()