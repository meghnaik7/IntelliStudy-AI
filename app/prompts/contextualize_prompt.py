from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Given the conversation history and latest user question,
        rewrite the latest question into a standalone question.

        Do not answer the question.
        If it is already standalone, return it unchanged.
        """
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])