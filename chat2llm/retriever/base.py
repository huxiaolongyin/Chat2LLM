from chat2llm.embedding.bert import BertEmbedding

class RetrieverBase:
    def retriever(self, question, similar_arg: int=1):
        vectorstore = BertEmbedding().load_vectorstore()
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": similar_arg})
        docs = retriever.invoke(question)

        return docs