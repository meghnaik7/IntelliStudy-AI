from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Send prompt
response = llm.invoke("Explain Generative AI in simple words")

# Print response
print(response.content)