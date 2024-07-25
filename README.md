# RecipeScrapper

**RecipeScrapper** es una aplicación web que permite buscar y visualizar recetas de dos sitios web populares, **ABC.es** y **Cocinatis**, mediante web scraping. Utiliza Python para realizar la extracción de datos y Flask para la interfaz web.

## Descripción

Este proyecto es una aplicación sencilla para buscar recetas en dos sitios web específicos. El usuario introduce un ingrediente y la aplicación muestra recetas relacionadas con ese ingrediente, recuperadas a través de scraping. La aplicación tiene una interfaz web moderna que muestra las recetas con enlaces para ver los detalles completos.

## Funcionalidades

- **Búsqueda de recetas**: Introduce un ingrediente para obtener recetas relacionadas.
- **Recuperación de datos**: Scrapea recetas de **ABC.es** y **Cocinatis**.
- **Interfaz web**: Diseño responsivo con un formulario de búsqueda y resultados de recetas.

## Dependencias

Asegúrate de tener instaladas las siguientes dependencias:

### Python

- Flask
- Requests
- BeautifulSoup4 (bs4)

### Frontend

- CSS personalizado

Puedes instalar las dependencias de Python utilizando `pip`:

```bash
pip install Flask requests beautifulsoup4
python3 app.py

