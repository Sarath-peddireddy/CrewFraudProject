from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from agents.transaction_analyzer import transaction_analyzer
from agents.geo_agent import geo_agent
from agents.profile_consistency import profile_consistency
from agents.fraud_investigator import fraud_investigator
from crewai import Crew, Task


model = joblib.load("models/fraud_model.pkl")


app = FastAPI(title="Fraud Investigation Crew API")


class Transaction(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price: float
    repeat_retailer: int
    used_chip: int
    used_pin_number: int
    online_order: int


@app.post("/predict")
async def predict_transaction(tx: Transaction):
    try:
        
        features = [
            tx.distance_from_home,
            tx.distance_from_last_transaction,
            tx.ratio_to_median_purchase_price,
            tx.repeat_retailer,
            tx.used_chip,
            tx.used_pin_number,
            tx.online_order
        ]
        X = np.array(features).reshape(1, -1)

    
        pred = model.predict(X)[0]            
        prob = model.predict_proba(X)[0][1]     
        
        transaction_task = Task(
            description=f"Transaction features: {features}. Check for fraud indicators.",
            expected_output="Return 1 if fraud, 0 if normal, with reasoning",
            agent=transaction_analyzer
        )

        geo_task = Task(
            description="Check anomalies based on location/time differences.",
            expected_output="Suspicious or normal",
            agent=geo_agent
        )

        profile_task = Task(
            description="Compare with user's past behavior.",
            expected_output="Consistency score and reasoning",
            agent=profile_consistency
        )

        investigator_task = Task(
            description="Combine all analyses for final fraud prediction.",
            expected_output="Final fraud prediction (0 or 1) with explanation",
            agent=fraud_investigator
        )

  
        crew = Crew(
            agents=[transaction_analyzer, geo_agent, profile_consistency, fraud_investigator],
            tasks=[transaction_task, geo_task, profile_task, investigator_task],
            verbose=True
        )
        report = crew.kickoff()

        return {
            "prediction": int(pred),
            "probability": float(prob),
            "report": str(report)
        }

    except Exception as e:
        return {"error": str(e)}
