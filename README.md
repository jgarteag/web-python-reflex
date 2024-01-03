# Proyecto: Adeviento Web 🌐

## Estructura del Proyecto 🏗️

* **web-python-reflex**: Contiene el código fuente principal.
	* **web-python-reflex.py**: Punto de inicio del sitio web.
	* **constants.py**: Definición de constantes utilizadas en el sitio.
	* **styles**: Directorio de estilos (css, colores y fuentes).
	* **views**: Directorio de vistas (secciones gráficas).
	* **components**: Directorio de componentes (elementos gráficos con menor entidad que una vista).
* **assets**: Recursos gráficos y utilidades JavaScript (nive y cuenta atrás).
* **rxconfig.py**: Configuración principal del proyecto (por defecto).
* **requirements.txt**: Lista de dependencias del proyecto para su ejecución.
* **build.sh**: Script de generación estática de la web para producción.
* **[generado] public**: Empaquetado estático del proyecto desplegable en producción (HTML, CSS, JS e imágenes).

## Configuración en Local 🖥️

1. Haz un `Fork` del repositorio.

2. Clona ese repositorio en tu máquina local.

    ```bash 
    git clone url
    ```

3. Navega al directorio del proyecto.

    ```bash
    cd web-python-reflex
    ```

4. Crea un entorno virtual.

    ```bash
    python3 -m venv venv
    ```

5. Activa el entorno virtual.

    ```bash
    source venv/bin/activate
    ```

6. Instala las dependencias.

    ```bash
    python -m pip install -r requirements.txt
    ```

7. Inicializa el proyecto de Reflex.

    ```bash
    reflex init
    ```

8. Ejecuta el proyecto en local.

    ```bash
    reflex run
    ```

    *Podrás acceder a él entrando en la url `http://localhost:3000/` desde el navegador.*

> Para más información sobre [Reflex](https://reflex.dev/), consulta su [documentación oficial](https://reflex.dev/docs).

## Despliegue 🚀

Para realizar el despliegue del proyecto, utiliza el archivo `build.sh`. Este script ejecuta el flujo necesario para generar el directorio `public` con todos los recursos estáticos necesarios para el servidor web.

El repositorio siempre cuenta con el directorio `public` para que puedas revisar el contenido estático de la web sin ejecutar el script `build.sh`.

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
```

## Recursos utilizados

![Python](https://img.shields.io/github/stars/python/cpython?label=Python&style=social)
![Reflex](https://img.shields.io/github/stars/reflex-dev/reflex?label=Reflex&style=social)
![NES.css](https://img.shields.io/github/stars/nostalgic-css/NES.css?label=NES.css&style=social)
![Vercel](https://img.shields.io/github/stars/vercel/vercel?label=Vercel&style=social)

* Lenguaje: [Python](https://www.python.org/)
* Framework: [Reflex](https://reflex.dev/)
* CSS: [NES.css](https://nostalgic-css.github.io/NES.css/)
* Fuente: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P)
* Hosting: [Vercel](https://vercel.com/)