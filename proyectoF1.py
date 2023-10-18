#!/usr/bin/python3

import json, requests #Importo el módulo para trabajar con JSON y el módulo requests para hacer peticiones a APIs online.

def tryApi(estado): #La respuesta 200 es el OK de la API, otro número sería un error en la respuesta.
    if estado == 200:
        return True
    print('Algo ha ido mal, la solicitud de datos a la API no ha funcionado, podría estar offline.')
    return False

def getDrivers(season):
    
    print('')
    if season < 1950:
        print('Demasiado atrás en el tiempo, los mundiales de Fórmula 1 comenzaron en el año 1950. Volvamos a intentarlo.')
        getDrivers()
    elif season > 2023:
        print('Te has pasado, ¡no puedo ver el futuro! Volvamos a intentarlo.')
        getDrivers()
    else:
        url = f"http://ergast.com/api/f1/{season}/drivers.json" #Acabo las URL con ".json" porque la API devuelve formato XML por defecto.
        peticion = requests.get(url)    #Solicitud GET a la API.
        if tryApi(peticion.status_code):
            datos = peticion.json()    #Guardo en "datos" todo el JSON que me da la API.
            conductores = [] #Voy a crear en conductores un diccionario con los elementos que me interesan de todo el JSON que devuelve la API.

            for conductor in datos["MRData"]["DriverTable"]["Drivers"]:    #En "conductores" guardo la parte que me interesa del JSON anterior.
                conductores.append({'id':conductor['driverId'],'nombre':conductor['givenName'],'apellidos':conductor['familyName']})
            return conductores

def getWins(conductor,año):
    url = f"http://ergast.com/api/f1/{año}/drivers/{conductor}/results.json" #Este link de la api me devuelve la posición del piloto en todas las carreras de ese año.
    peticion = requests.get(url)
    if tryApi(peticion.status_code):
        datos = peticion.json()
        posiciones = [] #En esta lista guardaré todas las posiciones en las que ha quedado, luego contaré el número de veces que sale el 1.
        for carrera in datos['MRData']['RaceTable']['Races']:
            posicion = carrera['Results'][0]['position']
            posiciones.append(posicion)
        print(f'Posiciones de {conductor}:')
        print(posiciones)

print('Bienvenido al contador de victorias de Fórmula 1.')
año = int(input('¿De qué año te interesa conocer la tabla de victorias? '))
conductoresDelAño = getDrivers(año)
# getWins('alonso',2008) Probé con alonso 2020 y fue el mayor problema.


#for conductor in conductoresDelAño: #Para cada conductor, cuento sus victorias y las meto en un diccionario, luego lo ordenaré.
#    getWins(conductor['id'],año)

#Voy a sacar la tabla de victorias como Nombre, Apellidos, Nº de victorias
#Ordenado de más victorias a menos, y cuando llegue a los pilotos sin ninguna victoria, ordenados alfabéticamente.