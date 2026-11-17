from app.services.vector_service import search_documents
from app.chains.document_quiz_chain import document_quiz_chain


def generate_document_quiz(topic, difficulty, num_questions):

    # Step 1: Retrieve relevant document chunks
    docs = search_documents(topic, k=6)

    if not docs:
        raise ValueError("No indexed document content found.")

    # Step 2: Construct context
    context = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\n"
        f"Page: {doc.metadata['page'] + 1 if 'page' in doc.metadata else 'N/A'}\n"
        f"{doc.page_content}"
        for doc in docs
    )

    # Step 3: Generate quiz
    quiz = document_quiz_chain.invoke({
        "context": context,
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": num_questions
    })

    # Step 4: Validate question count
    if len(quiz.questions) != num_questions:
        raise ValueError("Generated question count does not match request.")

    # Step 5: Collect sources
    sources = [
        {
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata["page"] + 1
                    if "page" in doc.metadata else "N/A"
        }
        for doc in docs
    ]

    return {
        "quiz": quiz,
        "sources": sources
    }