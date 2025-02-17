# Docker - Terraform Module 1

Cómo saber si tienes bien instalado Docker. 
ejecular línea: ```docker run hello-world```
la primera palabra "docker" para referenciar a docker, la segunda palabra "run" para ejecutar y la tercera palabra "hello-world" para indicar la imagen.

Se pueden ejecutar imagenes de bash de ubuntu, como lo indica la imagen "hello-world", otras cosas que se pueden ejecutar es python:
```docker run -it python:3.9```
En esta ejecución docker agregamos un "-it" donde indicamos que queremos interaccionar con la imagen en este caso "python:3.9" donde se está señalando la versión que se quiere.
Se puede agregar un entrypoint para poder instalar librerías que se necesitan como Pandas, Numpy, etc...
```docker run -it --entrypoint=bash pyhton:3.9```