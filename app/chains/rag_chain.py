from app.core.llm import llm
from app.prompts.rag_prompt import rag_prompt

from langchain_core.output_parsers import StrOutputParser


rag_chain = rag_prompt | llm | StrOutputParser()