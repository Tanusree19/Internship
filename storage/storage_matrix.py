
storage_responsibilities = {
    "MongoDB": {
        "purpose": "Store application data and session information",
        "examples": "User sessions, metadata, status"
    },
    "Neo4j": {
        "purpose": "Store relationships between entities",
        "examples": "Workflow, Step, DataSource, Chunk"
    },
    "Object Storage": {
        "purpose": "Store original files",
        "examples": "PDFs, documents, images"
    },
    "Vector Storage": {
        "purpose": "Store vector embeddings",
        "examples": "Document embeddings, semantic search data"
    }
}


def display_storage_matrix():
    print("\n===== MAF STORAGE RESPONSIBILITY MATRIX =====")

    for storage, details in storage_responsibilities.items():
        print("\nStorage:", storage)
        print("Purpose:", details["purpose"])
        print("Examples:", details["examples"])


if __name__ == "__main__":
    display_storage_matrix()
