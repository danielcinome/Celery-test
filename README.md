## Proyecto 2
1. Desarrollar una función Lambda que consulte a la página https://dweet.io/follow/thecore los valores de “temperature” y “humidity” cada minuto durante 15 minutos
2. Almacenar los valores consultados en una base de datos
3. Pasados los quince minutos, que la función Lambda de forma automática golpee el webhook URL https://webhook.site/14693700-0cce-4ef4-9961-e927cf90c008 con un body que incluya todos los valores almacenados en la base de datos


## Descripción
Para la solución de este proyecto he utilizado el lenguaje de programación Python y usado un entorno virtual para evitar el conflicto de dependencias y para que se facilite la ejecución en otro entorno local. A continuación encontrarás los pasos para ejecutar el proyecto en tu máquina local.
####  Configuración
1. clonar el repositorio `git clone https://github.com/danielcinome/todolegal-test2.git`

2. ir a la carpeta todolegal-test-backend con el comando `cd todolegal-test2`
---

File Name|Description
---|---
[config_venv	](https://github.com/danielcinome/todolegal-test-backend/blob/main/config_venv)| En éste archivo encontrara la configuración para su ambiente local, contiene una serie de scripts de instalación de paquetes necesarios para correr el proyecto.

### Nota: Este Ejercicio no se ha desarrollado por completo, por términos de tiempo he usado celery en lugar de lambda

Con el fin de lograr el principal objetivo, en este punto del desarrollo, la función es ejecutada cada minuto haciendo la petición a la URL dada en el ejercicio y guardando los datos en la base de datos. 
	
![N|Solid](https://i.ibb.co/1dXZh7q/test2.png)




## Author

- Daniel Chinome - [Github](https://github.com/danielcinome) / [Twitter](https://twitter.com/DanielChinome)
