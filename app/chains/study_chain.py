from langchain_core.output_parsers import StrOutputParser

from app.core.llm import llm
from app.prompts.study_prompt import study_prompt

study_chain = study_prompt | llm | StrOutputParser()