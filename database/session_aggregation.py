
from database.mongodb import sessions_collection


def get_session_statistics():
    print("\n--- Session Statistics by Status ---")

    pipeline = [
        {
            "$match": {
                "status": {"$in": ["active", "expired"]}
            }
        },
        {
            "$group": {
                "_id": "$status",
                "total_sessions": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "total_sessions": -1
            }
        }
    ]

    results = sessions_collection.aggregate(pipeline)

    for result in results:
        print(
            "Status:", result["_id"],
            "| Total Sessions:", result["total_sessions"]
        )


def get_user_session_statistics():
    print("\n--- Sessions Grouped by User ---")

    pipeline = [
        {
            "$match": {
                "status": "active"
            }
        },
        {
            "$group": {
                "_id": "$user_id",
                "total_sessions": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "total_sessions": -1
            }
        }
    ]

    results = sessions_collection.aggregate(pipeline)

    for result in results:
        print(
            "User ID:", result["_id"],
            "| Total Sessions:", result["total_sessions"]
        )


if __name__ == "__main__":
    get_session_statistics()
    get_user_session_statistics()
