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
    # imprimimos todos los datos leidos
    print(data.head())
    # regresamos como respuesta una tabla con los datos
    return {"message": f"main page {data}"}


@app.get("/filtro")
async def root(filter : str = {"neighbourhood":"Miguel Hidalgo"}):
    filter = json.loads(filter)
    # cargamos los datos desde el archivo airbnb.csv
    data = pandas.read_csv("airbnb.csv")

    # realizamos el filtrado de datos de acuerdo al tipo de dato que solicitamos y dato especifico de busqueda

    filtrados = data[data[list(filter.keys())[0]] == filter.get(str(list(filter.keys())[0]),"no existe el dato")]
    #print(type(data),type(filtrados))
    #print(filter.keys())
    #si el dato que pedimos no se encuentra en la informacion nos imprime "no existe el dato"
    print(filter.get(str(list(filter.keys())[0]),"no existe el dato"))
    #print(data.head(3))
    #imprimimos los datos encontrados
    print(filtrados)
    print(len(filtrados), "elementos")
    #enviamos respuesta a la peticion
    return {"message": f"filter page {filtrados}"}

@app.get("/rooms")
async def root():
    #cargamos los datos del archivo "airbnb.csv"
    data = pandas.read_csv("airbnb.csv")
    #agrupamos los datos por "neighbourhood" y sumamos el "calculated_host_listings_count" de cada grupo
    rooms = data[["neighbourhood", "calculated_host_listings_count"]].groupby("neighbourhood").sum()
    #imprimimos los grupos filtrados y su resultado de la suma
    print(rooms)
    #enviamos respuesta a la peticion
    return {"message": f"rooms page {rooms}"}

@app.get("/meancost")
async def root():
    #cargamos los datos desde el archivo "airbnb.csv"
    data = pandas.read_csv("airbnb.csv")
    # agrupamos por "neighbourhood" y calculamos el precio promedio de cada grupo
    mean_cost = data[["neighbourhood", "price"]].groupby("neighbourhood").mean()
    #imprimimos el promedio de cada grupo
    print("Promedio por delegacion", mean_cost)
    #enviamos respuesta a la peticion
    return {"message": f"meancost page {mean_cost}"}


@app.get("/meancostdate")
async def root(date_min_str : str = "2016-12-24", date_max_str : str = "2017-5-16"):
    #cargamos datos desde el archivo "airbnb.csv"
    data = pandas.read_csv("airbnb.csv", parse_dates = ["last_review"])
    #convertimos la fecha introducida en tipo datetime
    date_min = datetime.strptime(date_min_str, "%Y-%m-%d")
    date_max = datetime.strptime(date_max_str, "%Y-%m-%d")
    # filtramos los datos quedandonos solo los mayores o iguales a la fecha minima
    data2 = data[data["last_review"] >= date_min]
    # filtramos los datos quedandonos solo los menores  o iguales a la fecha maxima 
    data3 = data2[data2["last_review"] <= date_max]
    # calculamos el promedio del precio de alojo dentro de estas fechas
    mean_cost = data3[["last_review", "price"]].mean()
    #imprimimos solo el costo promedio
    print("costo promedio", mean_cost)
    #enviamos respuesta a la peticion
    return {"message": f"meancost filter by date page {mean_cost}"}


@app.get("/average")
async def root():
    # cargamos los datos desde el archivo "airbnb.csv"
    data = pandas.read_csv("airbnb.csv")
    # agrupamos los datos por "neighbourhood" calculamos el promedio de las reseñas por mes
    average = data[["neighbourhood", "reviews_per_month"]].groupby("neighbourhood").mean()
    # imprimimos por grupos
    print("promedio de calificaciones por mes", average)
    # enviamos respuesta a la peticion
    return {"message": f"meancost page {average}"}


@app.get("/proposal")
async def root():

    return {"message": "aun no se"}