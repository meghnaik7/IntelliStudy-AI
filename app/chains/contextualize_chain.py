from app.core.llm import llm
from app.prompts.contextualize_prompt import contextualize_prompt
from langchain_core.output_parsers import StrOutputParser

contextualize_chain = contextualize_prompt | llm | StrOutputParser()