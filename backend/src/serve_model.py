from fastapi import FastAPI
import uvicorn
from joblib import load
from pydantic import BaseModel

clf = load(r"d_tree.joblib")

def get_prediction(gender, age, bmi):
    x = [[gender, age, bmi]]
    y = clf.predict(x)[0]
    prob = clf.predict_proba(x)[0].tolist()
    return {"prediction": y}


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

class ModelParams(BaseModel):
    gender: int
    age: int
    bmi: float

@app.post("/predict")
def predict(params: ModelParams):
    pred = get_prediction(params.gender, params.age, params.bmi)
    return pred

