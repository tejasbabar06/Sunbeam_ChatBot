from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os


def get_answer(context: str, question: str) -> str:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    messages = [
        SystemMessage(
            content=(
                "You are a Sunbeam AI assistant. "
                "Answer ONLY using the given context. "
                "If the answer is not present, say you don't know."
            )
        ),
        HumanMessage(
            content=f"Context:\n{context}\n\nQuestion:\n{question}"
        )
    ]

    response = llm.invoke(messages)   # ✅ correct call

    return response.content
