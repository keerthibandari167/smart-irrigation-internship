import streamlit as st
import numpy as np
import joblib

model = joblib.load("Farm_Irrigation_System.pkl")

st.title("Smart Irrigation Prediction")
st.subheader("Enter sensor values (0 to 1 scale)")

inputs = []
for i in range(20):
    value = st.slider(f"Sensor {i}", 0.0, 1.0, 0.5, 0.01)
    inputs.append(value)

if st.button("Predict"):
    data = np.array(inputs).reshape(1, -1)
    output = model.predict(data)[0]

    st.markdown("### Sprinkler Status:")
    for i in range(len(output)):
        st.write(f"Sprinkler {i}: {'ON' if output[i] == 1 else 'OFF'}")

