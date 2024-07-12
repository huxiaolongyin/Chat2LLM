from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class Get_Prompt:
    _prompt = "chat2llm/prompts/ai_assistant.txt"

    @classmethod
    def get_prompt(cls):
        """获取提示词"""
        with open(cls._prompt, "r", encoding="utf-8") as f:
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system",f.read()),
                    ("human", "检索文档: \n\n {document} \n\n 用户问题: {question}"),
                    # MessagesPlaceholder(variable_name="question"),
                ]
            )
        return prompt
    

# print(Get_Prompt.get_prompt())