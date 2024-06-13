from langchain_core.runnables import ConfigurableField
from langchain_google_genai import ChatGoogleGenerativeAI

from providers.base import BaseProvider
from settings import settings


class GoogleModel:
    default_model = "gemini-1.5-pro-001"
    version_model = "gemini-1.0-pro-vision-001"


options = {
    GoogleModel.default_model: GoogleModel.default_model,
    GoogleModel.version_model: GoogleModel.version_model,
}


class GoogleProvider(BaseProvider):

    def __init__(self, model: str = GoogleModel.default_model):
        super().__init__(model)
        self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=settings.GOOGLE_API_KEY).configurable_fields(
            temperature=ConfigurableField(
                id="llm_temperature",
                name="LLM Temperature",
                description="The temperature of the LLM",
            )
        )
