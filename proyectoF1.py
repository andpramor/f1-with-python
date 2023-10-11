#!/usr/bin/python3

import json, requests    #Importo el módulo para trabajar con JSON y el módulo para hacer peticiones a APIs online.

url = "http://ergast.com/api/f1/2022/drivers.json"    #Acabo las URL con ".json" porque la API devuelve formato XML por defecto.

peticion = requests.get(url)    #Solicitud GET a la API.

if peticion.status_code == 200:    #La respuesta 200 es el OK, otro número sería un error en la respuesta de la API.
    datos = peticion.json()    #Guardo en "datos" todo el JSON que me da la API.

    conductores = []

    for conductor in datos["MRData"]["DriverTable"]["Drivers"]:    #En "conductores" guardo la parte que me interesa del JSON anterior.
        conductores.append({'id':conductor['driverId'],'nombre':conductor['givenName'],'apellidos':conductor['familyName']})
    #Pruebo a mostrar el diccionario que acabo de crear:
    print('Prueba de impresión del diccionario en el que guardo nombre, apellidos e id de los pilotos:')
    print(conductores)
else:
    print("La solicitud GET no ha funcionado. API inalcanzable.")

# IDEAS:
# Juego de preguntas: ¿Cuántas carreras ha ganado en el año 2022 el piloto aleatorio que te dé? Te saco un nombre completo por pantalla y te pregunto, tú como usuario respondes, y yo compruebo.
# Al principio, se pide número de jugadores y el nombre de cada jugador. Se hacen tres preguntas por jugador. Al final, sacar las respuestas de cada jugador y las correctas.
# Puedo montarme mi propio JSON recorriendo todas las carreras del año, y anotando en cada piloto el número de victorias.
# Sacar un pdf con los resultados, respuestas de cada jugador, y tabla con los pilotos que hayan ganado alguna carrera en 2022, junto con el número de carreras que hayan ganado, ordenados de más a menos victorias.