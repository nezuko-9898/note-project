import os
from dotenv import load_dotenv

# ✅ LOAD ENV FIRST (VERY IMPORTANT)
load_dotenv()

from agno.agent import Agent
from agno.models.groq import Groq
from app.ai_services.prompt import SYSTEM_PROMPT

# ✅ DEBUG (remove later)
print("GROQ_API_KEY loaded:", bool(os.getenv("GROQ_API_KEY")))

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=SYSTEM_PROMPT,
)

def ask_note_agent(question: str, note_text: str) -> str:
    prompt = f"""
NOTES:
{note_text}

QUESTION:
{question}
"""
    response = agent.run(prompt)
    return response
