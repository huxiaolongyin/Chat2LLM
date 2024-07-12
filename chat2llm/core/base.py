from langchain_core.messages import HumanMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


class BaseGenerator:
    """ """

    @staticmethod
    def generate(
        model,
        prompt,
        retriever,
        question,
        config,
        stream: bool = False,
        *args,
        **kwargs,
    ):
        """传入模型, 提示词, 问题, 会话id, 生成回答"""

        # 将检索索引器和输入内容（问题）生成检索
        setup_and_retrieval = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        )
        # 生成输出解析器
        output_parser = StrOutputParser()
        # 建立增强链
        chain = setup_and_retrieval | prompt | model | output_parser

        # 上下文管理
        def get_session_history(user_id, session_id: str) -> BaseChatMessageHistory:
            return SQLChatMessageHistory(
                f"{user_id}_{session_id}",
                connection="sqlite:///chat2llm/messages/messages.db",
            )

        with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="question",
            # history_messages_key="history",
            history_factory_config=[
                ConfigurableFieldSpec(
                    id="user_id",
                    annotation=str,
                    name="用户ID",
                    description="用户ID",
                    default="",
                    is_shared=True,
                ),
                ConfigurableFieldSpec(
                    id="session_id",
                    annotation=str,
                    name="会话ID",
                    description="会话ID",
                    default="",
                    is_shared=True,
                ),
            ],
        )

        return with_message_history.invoke(
            {"question": question, "document": relevant_data},
            config=config,
        ).content
