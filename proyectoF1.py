#!/usr/bin/python3

import json, requests #Importo el módulo para trabajar con JSON y el módulo requests para hacer peticiones a APIs online.

def pruebaApi(estado): #La respuesta 200 es el OK de la API, otro número sería un error en la respuesta.
    if estado == 200:
        return True
    print('Algo ha ido mal, la solicitud de datos a la API no ha funcionado, podría estar offline.')
    return False

def getConductores(temporada):
    if temporada < 1950:
        print('Demasiado atrás en el tiempo, los mundiales de Fórmula 1 comenzaron en el año 1950. Volvamos a intentarlo.')
        año = int(input('¿De qué año te interesa conocer la tabla de victorias?\n'))
        getConductores(año)
    elif temporada > 2023:
        print('Te has pasado, ¡no puedo ver el futuro! Volvamos a intentarlo.')
        año = int(input('¿De qué año te interesa conocer la tabla de victorias?\n'))
        getConductores(año)
    else:
        url = f"http://ergast.com/api/f1/{temporada}/drivers.json" #Acabo las URL con ".json" porque la API devuelve formato XML por defecto.
        peticion = requests.get(url)    #Solicitud GET a la API.
        if pruebaApi(peticion.status_code):
            datos = peticion.json()    #Guardo en "datos" todo el JSON que me da la API.
            conductores = [] #Voy a crear en conductores un diccionario con los elementos que me interesan de todo el JSON que devuelve la API.

            for conductor in datos["MRData"]["DriverTable"]["Drivers"]:    #En "conductores" guardo la parte que me interesa del JSON anterior.
                conductores.append({'id':conductor['driverId'],'nombre':conductor['givenName'],'apellidos':conductor['familyName']})
            return conductores

def getVictorias(conductor,año):
    url = f"http://ergast.com/api/f1/{año}/drivers/{conductor}/results.json" #Este link de la api me devuelve la posición del piloto en todas las carreras de ese año.
    peticion = requests.get(url)
    if pruebaApi(peticion.status_code):
        datos = peticion.json()
        posiciones = [] #En esta lista guardaré todas las posiciones en las que ha quedado, luego contaré el número de veces que sale el 1.
        for carrera in datos['MRData']['RaceTable']['Races']:
            posicion = carrera['Results'][0]['position']
            posiciones.append(posicion)
        victorias = 0
        for posicion in posiciones:
            if posicion == '1':
                victorias+=1
        return victorias
    
def numVictorias(conductor):
    return conductor['Victorias']


print('Bienvenido al contador de victorias de Fórmula 1.')
año = int(input('¿De qué año te interesa conocer la tabla de victorias?\n'))
conductoresDelAño = getConductores(año)

#getWins('alonso',2008) Probé con alonso 2020 y fue el mayor problema!!

conductoresVictorias =  [] #Diccionario donde meteré nombre y apellidos de los conductores, y su número de victorias.
for conductor in conductoresDelAño:
    conductoresVictorias.append({'Nombre':conductor['nombre'],'Apellidos':conductor['apellidos'],'Victorias':getVictorias(conductor['id'],año)})

#Aquí ya tengo conductores y victorias de los mismos, ahora reordeno el diccionario utilizando como clave de ordenación el campo victorias:

conductoresVictorias.sort(key=numVictorias, reverse=True) #Sort necesita una función como key, no le sirve poner key='Victorias'. Reverse porque quiero de más victorias a menos. Ya ordenados por número de victorias, saco por pantalla la tabla de victorias:

#print('Nombre:\t|\tApellidos:\t|\tNúmero de victorias:')
cabecera = {'Nombre':'Nombre:','Apellidos':'Apellidos:','Victorias':'Victorias:'}
conductoresVictorias.insert(0,cabecera) #Añado al principio de la lista la cabecera.
for conductor in conductoresVictorias:
    nombreFinal = conductor['Nombre'].ljust(15) #Ajusta a la izquierda (20 caracteres).
    apellidosFinal = conductor['Apellidos'].ljust(20)
    victoriasFinal = str(conductor['Victorias']).ljust(20) #Hago casting del número de victorias a string para poder aplicar ljust.

    print(f"{nombreFinal}\t|\t{apellidosFinal}\t|\t{victoriasFinal}")
    print('')