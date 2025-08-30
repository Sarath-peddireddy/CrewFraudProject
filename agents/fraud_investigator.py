from crewai import Agent

fraud_investigator =Agent(
    role='Fraud investigation',
    goal='Aggregate reports from others agents and assign a fraud risk score',
    backstory=(
        "You consolidate all agent findings and generate a Suspicious Activity Report "
        "with a final fraud risk score (0-100) and reasoning."
    ),
    verbose=True,
    llm='openai/gpt-3.5-turbo'
)