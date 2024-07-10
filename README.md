# Chat2LLM
本项目计划开发一个 基于LLM的知识库问答系统。

能够实现
- 知识的多种类型文件导入
- 问答系统
- 语音交互
- 知识图谱建设

# 应用场景
- 作为企业的知识库
- 作为智能客服
- 硬件的智能服务

# 开发
技术栈方面
支持的Python版本：Python3.8+

- 语音识别：whisper
- 大模型：基于ollama的llama3
- 大模型交互：langchain
- 知识数据库：MongoDB(拟定)
- api服务：Fastapi
- 知识图谱：待定
- 后端系统：Django(拟定)
- 管理数据：SQLite or Mysql
- 前端：Vue(拟定)
- 语音服务：edge-tts

# 开发计划
## 实现语音交互的知识库问答服务

- [ ] 语音识别
- [ ] 与大模型交互
- [ ] 上下文处理
- [ ] 会话处理
- [ ] RAG知识库
- [ ] 实时信息的爬取

| tips：基于以上这些就可以进行硬件小助手的开发

## 管理系统
- [ ] 问答交互页面
- [ ] 知识文件导入管理


# 参考
- Fastgpt：https://github.com/labring/FastGPT
- ollama：https://github.com/ollama/ollama
- langchain：https://github.com/langchain-ai/langchain
