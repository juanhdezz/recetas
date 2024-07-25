from bs4 import BeautifulSoup as bs
import requests as req

def busqueda_cocinatis(ingrediente):
    url = f"https://www.cocinatis.com/que-cocino-hoy/busqueda.html?q={ingrediente}"
    try:
        response = req.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado de error
        soup = bs(response.text, "html.parser")
        recetas = soup.find_all("a", class_="recipe-link")
        lista_recetas = []
        contador = 0
        for receta in recetas:
            contador += 1
            if(contador % 2 != 0):
                titulo = receta.get("title")
                link = receta.get("href")
                full_link = f"https://www.cocinatis.com{link}"
                lista_recetas.append({
                    "titulo": titulo,
                    "url": full_link
                })
        return lista_recetas
    except req.exceptions.RequestException as e:
        print(f"Error al acceder a la página: {e}")
        return []


# Llamar a la función con el ingrediente deseado
ingrediente = "sopa de pollo"
recetas_encontradas = busqueda_cocinatis(ingrediente)
