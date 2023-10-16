#!/usr/bin/python3

import json, requests, random    #Importo el módulo para trabajar con JSON, el módulo requests para hacer peticiones a APIs online y random para generar números aleatorios, que usaré para elegir el año de cada ronda del juego.

temporada = random.randint(1950, 2022) #Los mundiales empezaron en 1950, la API puede devolver información desde su inicio, así que elegiré el año entre ese y el pasado, de forma que sea el año que sea, la temporada esté completa.

url = f"http://ergast.com/api/f1/{temporada}/drivers.json"    #Acabo las URL con ".json" porque la API devuelve formato XML por defecto.

peticion = requests.get(url)    #Solicitud GET a la API.

if peticion.status_code == 200:    #La respuesta 200 es el OK, otro número sería un error en la respuesta de la API.

    print(f'El año elegido por el aleatorio ha sido {temporada}')
    
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
# Juego de preguntas: Dos jugadores, tres rondas. Cada ronda, un año aleatorio para cada jugador, se dice el número de carreras del año, el número de pilotos, y se saca cada piloto preguntando el número de victorias. Al final, se saca una lista con los pilotos, la guess del usuario y el número real de vicotorias. Se cuentan los aciertos y se decide el ganador. +3 ronda ganada, +1 a ambos en caso de empate.
# Puedo montarme mi propio JSON recorriendo todas las carreras del año, y anotando en cada piloto el número de victorias.
# Jodido que a esto me de tiempo, Sacar un pdf con los resultados, respuestas de cada jugador, y tabla con los pilotos que hayan ganado alguna carrera en 2022, junto con el número de carreras que hayan ganado, ordenados de más a menos victorias.