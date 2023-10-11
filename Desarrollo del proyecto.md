## Entornos virtuales
Vamos a desarrollar todo el proyecto utilizando un entorno virtual, que instalamos usando pip. El gestor de entornos virtuales que usaremos será virtualenvwrapper.
Para ello, instalamos virtualenv con pip:
![Captura: instalando virtualenv](./assets/Instalando%20virtualenv.png)

Creamos un directorio en el que guardar el entorno virtual en el que vamos a trabajar, yo usaré ~/.virtualenvs.
![Captura: creación del directorio para entornos virtuales](./assets/Creacion%20directorio%20entornos%20virtuales.png)

Instalamos virtualenvwrapper:
![Captura: instalando virtualenvwrapper](./assets/Instalando%20virtualenvwrapper.png)

Marco el directorio que creé antes como el directorio en el que deben crearse los entornos virtuales utilizando `export WORKON_HOME=~/.virtualenvs`.
Para asegurarme de que los comandos de virtualenvwrapper están disponibles siempre, añado el script que los carga a mi script .bashrc, de forma que se "activen" cada vez que inicie una sesión de terminal. Ésto se hace añadiendo al final del archivo .bashrc la línea `. /usr/local/bin/virtualenvwrapper.sh`.
![Captura: cargando los comandos de virtualenvwrapper cada vez que se inicie una sesión de terminal](./assets/Cargar%20virtualenvwrapper%20en%20bashrc.png)

Ahora creo el entorno virtual en el que voy a trabajar con la orden `mkvirtualenv nombre`, yo usaré "entornoF1":
![Captura: creando entorno virtual](./assets/Creando%20virtual%20env.png)

Entramos a trabajar en el entorno con la orden `workon entornoF1` y salimos del mismo con la orden `deactivate`.

##Python
Para atacar a la API, según su documentación, hay que utilizar un método GET y una URL que dependerá de lo que queremos pedir. Para construir la URL en nuestro programa, utilizaremos con Python las llamadas "f-strings", que utilizan la siguiente sintaxis:
`variable = f'texto_que_no_varía_{valor1}_no_varía_{valor2}`
Python interpreta ahí la cadena entre comillas simples, sustituyendo los valores entre llaves por lo que valgan las variales contenidas por las mismas. Si tenemos las dos variables valor1=1 y valor2=2, la cadena anterior sería:
`variable = "texto_que_no_varía_1_no_varía_2"`
Por ahora, conseguimos un diccionario con el id, el nombre y los apellidos de los pilotos de la temporada dada (2022):
![Captura: prueba impresión de los pilotos](./assets/Prueba%20pilotos.png)