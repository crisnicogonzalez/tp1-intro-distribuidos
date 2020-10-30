# TP N ◦ 1: App Layer

**Requerimientos para correr la aplicación**
* Python 3.6
* pip

**Pasos para  iniciar la aplicación**

* pip install -r requirements.txt -> instala todas las dependencias necesarias.

**Scrips**
* tp_ping.py : Se encarga de iniciar un client
* tp_ping_srv.py: Se encarga de inicializar un servidor
* constants.py: aqui se guardan las constantes que vamos a usar
* direct_ping.py: Implementa el direct ping del lado del cliente
* direct_ping_srv.py: Implementa el direct ping del lado del servidor
* reverse_ping.py: Implementa el reverse ping del lado del cliente
* reverse_ping_srv.py: Implementa el reverse ping del lado del servidor
* proxy_ping.py: Implementa el proxy ping del lado del cliente
* proxy_ping_srv.py: Implementa el proxy ping del lado del servidor
* payload_builder.py: guarda las funciones que usamos para crear y parsear los mensajes que intercambian cliente y servidor
* socket_client.py: tiene algunas de las funciones que el cliente y el servidor usan para mandar mensajes.

**Pasos para ejecutar el direct ping**

1) Levantar el servidor con el siguiente comando:

    python tp_ping_srv.py -P [puerto] -H [IP]

si los campos IP o puerto no son ingresados entonces por defecto se levanta el server con
la IP 127.0.0.1 y el puerto 8080 por defecto

2) Levantar el cliente para hacer direct ping:

    python tp_ping.py -s [IP:puerto] -p -c [count]

Consideraciones:
 +) No es necesario ingresar la opción "p" para ejecutar el direct ping, por defecto si ninguna
de las opciones de tipos de ping se ingresan se toma como direct ping por defecto.

 +) Si no se ingresa el valor de count por defecto el valor tomado es 10

 +) Si el valor de ip y puerto del servidor no se ingresan por defecto se toma el valor 127.0.0.1 y 8080 para ip y puerto respectivamente.

**Pasos para ejecutar el reverse ping**

1) Al igual que el direct ping levantar un servidor con el comando:

    python tp_ping_srv.py -P [puerto] -H [IP]


2) Levantar el cliente para hacer reverse ping:

    python tp_ping.py -s [IP:puerto] -r -c [count]

Consideraciones:
 +) En este caso es necesario especificar el tipo de ping con la opción "-r" o "--reverse".

 +) Si no se ingresa el valor de count por defecto el valor tomado es 10

 +) Si el valor de ip y puerto del servidor no se ingresan por defecto se toma el valor 127.0.0.1 y 8080 para ip y puerto respectivamente.

**Pasos para ejecutar el Proxy ping**

1) Al igual que el direct y reverse ping levantar un servidor con el comando:

    python tp_ping_srv.py -P [puerto] -H [IP]

2) Levantar otro servidor con el mismo comando que el caso 1 pero con ip y puerto distinto


3) Levantar el cliente para hacer proxy ping:

    python tp_ping.py -s [IP:puerto] -x -c [count] -d [ipDest:portDest]

Consideraciones:
 +) En este caso es necesario especificar el tipo de ping con la opcion "-x" o "--proxy", tambien es necesario incluir la opcion -d y un valor para consultar el servidor destino, si esto no pasa el cliente se cierra

 +) Si no se ingresa el valor de count por defecto el valor tomado es 10

 +) Si el valor de ip y puerto del servidor no se ingresan por defecto se toma el valor 127.0.0.1 y 8080 para ip y puerto respectivamente.

**Opciones quiet, verbose y help**:

Tanto cliente como servidor tienen implementadas las opciones verbose y help.

Help: muestra el mensaje de ayuda. Se activa si se agrega "-h" o "--help" a cualquiera de los comandos antes dichos.

Verbose: Con esta opción el cliente y el servidor muestran más información acerca de cuándo reciben y mandan mensajes.  Se activa si se agrega "-v" o "--verbose" a cualquiera de los comandos antes dichos.

Quiet: esta implementada solamente en el cliente. Con esta la lista de secuencia de paquetes y el rtt de cada ping y pong no se muestra, la única información que mostramos es ip de cliente y servidor y estadísticas.

