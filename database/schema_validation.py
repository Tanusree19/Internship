
from database.mongodb import db

# Define MongoDB JSON Schema
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "session_id",
            "user_id",
            "status",
            "created_at",
            "expires_at",
            "messages"
        ],
        "properties": {
            "session_id": {"bsonType": "string"},
            "user_id": {"bsonType": "string"},
            "status": {
                "bsonType": "string",
                "enum": ["active", "expired"]
            },
            "created_at": {"bsonType": "date"},
            "expires_at": {"bsonType": "date"},
            "messages": {
                "bsonType": "array",
                "items": {"bsonType": "string"}
            }
        }
    }
}

# Create collection with schema validation
if "validated_sessions" not in db.list_collection_names():
    collection = db.create_collection(
        "validated_sessions",
        validator=validator,
        validationLevel="strict",
        validationAction="error"
    )
    print("Validated collection created successfully!")
else:
    collection = db["validated_sessions"]
    print("Validated collection already exists.")

# Create TTL index
collection.create_index(
    "expires_at",
    expireAfterSeconds=0
)

print("TTL index created successfully!")
print("Schema validation setup completed!")
