import discord
import urllib.parse
import os
import requests
import asyncio
import logging
import json

from os import path
from discord.ext import commands, tasks
from dotenv import load_dotenv

# pulling sensitive information from a .env file instead of hardcoding it in
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
APPID = os.getenv("WEATHER_APPID")

# declare the bot as a client
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!weather'):
        msg = message.content.split(" ")
        city = msg[1]
        response = requests.get(F'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={APPID}')
        status_code = response.status_code
        print(status_code)
        if status_code == 200:
            json_obj = response.json()
            for key in json_obj:
                if key == 'main':
                    await message.channel.send(F'The weather in {city} right now is {json_obj[key]["temp"]} degrees.')
        else:
            await message.channel.send(F'{city} does not exist you fucking bafoon')

@client.event
async def on_ready():
    print('Bot has started!')

client.run(TOKEN) # starts the bot

