from langchain_community.chat_models.ollama import ChatOllama


class Ollama:
    _base_url = "http://192.168.30.66:11434"
    _model = "llama3"

    @classmethod
    def model(cls):
        """获取模型"""
        model = ChatOllama(base_url=cls._base_url, model=cls._model)
        return model
