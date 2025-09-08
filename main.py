from fastapi import FastAPI
import joblib
import train_model
from pydantic import BaseModel
import numpy as np

app = FastAPI()
model = joblib.load("regression.joblib")

class PredictData(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.post("/predict")
async def predict(data: PredictData):
    input_array = np.array(list(data.dict().values())).reshape(1, -1)
    pred = model.predict(input_array)
    return {"prediction": float(pred[0])}
