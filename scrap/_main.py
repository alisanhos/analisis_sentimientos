import os
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_tweets(username):
    all_the_tweets = []  # Una lista para almacenar todos los tweets de una página
    driver = webdriver.Chrome()  # Requiere tener instalado el driver de Chrome
    driver.get(f"https://twitter.com/{username}")
    sleep_time = 3
    time.sleep(sleep_time)  # Espera unos segundos para que se carguen los tweets

    # Repetir el proceso hasta que tenga 100 tweets
    while len(all_the_tweets) < 10:
        # Desplazarse hacia abajo para cargar más tweets (opcional)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_time)  # Espera adicional para cargar más tweets si es necesario

        page_source = driver.page_source

        soup = BeautifulSoup(page_source, "html.parser")
        tweets = soup.find_all("div", attrs={"data-testid": "tweetText"})
        all_the_tweets += tweets

    driver.quit()
    
    if all_the_tweets:
        # Obtener la ruta relativa al directorio del proyecto
        script_directory = os.path.dirname(os.path.abspath(__file__)) + "/tweets"
        # crear el directorio si no existe
        if not os.path.exists(script_directory):
            os.makedirs(script_directory)
            print(f"Se ha creado el directorio {script_directory}")
        file_path = os.path.join(script_directory, f"tweets_{username}.csv")

        with open(file_path, "w", encoding="utf-8", newline="",) as file:
            writer = csv.writer(file)
            for tweet in all_the_tweets:
                tweet_span = tweet.find_next("span")
                tweet_text = tweet_span.get_text(strip=True)
                tweet_text = tweet_text.replace("\n", " ")  # Eliminar los saltos de línea del contenido del tweet
                writer.writerow([tweet_text])

              #  print(tweet_text)
              #  print("------------------------")

        print(f"Los nuevos tweets se han guardado en {file_path}")
    else:
        print("No se encontró el contenedor de tweets.")

# Ejemplo de uso
scrape_tweets("elonmusk")
scrape_tweets("LinusTech")
scrape_tweets("illojuan")