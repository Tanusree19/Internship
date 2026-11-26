
from database.mongodb import db
from datetime import datetime, timezone, timedelta
from pymongo.errors import WriteError

collection = db["validated_sessions"]

# Test 1: Insert valid session
valid_session = {
    "session_id": "validation_test_001",
    "user_id": "user_test",
    "status": "active",
    "created_at": datetime.now(timezone.utc),
    "expires_at": datetime.now(timezone.utc) + timedelta(days=7),
    "messages": ["Hello", "Test session"]
}

try:
    result = collection.insert_one(valid_session)
    print("Valid session inserted successfully!")
    collection.delete_one({"_id": result.inserted_id})
except Exception as error:
    print("Valid session test failed:", error)

# Test 2: Insert invalid session
invalid_session = {
    "session_id": "validation_test_002",
    "user_id": "user_test",
    "status": "invalid_status",
    "messages": ["Invalid test"]
}

try:
    collection.insert_one(invalid_session)
    print("ERROR: Invalid session was accepted!")
except WriteError:
    print("Invalid session rejected successfully!")
except Exception as error:
    print("Unexpected error:", error)
