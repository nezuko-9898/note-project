
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from app.ai_services.prompt import SYSTEM_PROMPT
load_dotenv()
llm = Groq(id="llama-3.3-70b-versatile")

agent = Agent(
    model=llm,
    markdown= True,
    instructions=SYSTEM_PROMPT
)

def ask_note_agent(question: str, note_text: str) -> str:
    prompt = f"""
NOTES:
{note_text}

QUESTION:
{question}
"""
    response = agent.run(prompt)
    
    return response.content

    
