from langchain_openai import ChatOpenAI
from langchain_community.llms import Baichuan, ChatGLM
from langchain_community.llms import QianfanLLMEndpoint
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

class LLMs:
    def __init__(self, model_name, temprature=0.1):
        self.model_name = model_name
        self.temprature = temprature

    def get_llm(self):
        if self.model_name == "gpt-4":
            llm = ChatOpenAI(
                model_name="gpt-4",
                openai_api_key=os.environ["OPENAI_API_KEY"],
                streaming=False,
                temperature=self.temprature
            )
            return llm
        if self.model_name == "gpt-3.5-turbo-0125":
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo-0125",
                openai_api_key=os.environ["OPENAI_API_KEY"],
                streaming=False,
                temperature=self.temprature
            )
            return llm
        elif self.model_name == "mistral":
            llm = Ollama(model="mistral")
            return llm
        elif self.model_name == "gemma":
            llm = Ollama(model="gemma:2b")
            return llm



# llm = LLMs(model_name="gpt-4").get_llm()
# print(llm.model)
