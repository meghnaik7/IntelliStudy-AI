from langchain.agents import create_agent

from app.core.llm import llm

from app.tools.study_tools import (
    search_study_material,
    calculate_percentage
)


# Register available tools
tools = [
    search_study_material,
    calculate_percentage
]


# Create AI Agent
study_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are IntelliStudy AI, an intelligent study assistant.

    You can:
    1. Search indexed study documents.
    2. Calculate percentages.
    3. Answer general study questions.

    Use tools whenever they are useful.
    Explain answers in simple language.
    """
)