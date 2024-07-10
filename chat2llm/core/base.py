from langchain_core.messages import HumanMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables import ConfigurableFieldSpec


class BaseLLM:
    """ """

    def __init__(self) -> None:
        pass

    def generate(
        self, model, prompt, question, config, stream: bool = False, *args, **kwargs
    ):
        """传入模型, 提示词, 问题, 会话id, 生成回答"""

        chain = prompt | model

        # 上下文管理
        def get_session_history(user_id, session_id: str) -> BaseChatMessageHistory:
            return SQLChatMessageHistory(
                f"{user_id}_{session_id}",
                connection="sqlite:///chat2llm/messages/messages.db",
            )

        with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="messages",
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
            {"messages": question},
            config=config,
        ).content
