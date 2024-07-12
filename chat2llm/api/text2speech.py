import asyncio
import io
import edge_tts
import tempfile
from pydub import AudioSegment
from pydub.playback import play


class TTS:
    @classmethod
    def text_to_speech_async(cls, text, voice: str = "zh-CN-YunxiaNeural") -> None:
        """使用edge-tts模型进行文字转语音"""
        communicate = edge_tts.Communicate(text, voice)

        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file_path = temp_file.name
        communicate.save_sync(temp_file_path)

        return temp_file_path

    @classmethod
    async def tts_stream(cls, text, voice: str = "zh-CN-YunxiaNeural"):
        """使用edge-tts模型进行文字转语音"""
        audio_data = b""  # 重置音频数据
        communicate = edge_tts.Communicate(text, voice)
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                 audio_data += chunk["data"]
            elif chunk["type"] == "WordBoundary":
                    print(f"WordBoundary: {chunk}")
            # 当累积了足够的音频数据时,处理并播放
            if len(audio_data) > 32000:  # 可以根据需要调整这个阈值
                audio_segment = AudioSegment.from_wav(io.BytesIO(audio_data))
                play(audio_segment)
        # 处理剩余的音频数据
        if audio_data:
            audio_segment = AudioSegment.from_wav(io.BytesIO(audio_data))
            play(audio_segment)


text = """
张云是一名别墅设计师，在业内颇有名气，找他设计房子的人络绎不绝。

　　晚上，他待在房间里加班。正当他缓慢地敲打着键盘的时候，一阵风吹起了帘子，屋里的灯突然之间熄灭了。

　　停电了？张云找来蜡烛扑灭。

　　微弱的烛火飘忽摇曳，在地上拖出一个长长的陌生影子。

　　他抬起头，倒吸一口凉气：房间内不知什么时候多出了一个家伙，面白如纸，双脚离地，一双眼睛瞳内浑浊不堪，死气沉沉。

　　张云镇静下来，壮着胆子问：鬼大哥，你找小弟有事吗？

　　对方马上笑了：你是这一带最卓异的设计师，我找你当然是帮我设计房子了。
"""
async def main(text):
    text = text
    await TTS.tts_stream(text)

asyncio.run(main(text))