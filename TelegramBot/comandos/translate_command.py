import logging
import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def translate_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    archivo_json = "user_data.json"
    user = update.effective_user
# Leer los datos desde el archivo JSON
    with open(archivo_json, "r") as archivo:
        user_data = json.load(archivo)

    target_user_language = None

        # Itera sobre la lista para encontrar al usuario por su ID
    for datos in user_data:
        if int(datos["user_id"]) == user.id:
            target_user_language = datos["language"]
            break  # Si encontraste al usuario, puedes salir del bucle

    if target_user_language is not None:
        params = {
            'q': update.message.text,
            'langpair': target_user_language,
            'de': 'pablotomasmenna@gmail.com'
        }

        # URL de la API de MyMemory
        url = 'https://api.mymemory.translated.net/get'

        # Realiza la solicitud GET
        response = requests.get(url, params=params)

        # Comprueba si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:

            data = response.json()
            translation = data['responseData']['translatedText']
            await update.message.reply_text(translation)
            
        else:
            print("Error en la solicitud. Código de estado:", response.status_code)
    
    else:
        print(f"No se encontró un usuario con ID {user.id}")