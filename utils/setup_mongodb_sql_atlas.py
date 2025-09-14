from dotenv import load_dotenv
from pymongo import MongoClient  # this dependency helps to connect with mongodb and apply crud in db
import os

# call load_dotenv to access .env
load_dotenv()

db_uri = os.getenv("db_url") # url is imported in variable
if not db_uri:
    raise ValueError("db setup not working")
client = MongoClient(db_uri) # mongoclient function from pymongo helps to connect with db provider client using url

# connection with specific db provided by our client db provider
db = client["dummy"]