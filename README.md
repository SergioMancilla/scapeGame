# ScapeGame
Este es un pequeño juego desarrollado en Python, usando la librería PyGame: https://pypi.org/project/pygame/

## Para poder jugar:
1. Clona el repositorio
2. Crea un ambiente virtual de Python dentro de la carpeta del proyecto: `python -m venv env-name` (Puedes consultar aquí: https://docs.python.org/es/3.13/tutorial/venv.html)
3. Activar el ambiente virtual. Esto depende del sistema operativo, pero puedes moverte hasta la carpeta `env-name/Scripts` y ejecutar el comando `activate` o `activate.bat`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta el proyecto: `python initial.py`

Nota: dependiendo de tu sistema operativo o versión de Python instalada, es posible que el comando a ejecutarsea `python`, `python3` o `py`.

## ¿Cómo jugar?
El juego consiste en tener que encontrar la cantidad de llaves necesarias para abrir puertas.
Sencillo, ¿cierto? Pues, estarás casi a oscuras, sólo con un espacio circular que rodea al personaje, como si llevara una linterna. Mientras recorres el mapa para buscar las llaves, encontrarás 3 tipos de montruos, con diferentes cualidades:
- Zombie: Es el más lento y también el que menos daño hace
- Walker: Su apariencia es espeluznante y tiene mayor ataque que el anterior
- Boogie: Este personaje es mucho más rápido que los demás, y su ataque te quitará el 20% de vida
Una vez que te estrelles con uno, este desaparecerá para no seguirte atormentando.
Debes recoger todas las llaves del mapa en cada nivel para que la puerta se abra, y luego dirigirte hacia ella para pasar al siguiente.
Cada nivel hay más llaves por recolectar, y más monstruos, por lo que a medida que vas avanzando, te será más difícil seguir.

Este juego usa las teclas WASD para mover el persona, y click en los menús
El juego no incluye audio actualmente, y aún tiene detalles por mejorar.
