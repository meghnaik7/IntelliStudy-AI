from app.services.vector_service import get_vector_store
from app.chains.rag_chain import rag_chain
from app.chains.contextualize_chain import contextualize_chain


def ask_question(query, chat_history):

    # Step 1: Rewrite question using conversation history
    if chat_history:
        standalone_question = contextualize_chain.invoke({
            "chat_history": chat_history,
            "question": query
        })
    else:
        standalone_question = query

    # Step 2: Retrieve relevant documents
    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(standalone_question)

    if not docs:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }

    # Step 3: Construct context
    context = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\n"
        f"{doc.page_content}"
        for doc in docs
    )

    # Step 4: Generate answer
    answer = rag_chain.invoke({
        "context": context,
        "question": standalone_question,
        "chat_history": chat_history
    })

    # Step 5: Return answer and sources
    sources = [
        {
            "source": doc.metadata.get("source"),
            "page": (
                doc.metadata["page"] + 1
                if "page" in doc.metadata else "N/A"
            )
        }
        for doc in docs
    ]

    return {
        "answer": answer,
        "sources": sources
    }