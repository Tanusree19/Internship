
from database.neo4j_connection import driver


def get_all_workflows():
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Workflow)
            RETURN w.workflow_id AS id, w.name AS name
        """)

        print("\n--- All Workflows ---")
        for record in result:
            print(record["id"], "-", record["name"])


def get_all_steps():
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Workflow)-[:HAS_STEP]->(s:Step)
            RETURN w.name AS workflow, s.name AS step
        """)

        print("\n--- Workflow Steps ---")
        for record in result:
            print(record["workflow"], "->", record["step"])


def count_nodes():
    with driver.session() as session:
        result = session.run("""
            MATCH (n)
            RETURN labels(n) AS node_type, count(n) AS total
        """)

        print("\n--- Node Count ---")
        for record in result:
            print(record["node_type"], ":", record["total"])
def search_chunks(search_text):
    with driver.session() as session:
        result = session.run("""
            CALL db.index.fulltext.queryNodes(
                'chunk_content_index', $search_text
            )
            YIELD node, score
            RETURN node.chunk_id AS id,
                   node.content AS content,
                   score
        """, search_text=search_text)

        print("\n--- Full Text Search Results ---")

        for record in result:
            print("Chunk ID:", record["id"])
            print("Content:", record["content"])
            print("Score:", record["score"])

if __name__ == "__main__":
    try:
        get_all_workflows()
        get_all_steps()
        count_nodes()
        search_chunks("session")
    finally:
        driver.close()