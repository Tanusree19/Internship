
from database.neo4j_connection import driver


def create_knowledge_graph():
    with driver.session() as session:
        session.run("""
            MERGE (w:Workflow {workflow_id: 'WF001'})
            SET w.name = 'MAF Agent Workflow'

            MERGE (s:Step {step_id: 'ST001'})
            SET s.name = 'Data Processing'

            MERGE (d:DataSource {source_id: 'DS001'})
            SET d.name = 'MongoDB Session Data'

            MERGE (c:Chunk {chunk_id: 'CH001'})
            SET c.content = 'Sample session information'

            MERGE (w)-[:HAS_STEP]->(s)
            MERGE (s)-[:USES_SOURCE]->(d)
            MERGE (d)-[:CONTAINS_CHUNK]->(c)
        """)

        print("Knowledge graph created successfully!")


def display_knowledge_graph():
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Workflow)-[r1:HAS_STEP]->(s:Step)
                  -[r2:USES_SOURCE]->(d:DataSource)
                  -[r3:CONTAINS_CHUNK]->(c:Chunk)
            RETURN w.name AS workflow,
                   s.name AS step,
                   d.name AS source,
                   c.content AS chunk
        """)

        print("\n--- MAF Knowledge Graph ---")

        for record in result:
            print("Workflow:", record["workflow"])
            print("Step:", record["step"])
            print("Data Source:", record["source"])
            print("Chunk:", record["chunk"])


def create_indexes():
    with driver.session() as session:
        queries = [
            "CREATE INDEX workflow_id_index IF NOT EXISTS FOR (w:Workflow) ON (w.workflow_id)",
            "CREATE INDEX step_id_index IF NOT EXISTS FOR (s:Step) ON (s.step_id)",
            "CREATE INDEX datasource_id_index IF NOT EXISTS FOR (d:DataSource) ON (d.source_id)",
            "CREATE INDEX chunk_id_index IF NOT EXISTS FOR (c:Chunk) ON (c.chunk_id)"
        ]

        for query in queries:
            session.run(query)

        print("Neo4j indexes created successfully!")


def create_fulltext_index():
    with driver.session() as session:
        session.run("""
            CREATE FULLTEXT INDEX chunk_content_index IF NOT EXISTS
            FOR (c:Chunk)
            ON EACH [c.content]
        """).consume()

        print("Full-text index created successfully!")

if __name__ == "__main__":
    try:
        create_knowledge_graph()
        create_indexes()
        create_fulltext_index()
        display_knowledge_graph()
    finally:
        driver.close()