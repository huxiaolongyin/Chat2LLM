from fastapi import FastAPI
import uvicorn
from chat2llm.api.generate import Generate
from fastapi.responses import StreamingResponse
from textcls import TextCls

app = FastAPI()



@app.post("/generate")
async def get_answer(question: str):
    """调用tasking AI生成答案"""
    return StreamingResponse(Generate.taskai(question))



def get_cls(question: str):
    """调用Bert微调模型, 进行文本分类"""
    return TextCls.htw_text_cls(question)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
