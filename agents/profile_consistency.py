from crewai import Agent
profile_consistency =Agent(
    role="profile Consistency Agent",
    goal="Compare transactions with historical customer behaviour patterns",
    backstory=(
        "You ensure the transaction matches the customer's usual spending profile, "
        "flagging deviations such as high-value luxury purchases."
    ),
    verbose=True,
    llm='openai/gpt-3.5-turbo'
)