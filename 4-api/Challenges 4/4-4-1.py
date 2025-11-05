from fastapi import FastAPI,Query
import pandas as pd
import json
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv")
app = FastAPI()

@app.get("/api/flights/search")

def get_serah_flights(type:str = Query(), code:str = Query()):
    if type == "dep":
        flights = df[df['departure_airport_code'] == code]
    elif type == "arr": 
        flights = df[df['arrival_airport_code'] == code]
    else:
        return {}

    json_records = flights.to_json(orient ='records')
    return json.loads(json_records)
