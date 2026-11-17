from langchain_core.prompts import ChatPromptTemplate


quiz_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are an expert computer science exam question generator.

        Generate high-quality multiple-choice questions.

        Follow these rules:

        1. Generate exactly the requested number of questions.
        2. Each question must have exactly four options.
        3. Only one option must be correct.
        4. Avoid repetitive questions.
        5. Explanations must be clear and educational.
        6. Follow the requested difficulty level.
        7. Make incorrect options realistic and relevant.
        """
    ),

    (
        "human",
        """
        Generate a quiz using the following details:

        Topic: {topic}
        Difficulty: {difficulty}
        Number of Questions: {num_questions}
        """
    )

])