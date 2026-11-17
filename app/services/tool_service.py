from langchain_core.messages import HumanMessage

from app.chains.tool_chain import llm_with_tools

from app.tools.study_tools import (
    search_study_material,
    calculate_percentage
)


# Map tool names to Python functions
tool_map = {
    "search_study_material": search_study_material,
    "calculate_percentage": calculate_percentage
}


def run_tool_agent(question):

    messages = [HumanMessage(content=question)]

    # First LLM call
    response = llm_with_tools.invoke(messages)

    messages.append(response)

    # Execute requested tools
    while response.tool_calls:

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]

            selected_tool = tool_map.get(tool_name)

            if selected_tool:

                tool_message = selected_tool.invoke(tool_call)

                messages.append(tool_message)

            else:
                raise ValueError(f"Unknown tool: {tool_name}")

        # Send tool results back to LLM
        response = llm_with_tools.invoke(messages)

        messages.append(response)

    return response.content