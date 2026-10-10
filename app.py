from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

app = FastAPI(title="Liquor Production Forecast API")

# Mount static directory for images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates directory
templates = Jinja2Templates(directory="templates")

# Load model
model = joblib.load("catboost_model.pkl")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/")
def predict_from_form(
    request: Request,
    price: float = Form(...),
    lag1: float = Form(...),
    roll3: float = Form(...),
    week: int = Form(...)
):
    input_df = pd.DataFrame([[price, lag1, roll3, week]], 
                            columns=["Liquor_Retail_Price", "volume_lag_1", "volume_roll_mean_3", "week_of_year"])
    prediction = model.predict(input_df)[0]
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "request": request, 
            "prediction": round(float(prediction), 2),
            "price": price,
            "week": week
        }
    )