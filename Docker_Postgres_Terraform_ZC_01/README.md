# Docker - Terraform Module 1

Cómo saber si tienes bien instalado Docker. 
ejecular línea: ```docker run hello-world```
la primera palabra "docker" para referenciar a docker, la segunda palabra "run" para ejecutar y la tercera palabra "hello-world" para indicar la imagen.

Se pueden ejecutar imagenes de bash de ubuntu, como lo indica la imagen "hello-world", otras cosas que se pueden ejecutar es python:
```docker run -it python:3.9```
En esta ejecución docker agregamos un "-it" donde indicamos que queremos interaccionar con la imagen en este caso "python:3.9" donde se está señalando la versión que se quiere.
Se puede agregar un entrypoint para poder instalar librerías que se necesitan como Pandas, Numpy, etc...
```docker run -it --entrypoint=bash pyhton:3.9```

# Docker File
El docker file se utiliza para agregar todas las instruciones que queremos ejecutar para crear una nueva imagen según lo que queremos.
El docker file comienza:
    - declaración FROM: aquí decimos qué imagen base es la que queremos usar, por ejemplo, ```FROM python:3.9```
    - comando RUN: se utiliza para ejecutar comandos como instalar paqueterías, por ejempli, ```RUN pip install pandas```
    - entrypoint: se puede definir un enterypoint, por default cuando obtenemos la imagen de python, el entrypoint es python, se puede usar uno diferente, por ejemplo, ```ENTRYPOINT [ "bash" ]```. Además puedes agregar más parámetros, por ejemplo ```ENTRYPOINT [ "python", pipeline.py ]``` aquí prácticamente lo que decimos a docker es que quiero que con python ejecute el archivo pipeline.py
    -comando ```COPY```: entiendo que puede ser source y destination de los datos, para el caso que estamos viendo se agrega el archivo pipeline.py dos veces sugiriendo que primero se nombre la fuente y después el destino.
    - comando ```WORKDIR```:  especifica el directorio de trabaj, está será la ubicación de la imagen en el contenedor docker.

### Construyendo DockerFIle en Docker
Para construir el DockerFile, con las intrucciones que teníamos anteriormente, se tiene que ejecutar una línea de código que va a buscar el DockerFile 

```docker build -t test:pandas .``` : Construye una imagen docker desde el DockerFile, se nombra "test" y se agrega un texto despues de los dos puntos, en este caso "pandas", el punto final significa que la imagen se creará en el mismo directorio dónde está el DockerFile.

Una vez creada la imagen en Docker se puede ejecutar ```docker run -it test:pandas```

### Data Pipelines
Los data pipelines tienen que tener un contenedor autosuficientes, es decir, no queremos correr contenedores, ejecutar el archivo de python del pipeline, además de querer agregar parámetros cómo ejecutar un pipeline cierto día, con ciertas transformaciones, con ciertos datos, es decir que sea parametrico. 
Para esto se tendrá que crear un script de python dónde se podrán agregar las instrucciones necesarias para el pipelime cómo importar paqueterías, hacer transformaciones con pandas, etc..  

```
#Pipeline
import sys
import pandas as pd
print(sys.argv)
dat = sys.argv[1]
  #hacer lo que quieras con pandas
print("se terminó la tarea")

```


# Configurar postgres en Docker?

Para la configuraciónde postgres se necesitan declarar variables de entorno, cómo el usuario ```-e POSTGRES_USER=```, la contraseña del usuarios```POSTGRES_PASSWORD= "root"```, el nombre de la base de datos```POSTGRES_DB= "ny_taxi"``` y el volume (v-) que es una manera de mapear un folder que tenemos en nuestros archivos de la maquina hacia una carpeta en el contenedor docker porque postgres es una base de datos y necesita mantener archivos en un sistema de archivos ```-v c:/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/ny_taxi_db \```.
Se corre el comando docker cómo se muestra a continuacción 

```
docker run -it \
  -e POSTGRES_USER= "root" \
  -e POSTGRES_PASSWORD= "root" \
  -e POSTGRES_DB= "ny_taxi" \
  -v c:/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/ny_taxi_db \
  -p 5432:5432 \
  postgres:13



docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v /c/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/db_ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

para poder conectar al postgres que alzamos con Docker se utiliza pcgli con el comando que se agrega el -h host, -u user, -d database y -p puerto 

```
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

# pgAdmin and Postgres

pgAdmin interactúa con Postgresdb    
la imagen que neceistamos para correr pgAdmin ``` docker pull dpage/pgadmin4 ```

para correr pgAdmin con docker se necesitan las siguientes configuraciones 
```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4

```
hasta aquí no se tiene conectado postgres, por lo tanto nose podrá correr la db dentro del conetenedor , solo hqy que conectar postgres al contenedor de pgAdmin ya que postgres está en otro contenedor.
Se hace un NetWork dónde se juntan 2 contenedores dónde se conecta la base de datos con pgAdmin

``` docker network create pg-network ```

la configuración de Docker que se necesita para crear la base de datos o ponerla para que se pueda conectar la base de datos, con una imagen  

```
docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v /c/workspaces/Sa-lZooCamp2025/Docker_Postgres_Terraform_ZC_01/db_ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

 ```

Esta es la configuración para unir las 2 imagenes en un solo contenedor dentro del network que creamos. 

```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-4 \
  dpage/pgadmin4

```

ahora si, están en un network, en un contenedor 2 imagenes, pgAdmin que es para interaccionar con  la base de datos y postgres que es la base de datos.

#  Dockerizing the Ingestion Script

docker compose
 para convertir un jupyter notebook a un scrip de python, se debe correr un comando jupyter:

 ``` jupyter nbconvert --to-script upload_data_gcli ```


