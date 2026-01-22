from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from models import CustomerFeedback


class BuyBuyAnalyzer:
    def __init__(self, api_key: str):
        self.llm = ChatNVIDIA(
            model="meta/llama-3.1-8b-instruct",
            api_key=api_key,
            temperature=0,
        )
        self.parser = PydanticOutputParser(
            pydantic_object=CustomerFeedback
        )
        self._prompt = self._create_prompt()
        self.chain = self._prompt | self.llm | self.parser

    def _create_prompt(self):
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Tu es un analyste retail expert. "
                    "Réponds UNIQUEMENT en JSON.",
                ),
                (
                    "user",
                    "Analyse cet email client: {email}\n\n"
                    "{format_instructions}",
                ),
            ]
        )

    def process_email(self, email_text: str) -> CustomerFeedback:
        """Invoke the LangChain pipeline for a single email."""
        return self.chain.invoke(
            {
                "email": email_text,
                "format_instructions": (
                    self.parser.get_format_instructions()
                ),
            }
        )
