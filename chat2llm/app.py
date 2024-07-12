import os
from chat2llm.core.base import BaseGenerator
from chat2llm.llms.ollama import Ollama
from chat2llm.prompts.base import Get_Prompt
from langchain_core.output_parsers import StrOutputParser
from chat2llm.retriever.base import RetrieverBase


def main(question):
    model = Ollama.model()
    prompt = Get_Prompt.get_prompt()
    config = {"configurable": {"user_id": "用户1", "session_id": "1231245"}}
    relevant_data = RetrieverBase.retriever(question)
    return BaseGenerator.generate(model, prompt, relevant_data, question, config)


if __name__ == "__main__":
    question = "肖申克的救赎的剧情简介"
    print(main(question))