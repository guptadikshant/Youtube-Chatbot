from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from prompt_templates import TEMPLATE


def get_model_output(video_transcript: str, question: str) -> str:
    groq_llm = ChatGroq(temperature=0, model="llama-3.1-70b-versatile")

    prompt_template = ChatPromptTemplate.from_messages(TEMPLATE)

    chain = (
            prompt_template
            | groq_llm
            | StrOutputParser()
    )

    return chain.invoke({"transcript": video_transcript, "query": question})
