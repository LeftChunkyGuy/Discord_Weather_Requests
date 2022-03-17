import discord
import urllib.parse
import os
import requests
import asyncio
import logging

from os import path
from discord.ext import commands, tasks
from dotenv import load_dotenv

# pulling sensitive information from a .env file instead of hardcoding it in
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# declare the bot as a client
client = discord.Client()



@client.event
async def on_ready():
    print('Bot has started!')

client.run(TOKEN) # starts the bot

