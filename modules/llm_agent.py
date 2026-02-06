from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os

def get_answer(context, question):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

    messages = [
        SystemMessage(
            content=(
                "You are a Sunbeam Institute assistant. "
                "Answer ONLY from the provided context. "
                "If the answer is not present, say: "
                "'Sorry, I don't know based on available information.'"
            )
        ),
        HumanMessage(
            content=f"Context:\n{context}\n\nQuestion:\n{question}"
        )
    ]

    response = llm(messages)
    return response.content
