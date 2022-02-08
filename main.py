from datetime import datetime
from time import strptime
from fastapi import FastAPI
import pandas
import json

app = FastAPI()

@app.get("/main")
async def root():

    # cargamos los datos desde el archivo airbnb.csv
    data = pandas.read_csv("airbnb.csv")
    print(data.head())
    # regresamos como respuesta una tabla con los datos
    return {"message": f"main page {data}"}


@app.get("/filtro")
async def root(filter : str = {"neighbourhood":"Miguel Hidalgo"}):
    filter = json.loads(filter)
    # cargamos los datos desde el archivo airbnb.csv
    data = pandas.read_csv("airbnb.csv")

    # realizamos el filtrado de datos

    filtrados = data[data[list(filter.keys())[0]] == filter.get(str(list(filter.keys())[0]),"no existe el dato")]
    #print(type(data),type(filtrados))
    #print(filter.keys())
    print(filter.get(str(list(filter.keys())[0]),"no existe el dato"))
    #print(data.head(3))
    print(filtrados)
    print(len(filtrados), "elementos")

    return {"message": f"filter page {filtrados}"}

@app.get("/rooms")
async def root():
    data = pandas.read_csv("airbnb.csv")
    rooms = data[["neighbourhood", "calculated_host_listings_count"]].groupby("neighbourhood").sum()
    print(rooms)
    return {"message": f"rooms page {rooms}"}

@app.get("/meancost")
async def root():
    data = pandas.read_csv("airbnb.csv")
    mean_cost = data[["neighbourhood", "price"]].groupby("neighbourhood").mean()
    print("Promedio por delegacion", mean_cost)
    return {"message": f"meancost page {mean_cost}"}


@app.get("/meancostdate")
async def root(date_min_str : str = "2016-12-24", date_max_str : str = "2017-5-16"):
    data = pandas.read_csv("airbnb.csv", parse_dates = ["last_review"])
    date_min = datetime.strptime(date_min_str, "%Y-%m-%d")
    date_max = datetime.strptime(date_max_str, "%Y-%m-%d")
    data2 = data[data["last_review"] >= date_min] 
    data3 = data2[data2["last_review"] <= date_max]
    mean_cost = data3[["last_review", "price"]].mean()
    #print(data)
    #print(data3)
    print("costo promedio", mean_cost)
    return {"message": f"meancost filter by date page {mean_cost}"}


@app.get("/average")
async def root():
    data = pandas.read_csv("airbnb.csv")
    average = data[["neighbourhood", "reviews_per_month"]].groupby("neighbourhood").mean()
    print("promedio de calificaciones por mes", average)
    return {"message": f"meancost page {average}"}


@app.get("/proposal")
async def root():

    return {"message": "aun no se"}