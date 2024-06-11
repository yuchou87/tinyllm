from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable, ConfigurableField, ConfigurableFieldSingleOption
from langchain_groq import ChatGroq

from settings import settings


class GroqModel:
    default_model = "llama3-8b-8192"
    llama_large_model = "llama3-70b-8192"
    mixtral_model = "mixtral-8x7b-32768"
    gemma_model = "gemma-7b-it"


options = {
    GroqModel.default_model: GroqModel.default_model,
    GroqModel.llama_large_model: GroqModel.llama_large_model,
    GroqModel.mixtral_model: GroqModel.mixtral_model,
    GroqModel.gemma_model: GroqModel.gemma_model
}


class GroqProvider(object):

    def __init__(self, model: str = GroqModel.default_model):
        self.llm = ChatGroq(model_name=model, groq_api_key=settings.GROQ_API_KEY).configurable_fields(
            temperature=ConfigurableField(
                id="llm_temperature",
                name="LLM Temperature",
                description="The temperature of the LLM",
            ),
            model_name=ConfigurableFieldSingleOption(
                id="model",
                name="model for use",
                description="The model for use",
                options=options,
                default=GroqModel.default_model
            )
        )

    def base_chain(self) -> RunnableSerializable[dict, BaseMessage]:
        system = "You are a helpful assistant."
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        return prompt | self.llm