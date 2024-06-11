from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable


class BaseProvider(object):
    def __init__(self, model: str):
        self.model = model
        self.llm = None

    def basic_chat_chain(self) -> RunnableSerializable[dict, BaseMessage]:
        system = "You are a helpful assistant."
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        return prompt | self.llm
