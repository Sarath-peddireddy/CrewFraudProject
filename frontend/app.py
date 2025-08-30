# frontend/app.py
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8001/predict"

# Page config
st.set_page_config(page_title="Fraud Investigation Crew", layout="wide")
st.title("Fraud Investigation Crew")
st.markdown("---")

st.write("### Enter Transaction Details:")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    distance_from_home = st.number_input("Distance from Home (km)", min_value=0.0, value=10.0, step=0.1)
    distance_from_last_transaction = st.number_input("Distance from Last Transaction (km)", min_value=0.0, value=1.0, step=0.1)
    ratio_to_median_purchase_price = st.number_input("Ratio to Median Purchase Price", min_value=0.0, value=1.0, step=0.1)

with col2:
    repeat_retailer = st.selectbox("Repeat Retailer", [0, 1])
    used_chip = st.selectbox("Used Chip", [0, 1])
    used_pin_number = st.selectbox("Used PIN Number", [0, 1])
    online_order = st.selectbox("Online Order", [0, 1])

# Collect features
features = {
    "distance_from_home": distance_from_home,
    "distance_from_last_transaction": distance_from_last_transaction,
    "ratio_to_median_purchase_price": ratio_to_median_purchase_price,
    "repeat_retailer": repeat_retailer,
    "used_chip": used_chip,
    "used_pin_number": used_pin_number,
    "online_order": online_order,
}

# Prediction button
if st.button("Run Fraud Prediction"):
    with st.spinner("Analyzing transaction..."):
        response = requests.post(BACKEND_URL, json=features)

        if response.status_code == 200:
            result = response.json()

            if "prediction" in result:
                st.markdown("### Prediction Result")
                
                # Create card-like container
                if result["prediction"] == 1:
                    st.markdown(
                        f"""
                        <div style="padding:15px; border-radius:10px; background-color:#ffe6e6; border:1px solid #cc0000;">
                            <h4 style="color:#cc0000;">🚨 Fraud Detected</h4>
                            <p><b>Prediction:</b> Fraudulent Transaction</p>
                            <p><b>Probability:</b> {result.get("probability", "N/A"):.2f}</p>
                            <p><b>Report:</b><br>{result.get("report", "No detailed report available.")}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div style="padding:15px; border-radius:10px; background-color:#e6ffe6; border:1px solid #009900;">
                            <h4 style="color:#009900;">✅ Normal Transaction</h4>
                            <p><b>Prediction:</b> Normal</p>
                            <p><b>Probability:</b> {result.get("probability", "N/A"):.2f}</p>
                            <p><b>Report:</b><br>{result.get("report", "No detailed report available.")}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.error(f"Backend Error: {result.get('error', 'Unknown error')}")
        else:
            st.error(f"Request failed: {response.text}")
