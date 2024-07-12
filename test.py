import asyncio
import pyaudio
import edge_tts
from pydub import AudioSegment

TEXT = "在线音频常用的在线传输方式之一是通过HTTP流。有多种流方法属于HTTP流方法的分支，包括服务器推送，这在历史上一直用于在浏览器中不断的刷新网络摄像头图像进行显示；以及一系列由Apple、Adobe和Microsoft等公司提出的新方法，用于他们各自的媒体播放应用程序。..."
VOICE = "zh-CN-YunxiaNeural"
OUTPUT_FILE = "test.mp3"


async def stream_and_play():
    communicate = edge_tts.Communicate(TEXT, VOICE)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])

    stream.stop_stream()
    stream.close()
    p.terminate()


asyncio.run(stream_and_play())
# p = pyaudio.PyAudio()
