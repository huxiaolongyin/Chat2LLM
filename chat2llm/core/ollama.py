from langchain_community.chat_models.ollama import ChatOllama
from base import BaseLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class Ollama(BaseLLM):
    def __init__(self):
        super().__init__()
        self._base_url = "http://192.168.30.66:11434"
        self._model = "llama3"
        self._prompt = "chat2llm/prompts/ai_assistant.txt"

    def gen_answer(self, question, stream: bool = False):
        # 提示词
        with open(self._prompt, "r", encoding="utf-8") as f:
            prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        f.read(),
                    ),
                    MessagesPlaceholder(variable_name="messages"),
                ]
            )
        # 处理上下文
        config = {"configurable": {"user_id": "用户1", "session_id": "1231245"}}
        model = ChatOllama(base_url=self._base_url, model=self._model)
        return self.generate(model, prompt, question, config)


model = Ollama()
# print(model.gen_answer("我名字叫bob，请记住"))
print(model.gen_answer("请问，我叫什么名字"))
