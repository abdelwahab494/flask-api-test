import streamlit as st
import requests

st.title("Test a number: Even or Odd?")

number = st.number_input("Write number here", step=1)

if st.button("Predict"):
    res = requests.post(
        "http://localhost:5000/predict",
        json={"number": number}
    )
    
    if res.status_code == 200:
        prediction = res.json()["prediction"]
        st.success(f"Result: {prediction}")
    else:
        st.error("Server Problem")
