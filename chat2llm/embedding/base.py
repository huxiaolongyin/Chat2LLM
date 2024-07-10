import bs4
import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    @abstractmethod
    def load_web(self, url, classes: list):
        """使用bs4抓取网页内容"""

        bs4_strainer = bs4.SoupStrainer(class_=classes)
        loader = WebBaseLoader(
            web_paths=(url,),
            bs_kwargs={"parse_only": bs4_strainer},
        )
        return loader.load()

    @abstractmethod
    def vectorstore(self, docs, embedding):
        """拆分数据，然后向量化存储"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
        all_splits = text_splitter.split_documents(docs)

        Chroma.from_documents(
            all_splits,
            embedding,
            persist_directory="chat2llm/vectorstore",
        )

    # @abstractmethod
    def load_vectorstore(self, embedding):
        """加载向量存储"""
        return Chroma(
            embedding_function=embedding,
            persist_directory="chat2llm/vectorstore",
        )
