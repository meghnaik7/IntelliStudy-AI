from langchain_chroma import Chroma

from app.core.embeddings import embeddings


VECTOR_DB_PATH = "vector_db"


def get_vector_store():

    vector_store = Chroma(
        collection_name="intellistudy",
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store


def store_documents(chunks):

    vector_store = get_vector_store()

    # Avoid indexing the same source repeatedly
    source = chunks[0].metadata.get("source")

    if source:
        vector_store.delete(
            where={"source": source}
        )

    vector_store.add_documents(chunks)

    return vector_store

def search_documents(query, k=4):

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results    