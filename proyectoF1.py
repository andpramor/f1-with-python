#!/usr/bin/python3

#Importamos el módulo para trabajar con JSON:
import json, requests

#ACABO TODAS LAS URL CON .JSON PORQUE LA API DEVUELVE LOS DATOS COMO XML POR DEFECTO.
#Le voy a pedir al usuario que elija un conductor, de la temporada del año pasado, de forma que no haya demasiados datos pero los datos sean de una temporada completa, para lo que le muestro todos los disponibles y cuál es su id:
url = "http://ergast.com/api/f1/2022/drivers.json"

#Ante todo, compruebo que puedo alcanzar la API haciendo la solicitud GET:
peticion = requests.get(url)
#Si el código de respuesta es 200, todo va bien, así que lo compruebo. Si va bien cojo los datos, sino, aviso del error:
if peticion.status_code == 200:
    datos = peticion.json()
    #Aquí tengo en datos todo el json. Ahora voy a meter todos los conductores y su ID en otra variable:
    conductores = datos["MRData"]["DriverTable"]["Drivers"]
    #Ahora recorro todos los datos en conductores y saco solo el nombre y el id:
    for conductor in conductores:
        id = conductor["driverId"]
        nombre = f"{conductor['givenName']} {conductor['familyName']}"
        print(f"Nombre: {nombre}, ID: {id}.\n")
else:
    print("La solicitud GET no ha funcionado. API inalcanzable.")