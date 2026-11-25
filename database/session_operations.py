
from datetime import datetime, timezone, timedelta
from database.mongodb import sessions_collection


# 1. CREATE SESSION
def create_session():
    session = {
        "session_id": "session_002",
        "user_id": "user_002",
        "status": "active",
        "created_at": datetime.now(timezone.utc),
        "expires_at": datetime.now(timezone.utc) + timedelta(days=7),
        "messages": [
            "Hello",
            "Welcome to MAF Agent Builder"
        ]
    }

    result = sessions_collection.insert_one(session)

    print("\nSession inserted successfully!")
    print("Inserted ID:", result.inserted_id)


# 2. GET ALL SESSIONS
def get_sessions():
    print("\nAll stored sessions:")

    for session in sessions_collection.find():
        print(session)


# 3. GET SESSION BY ID
def get_session_by_id(session_id):
    session = sessions_collection.find_one(
        {"session_id": session_id}
    )

    if session:
        print("\nSession found:")
        print(session)
    else:
        print("\nSession not found!")


# 4. UPDATE SESSION

def update_session(session_id):
    result = sessions_collection.update_one(
        {"session_id": session_id},
        {"$set": {"status": "expired"}}
    )

    if result.modified_count > 0:
        print("\nSession updated successfully!")
    else:
        print("\nNo session was updated.")

# 5. DELETE SESSION
def delete_session(session_id):
    result = sessions_collection.delete_one(
        {"session_id": session_id}
    )

    if result.deleted_count:
        print("\nSession deleted successfully!")
    else:
        print("\nSession not found!")


# 6. COUNT SESSIONS
def count_sessions():
    total = sessions_collection.count_documents({})

    print("\nTotal sessions:", total)


# MAIN EXECUTION
if __name__ == "__main__":

    # Create a new session
    create_session()

    # Display all sessions
    get_sessions()

    # Find a particular session
    get_session_by_id("session_002")

    # Update session status
    update_session("session_002")

    # Display updated session
    get_session_by_id("session_002")

    # Count all sessions
    count_sessions()

    # Delete the test session
    delete_session("session_002")

    # Display final session count
    count_sessions()
