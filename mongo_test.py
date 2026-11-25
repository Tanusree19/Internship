
from database.mongodb import client, db, sessions_collection

print("Database name:", db.name)
print("Collection name:", sessions_collection.name)

print("MongoDB connection test completed!")

client.close()
