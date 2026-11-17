from langchain_core.messages import HumanMessage

from app.agents.study_agent import study_agent


def run_study_agent(question, chat_history):

    # Add new user message to existing history
    messages = chat_history + [
        HumanMessage(content=question)
    ]

    # Invoke agent
    response = study_agent.invoke({
        "messages": messages
    })

    # Get updated conversation history
    updated_history = response["messages"]

    # Get final AI response
    answer = updated_history[-1].content

    return answer, updated_history