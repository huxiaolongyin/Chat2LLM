import whisper
import zhconv


class Speech2Text:

    @classmethod
    def speach_to_text(audio):
        """使用whisper模型进行语音转文字"""
        model = whisper.load_model("small", device="cpu")
        result = model.transcribe(audio)
        return zhconv.convert(result["text"], "zh-cn")  # 繁体转简体
