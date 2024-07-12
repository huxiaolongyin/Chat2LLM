import taskingai

class Generate:

    @classmethod
    def taskai(self, question):
        """调用taskai api回答问题"""
        api_key = "tkp1yUY4EkM1gBXLrhpTfo8E29wxwXQT"
        host = "http://127.0.0.1:8080"
        assistant_id = "X5lMiNC6y2JjPG1WU1DwyJ2M"
        chat_id = "SdELMIytescyhaMMoNWhs5Eh"
        taskingai.init(api_key=api_key, host=host)

        taskingai.assistant.create_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            text=question,
        )

        assistant_message_response = taskingai.assistant.generate_message(
            assistant_id,
            chat_id,
            stream=True,
        )

        for item in assistant_message_response:
            if hasattr(item, "delta"):
                yield item.delta
