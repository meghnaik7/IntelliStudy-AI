from langchain.tools import tool

from app.services.vector_service import search_documents


@tool
def search_study_material(query: str) -> str:
    """
    Search indexed study documents for information
    related to the given query.
    """

    docs = search_documents(query, k=4)

    if not docs:
        return "No relevant information found."

    context = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\n"
        f"{doc.page_content}"
        for doc in docs
    )

    return context

@tool
def calculate_percentage(obtained: float, total: float) -> float:
    """
    Calculate percentage based on obtained marks and total marks.
    """

    if total <= 0:
        return 0.0

    return round((obtained / total) * 100, 2)
