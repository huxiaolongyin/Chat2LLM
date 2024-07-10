from chat2llm.embedding.base import BaseEmbedding
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

class BertEmbedding(BaseEmbedding):
    def __init__(self):
        self._model_name = "D:/code/BigModel/bert-base-chinese"
        _device = "cpu"
        self._model_kwargs = {"device": _device}
        self._encode_kwargs = {"normalize_embeddings": True}


    def load_web(self, url, classes: list):
        return super().load_web(url, classes)

    def vectorstore(self, docs):
        hf = HuggingFaceBgeEmbeddings(
            model_name=self._model_name,
            model_kwargs=self._model_kwargs,
            encode_kwargs=self._encode_kwargs,
        )
        return super().vectorstore(docs, hf)


    def load_vectorstore(self):
        hf = HuggingFaceBgeEmbeddings(
            model_name=self._model_name,
            model_kwargs=self._model_kwargs,
            encode_kwargs=self._encode_kwargs,
        )
        return super().load_vectorstore(hf)