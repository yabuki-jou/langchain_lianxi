
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)
DEEPSEEK_API_KEY= os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL= os.getenv("DEEPSEEK_BASE_URL")
llmOpenai = init_chat_model(
    model="deepseek:deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    temperature=0
)
for i in range(3):
    response = llmOpenai.invoke("写一个十个字的小说大纲")
    print(response.content)