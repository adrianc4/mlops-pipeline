# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model
model = joblib.load("src/model.pkl")


class Features(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {"message": "ML API is running"}


@app.post("/predict")
def predict(data: Features):
    prediction = model.predict([np.array(data.features)])
    target_names = ["setosa", "versicolor", "virginica"]
    print(f"Input: {data.features}, \
          Prediction: {target_names[int(prediction[0])]}")
    return {"prediction": target_names[int(prediction[0])]}
