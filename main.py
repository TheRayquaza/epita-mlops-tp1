from fastapi import FastAPI
import joblib
import train_model
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import numpy as np
import uvicorn
import os

app = FastAPI()
model = joblib.load(os.getenv("MODEL_PATH"))

class PredictData(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.post("/predict")
async def predict(data: PredictData):
    input_array = np.array(list(data.dict().values())).reshape(1, -1)
    pred = model.predict(input_array)
    return {"prediction": float(pred[0])}

@app.get("/redirect")
async def redirect_to_youtube():
    return RedirectResponse("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == "__main__":
    uvicorn.run("main:app", port=int(os.getenv('PORT')), host=str(os.getenv('HOST')), log_level="info")
