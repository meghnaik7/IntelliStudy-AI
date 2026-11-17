from app.core.llm import llm
from app.prompts.quiz_prompt import quiz_prompt
from app.schemas.quiz import Quiz


# Convert LLM into a structured output model
structured_llm = llm.with_structured_output(Quiz)


# Create quiz generation pipeline
quiz_chain = quiz_prompt | structured_llm