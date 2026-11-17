from app.chains.study_chain import study_chain
from app.services.quiz_service import generate_quiz
from app.services.quiz_evaluation import evaluate_quiz
from app.services.document_service import load_document, split_documents
from app.services.vector_service import (
    store_documents,
    search_documents
)
from app.services.rag_service import ask_question
from langchain_core.messages import HumanMessage, AIMessage
from app.services.chat_history_service import (
    initialize_database,
    save_message,
    load_chat_history
)
from app.services.document_quiz_service import generate_document_quiz
from app.services.quiz_evaluation import evaluate_quiz
from app.services.agent_service import run_study_agent
# Feature 1: Explain a topic
def explain_topic():

    topic = input("Enter topic: ")
    difficulty = input("Enter difficulty: ")

    response = study_chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })

    print("\n========== STUDY EXPLANATION ==========")
    print(response)


# Feature 2: Generate a quiz
def create_quiz():

    topic = input("Enter topic: ")
    difficulty = input("Enter difficulty: ")

    try:
        num_questions = int(input("Number of questions: "))

        if not 1 <= num_questions <= 20:
            print("Enter a number between 1 and 20.")
            return

        quiz = generate_quiz(topic, difficulty, num_questions)

        print("\n========== INTELLISTUDY QUIZ ==========")

        user_answers = []

        # Display questions
        for i, q in enumerate(quiz.questions, 1):

            print(f"\nQ{i}. {q.question}")

            for j, option in enumerate(q.options, 1):
                print(f"{j}. {option}")

            while True:

                try:
                    choice = int(input("Your answer (1-4): "))

                    if 1 <= choice <= 4:
                        user_answers.append(q.options[choice - 1])
                        break

                    print("Select a number between 1 and 4.")

                except ValueError:
                    print("Please enter a valid number.")

        # Evaluate quiz
        result = evaluate_quiz(quiz, user_answers)

        # Display results
        print("\n========== QUIZ RESULTS ==========")

        print(f"Score: {result['score']}/{result['total']}")
        print(f"Percentage: {result['percentage']:.2f}%")

        for i, r in enumerate(result["results"], 1):

            print(f"\nQ{i}. {r['question']}")

            print("Your answer:", r["user_answer"])
            print("Correct answer:", r["correct_answer"])

            print(
                "Result:",
                "Correct" if r["is_correct"] else "Incorrect"
            )

            print("Explanation:", r["explanation"])

    except ValueError as e:
        print("Invalid input:", e)

def process_pdf():

    file_path = input("Enter document path: ")

    try:

        # Load document
        docs = load_document(file_path)

        print("\n========== DOCUMENT INFORMATION ==========")
        print("Total Pages:", len(docs))

        # Split document
        chunks = split_documents(docs)

        print("\n========== CHUNK INFORMATION ==========")

        print("Total Chunks:", len(chunks))

        # Display first chunk
        print("\nFirst Chunk Content:\n")
        print(chunks[0].page_content)

        # Display metadata
        print("\nFirst Chunk Metadata:")
        print(chunks[0].metadata)

    except (FileNotFoundError, ValueError) as e:
        print("Error:", e)

def index_document():

    file_path = input("Enter document path: ")

    try:

        # Load document
        docs = load_document(file_path)

        # Split document
        chunks = split_documents(docs)

        # Store embeddings
        store_documents(chunks)

        print("\n========== INDEXING COMPLETE ==========")
        print("Total Pages:", len(docs))
        print("Total Chunks:", len(chunks))
        print("Documents stored successfully!")

    except (FileNotFoundError, ValueError) as e:
        print("Error:", e)   

def search_document():

    query = input("Ask a question about your document: ")

    try:

        results = search_documents(query, k=4)

        print("\n========== SEARCH RESULTS ==========")

        if not results:
            print("No relevant documents found.")
            return

        for i, doc in enumerate(results, 1):

            print(f"\nResult {i}")
            print("Content:", doc.page_content)
            print("Metadata:", doc.metadata)

    except Exception as e:
        print("Search error:", e)  


def chat_with_document():

    print("\n========== INTELLISTUDY DOCUMENT CHAT ==========")

    session_id = input("Enter session ID: ")

    print("Session ID:", session_id)

    chat_history = load_chat_history(session_id)

    print(f"Loaded {len(chat_history)} previous messages.")

    while True:

        query = input("\nYou: ")

        if query.lower() == "exit":
            break

        try:
            result = ask_question(query, chat_history)

            answer = result["answer"]

            print("\nAI:", answer)

            save_message(session_id, "human", query)
            save_message(session_id, "ai", answer)

            chat_history = load_chat_history(session_id)

        except Exception as e:
            print("Error:", e)


from app.services.agent_service import run_study_agent


def chat_with_agent():

    print("\n========== INTELLISTUDY AI AGENT ==========")

    # In-memory conversation history
    chat_history = []

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            break

        if not question:
            print("Please enter a question!")
            continue

        try:

            answer, chat_history = run_study_agent(
                question,
                chat_history
            )

            print("\nIntelliStudy AI:", answer)

        except Exception as e:
            print("Error:", e)

    print("\nConversation ended. In-memory history cleared.")

def create_document_quiz():

    print("\n========== DOCUMENT-BASED QUIZ ==========")

    topic = input("Enter topic: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

    try:
        num_questions = int(input("Number of questions: "))

        if num_questions < 1 or num_questions > 20:
            print("Please enter between 1 and 20 questions.")
            return

        # Generate quiz from indexed documents
        result = generate_document_quiz(
            topic,
            difficulty,
            num_questions
        )

        quiz = result["quiz"]

        # Display questions
        user_answers = []

        for i, question in enumerate(quiz.questions):

            print(f"\nQ{i + 1}. {question.question}")

            for j, option in enumerate(question.options):
                print(f"{j + 1}. {option}")

            while True:
                answer = input("Your answer (1-4): ")

                if answer in ["1", "2", "3", "4"]:
                    user_answers.append(
                        question.options[int(answer) - 1]
                    )
                    break

                print("Invalid choice! Enter 1-4.")

        # Evaluate quiz
        evaluation = evaluate_quiz(quiz, user_answers)

        print("\n========== QUIZ RESULT ==========")

        print(f"Score: {evaluation['score']}/{evaluation['total']}")
        print(f"Percentage: {evaluation['percentage']:.2f}%")

        for i, answer_result in enumerate(evaluation["results"]):

            print(f"\nQuestion {i + 1}")
            print("Your answer:", answer_result["user_answer"])
            print("Correct answer:", answer_result["correct_answer"])

            print(
                "Result:",
                "Correct" if answer_result["is_correct"] else "Incorrect"
            )

            print("Explanation:", answer_result["explanation"])

        # Display sources
        print("\n========== DOCUMENT SOURCES ==========")

        for source in result["sources"]:
            print(
                f"File: {source['source']} | "
                f"Page: {source['page']}"
            )

    except Exception as e:
        print("Error generating document quiz:", e)

# Main application
def main():

    initialize_database()

    while True:

        print("\n========== INTELLISTUDY AI ==========")
        print("1. Explain a topic")
        print("2. Generate a general quiz")
        print("3. Index a document")
        print("4. Search documents")
        print("5. Chat with documents")
        print("6. Generate quiz from documents")
        print("7. Chat with AI Agent")
        print("8. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            explain_topic()

        elif choice == "2":
            create_quiz()

        elif choice == "3":
            index_document()

        elif choice == "4":
            search_document()

        elif choice == "5":
            chat_with_document()

        elif choice == "6":
            create_document_quiz()

        elif choice == "7":
            chat_with_agent()

        elif choice == "8":
            print("Thank you for using IntelliStudy AI!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()