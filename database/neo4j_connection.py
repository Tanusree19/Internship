
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(override=True)

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    uri,
    auth=(username, password)
)


def test_connection():
    try:
        with driver.session() as session:
            result = session.run(
                "RETURN 'Neo4j Connected Successfully!' AS message"
            )
            print(result.single()["message"])
    except Exception as error:
        print("Connection error:", error)


if __name__ == "__main__":
    test_connection()
    driver.close()
