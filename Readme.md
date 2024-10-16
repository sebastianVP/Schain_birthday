# REPOSITORIO SCHAIN PRUEBAS AMISR-14


Notas de desarrollo:
---

* La carpeta superior se llama **BIRTHDAY**
* cd BIRTHDAY
* Esta carpeta contiene el repositorio Schain_birthday y el entorno virtual schain_amisr
* Estamos creando el entorno virtual schain_amisr, para activarlo usamos el siguiente comando:

	 source schain_master/bin/activate

* Link del repositorio de [schain](http://intranet.igp.gob.pe:8082/schain)
* Nos ubicamos en el directorio BIRTHDAY

Escribimos los siguientes pasos:

* $ git clone http://intranet.igp.gob.pe:8082/schain
* La carpeta que contiene el software Signal Chain se llama schain
* $ git status
* $ git checkout master_tmp
* $ git status
* $ git log

Recordemos el directorio.

* $ tree
 BIRTHDAY
  - Schain_birthday: Notas
  - schain_amisr: Entorno virtual
  - schain: Librerias schain con repositorio de amis-14, el nombre es master_tmp

Estamos haciendo todo este repaso y trabajo con el entorno **emulado de Ubuntu**.

 * Directorio del Readme: 

	/home/soporte/BIRTHDAY/Schain_birthday  

 * La ruta de datos es la siguiente:

	/mnt/c/Users/soporte/Downloads/2024/20240822.002

Para utilizar el vscode desde windows, debemos abrir una carpeta con la siguiente direccion:

	\\wsl.localhost\Ubuntu-20.04\home\soporte\BIRTHDAY


Los entornos virtuales en esta carpeta se llama:
 - schain_amisr
 - schain_sophy


En el repositorio de pruebas tenemos 2 scripts de referencia: tw_procesamiento.py y el mlt_2022_03.py, estos scripts
dan origen al archivo de prueba:

- winds_amisr.py

# **CONEXION FTP**

Para conectar mediante FTP con Windows, simplemente necesitaremos los datos de conexión FTP al servidor. Al realizarlo directamente desde Windows, no necesitamos ningún software adicional, lo cual nos resultará muy útil cuando nos encontramos en un entorno de oficina con permisos restringidos.

Ubicamos la carpeta equipo:
- Click derecho Agregar una ubicacion de red.

* Server: 190.187.237.233
* user: visitor
* password: visitorJRO
* ruta: /WINDS_AMISR

# **OJO**

Queda pendiente en fecha 15/10/2024
Definir los cosenos directores en el patron de radiacion.
