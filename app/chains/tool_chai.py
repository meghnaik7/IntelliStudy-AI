from app.core.llm import llm

from app.tools.study_tools import (
    search_study_material,
    calculate_percentage
)

tools = [
    search_study_material,
    calculate_percentage
]

llm_with_tools = llm.bind_tools(tools)