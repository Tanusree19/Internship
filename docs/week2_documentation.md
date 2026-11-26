\# MAF-Agent-Builder – Week 2 Documentation



\## 1. MongoDB Integration

\- Connected Python application to MongoDB Atlas using PyMongo.

\- Created the `agent\_builder` database and `sessions` collection.

\- Implemented session CRUD operations: Create, Read, Update and Delete.

\- Added a TTL index to manage session expiration.

\- Implemented aggregation pipelines to group sessions by status and user.



\## 2. Neo4j Integration

\- Connected Python application to Neo4j AuraDB.

\- Created Workflow, Step, DataSource and Chunk nodes.

\- Established relationships between the nodes.

\- Created property indexes and a full-text index.

\- Implemented Cypher queries to retrieve and search graph data.



\## 3. Storage Responsibility Matrix



| Storage | Responsibility |

|---|---|

| MongoDB | Application and session data |

| Neo4j | Entity relationships |

| Object Storage | Original files |

| Vector Storage | Vector embeddings |



\## 4. Technologies Used

\- Python

\- PyMongo

\- MongoDB Atlas

\- Neo4j AuraDB

\- Cypher Query Language

\- FastAPI



\## 5. Outcome

Successfully integrated MongoDB and Neo4j into the MAF-Agent-Builder project. Implemented database operations, graph relationships, indexes, full-text search and storage responsibility mapping.

