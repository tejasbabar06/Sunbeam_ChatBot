import os
import chromadb
from chromadb.config import Settings
from config.settings import VECTOR_DB_PATH

_client = None
_collection = None


def get_collection():
    global _client, _collection

    if _collection is not None:
        return _collection

    # ✅ Ensure vector DB directory exists
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    _client = chromadb.Client(
        Settings(
            persist_directory=VECTOR_DB_PATH,
            anonymized_telemetry=False
        )
    )

    _collection = _client.get_or_create_collection(
        name="sunbeam_docs"
    )

    return _collection


def store_documents(collection, documents, embed_model):
    # ✅ Do not reinsert if already stored
    if collection.count() > 0:
        return

    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    ids = [f"doc_{i}" for i in range(len(texts))]

    embeddings = embed_model.embed_documents(texts)

    if not embeddings:
        raise ValueError("No embeddings generated. Check input documents.")

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )
