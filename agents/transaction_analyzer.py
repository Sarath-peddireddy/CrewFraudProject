from crewai import Agent
from config.settings import settings

transaction_analyzer = Agent(
    role="Transaction Analyzer",
    goal="Detect unusual transaction patterns such as abnormal frequency, amount, or timing",
    backstory=(
        "You are responsible for reviewing transaction data"
        "to spot anamolies that may indicate fraud"
    ),
    verbose=True,
    llm="openai/gpt-3.5-turbo"
)