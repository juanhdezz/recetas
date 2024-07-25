from bs4 import BeautifulSoup as bs
import requests as req

def busqueda_cocinatis(ingrediente):
    url = f"https://www.cocinatis.com/que-cocino-hoy/busqueda.html?q={ingrediente}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = req.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción para códigos de estado de error
        response.encoding = 'utf-8'  # Especifica la codificación
        soup = bs(response.text, "html.parser")
        recetas = soup.find_all("a", class_="recipe-link")
        lista_recetas = []
        contador = 0
        for receta in recetas:
            contador += 1
            if contador % 2 != 0:
                titulo = receta.get("title")
                link = receta.get("href")
                full_link = f"https://www.cocinatis.com{link}"
                
                # Encontrar la imagen asociada
                source_tag = receta.find("source", {"media": "(min-width: 415px)"})
                imagen_url = source_tag.get("srcset") if source_tag else None
                
                lista_recetas.append({
                    "titulo": titulo,
                    "url": full_link,
                    "imagen": f"https://www.cocinatis.com{imagen_url}" if imagen_url else None
                })
        return lista_recetas
    except req.exceptions.RequestException as e:
        print(f"Error al acceder a la página: {e}")
        return []

# Llamar a la función con el ingrediente deseado
# ingrediente = "sopa de pollo"
# recetas_encontradas = busqueda_cocinatis(ingrediente)

# Imprimir los resultados
# for receta in recetas_encontradas:
#     print(f"Título: {receta['titulo']}")
#     print(f"URL: {receta['url']}")
#     print(f"Imagen: {receta['imagen']}")
#     print("-" * 40)
