#!/usr/bin/python3

#Importamos el módulo para trabajar con JSON:
import json, requests

#ACABO TODAS LAS URL CON .JSON PORQUE LA API DEVUELVE LOS DATOS COMO XML POR DEFECTO.
#Le pediré al usuario algunos datos para completar la URL con la que atacaré a la API, por ahora es un valor que doy yo para pruebas:
url = "http://ergast.com/api/f1.json"

#Hago la solicitud GET:
peticion = requests.get(url)
#Si el código de respuesta es 200, todo va bien, así que lo compruebo. Si va bien cojo los datos, sino, aviso del error:
if peticion.status_code == 200:
    datos = peticion.json()
    print(datos) #Saco por pantalla los datos del json para probar
else:
    print("La solicitud GET no ha funcionado.")