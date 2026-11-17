from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are IntelliStudy AI, an intelligent document assistant.

        Answer using the provided document context.

        Rules:
        1. Do not invent information.
        2. If the answer is unavailable in the context,
           clearly say so.
        3. Explain concepts in simple language.
        4. Use conversation history when useful.
        """
    ),

    MessagesPlaceholder(variable_name="chat_history"),

    (
        "human",
        """
        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )
])