from bs4 import BeautifulSoup as bs
import requests as req

def busqueda_abc(ingrediente):
    url = f"https://www.abc.es/recetasderechupete/?s={ingrediente}"
    
    # Encabezados HTTP para simular una solicitud de navegador y que no nos bloqueen por bot
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = req.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción para códigos de estado de error
        
        # Analizar el contenido HTML
        soup = bs(response.text, "html.parser")
        
        # Verificar la estructura HTML real
        recetas = soup.find_all("h2", class_="entry-title ast-blog-single-element")
        
        # Lista para almacenar las recetas
        lista_recetas = []
        
        for receta in recetas:
            a_tag = receta.find("a", rel="bookmark")
            if a_tag:
                titulo = a_tag.text.strip()
                link = a_tag.get("href")
                full_link = link if link else None
                
                # Buscar la imagen asociada
                img_tag = receta.find_next("img", class_="attachment-large size-large wp-post-image")
                imagen_url = img_tag.get("src") if img_tag else None
                
                lista_recetas.append({
                    "titulo": titulo,
                    "url": full_link,
                    "imagen": imagen_url
                })
        
        return lista_recetas
    
    except req.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except req.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except Exception as e:
        print(f"Error: {e}")
    
    return []

# # Buscar recetas con el ingrediente deseado
# ingrediente = "sopa de pollo"
# recetas_encontradas = busqueda_abc(ingrediente)

# # Imprimir los resultados
# for receta in recetas_encontradas:
#     print(f"Título: {receta['titulo']}")
#     print(f"URL: {receta['url']}")
#     print(f"Imagen: {receta['imagen']}")
#     print("-" * 40)
