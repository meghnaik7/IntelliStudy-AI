from app.core.llm import llm
from app.prompts.document_quiz_prompt import document_quiz_prompt
from app.schemas.quiz import Quiz

structured_llm = llm.with_structured_output(Quiz)

document_quiz_chain = document_quiz_prompt | structured_llm