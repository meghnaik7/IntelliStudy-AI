from app.chains.quiz_chain import quiz_chain


def generate_quiz(topic, difficulty, num_questions):

    quiz = quiz_chain.invoke({
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": num_questions
    })

    # Verify requested question count
    if len(quiz.questions) != num_questions:
        raise ValueError("Generated question count does not match request")

    return quiz