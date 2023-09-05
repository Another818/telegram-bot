import logging
import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def set_lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    # Datos del usuario
    user_data = {
        "user_id": user.id,
        "language": "es|en"
    }

    # Nombre del archivo JSON
    archivo_json = "user_data.json"

    # Leer los datos actuales del archivo JSON (si existen)
    try:
        with open(archivo_json, "r") as archivo:
            existing_data = json.load(archivo)
    except FileNotFoundError:
        existing_data = []

    # Agregar los nuevos datos del usuario
    existing_data.append(user_data)

    # Guardar los datos actualizados en el archivo JSON
    with open(archivo_json, "w") as archivo:
        json.dump(existing_data, archivo)