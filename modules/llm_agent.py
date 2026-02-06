from langchain_groq import ChatGroq
from langchain.agents import create_agent
from config.settings import LLM_MODEL
import os

def get_answer(context, question):
    llm = ChatGroq(
        model=LLM_MODEL,
        api_key=os.getenv("GROQ_API_KEY")
    )

    agent = create_agent(
        tools=[],
        model=llm,
        system_prompt=f"""
You are a Sunbeam website assistant.

Rules:
- Answer ONLY from context
- If any greeting message reply "I can serve you on Sunbeam website. Ask any question" and don't give any other information.
- If you can't answer reply - "Sorry! I don't Know, Please ask another question" and don't give any other information.
- Point-wise answers
- No hallucination
- If any batches related question give answer in table format
- Be clear and concise
- If any heading or title bold or highlight it
- Add bullets when possible

CONTEXT:
{context}

QUESTION:
{question}
"""
    )

    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })

    return result["messages"][-1].content
