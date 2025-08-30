# 💳 Fraud Investigation Crew  

A Machine Learning project to detect fraudulent transactions.  
This project simulates a **fraud investigation system** where users can input transaction details via a **Streamlit frontend**, and a **FastAPI backend** predicts whether the transaction is **fraudulent or genuine**.

---

## 🚀 Tech Stack  

### 🔹 Backend
- **Python**
- **FastAPI** – for building REST API endpoints  
- **Scikit-learn** – for model training and prediction  
- **Pandas, NumPy** – for data handling  

### 🔹 Frontend
- **Streamlit** – interactive UI for entering transaction details  
- **Requests** – connecting frontend with backend  

### 🔹 Environment & Tools
- **Anaconda / Virtual Environment**
- **pipreqs** – auto-generating `requirements.txt`  
- **Git & GitHub** – version control  

---

## 📚 What I Learned  

- How to build a **Machine Learning pipeline** for fraud detection  
- Connecting **FastAPI backend** with **Streamlit frontend**  
- Working with **REST APIs** (`POST` requests to backend)  
- Structuring ML projects with **frontend, backend, and middleware**  
- Managing dependencies using `requirements.txt`  
- Improving **UI/UX** in Streamlit (column layouts, styled outputs)  

---

## ⚡ Features  

- Input transaction details (distance, retailer info, chip usage, online order, etc.)  
- Predicts whether a transaction is **Fraudulent** or **Normal**  
- Displays a **suspicious activity report**  
- Clean and structured frontend layout  

---

## 📂 Project Structure  

CreditScoreCrew/
│── backend/ # FastAPI backend with ML model
│── frontend/ # Streamlit app
│── middleware/ # (Optional) data validation, logging
│── requirements.txt
│── README.md


---

## 🎯 Usage  

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/CreditScoreCrew.git
cd CreditScoreCrew


conda create -n fraudcrew python=3.11 -y
conda activate fraudcrew
pip install -r requirements.txt

uvicorn backend.app:app --reload --port 8001

streamlit run frontend/app.py

