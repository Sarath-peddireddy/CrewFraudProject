from crewai import Agent
geo_agent = Agent(
    role='Geo Location Checker',
    goal='Flag Suspicious location mismatches in transactions',
    backstory=(
        "you check if transactions occur from different countries/locations"
        "in an impossible timeframe, indicating fraud"
    ),
    verbose=True,
    llm='openai/gpt-3.5-turbo'
)