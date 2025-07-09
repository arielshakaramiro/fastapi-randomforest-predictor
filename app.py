from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Load model
with open("models/random_forest_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Definisi API
app = FastAPI()

# Data Input untuk Prediksi
class InputData(BaseModel):
    usia: int
    pendapatan: int

@app.post("/predict")
def predict(data: InputData):
    x_input = np.array([[data.usia, data.pendapatan]])
    y_output = loaded_model.predict(x_input)
    return {"prediction": int(y_output[0])}