import uvicorn
from fastapi import FastAPI, HTTPException
from weather_data import get_weather_for_city

app = FastAPI(title="Weather Service API")

import os
DB_CONNECTION_STRING = os.environ["DB_CONNECTION_STRING"] 

@app.get("/")
async def root():
    return {"message": "Welcome to the Weather Forecasting API"}

@app.get("/weather/{city}")
async def get_weather(city: str):
    weather_data = get_weather_for_city(city)
    if not weather_data:
        raise HTTPException(status_code=404, detail=f"Weather data for {city} not found")
    return weather_data

@app.get("/health")
async def health_check():
    if DB_CONNECTION_STRING:
        return {"status": "healthy"}
    return {"status": "unhealthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)