
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "agent_builder")

if not MONGODB_URI:
    raise ValueError("MongoDB URI not found in .env file")

# Connect to MongoDB
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

# Verify connection
try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")

except Exception as error:
    print("MongoDB connection failed:", error)
    raise
# Select database and collection
db = client[DATABASE_NAME]
sessions_collection = db["sessions"]
