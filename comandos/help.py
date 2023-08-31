import logging
import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    
    url = requests.get("https://dolarhoy.com/")

    soup = BeautifulSoup(url.content, "html.parser")

    result = soup.find("div", class_="venta").find("div", class_="val").get_text()
    await update.message.reply_text(result)
