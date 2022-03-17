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
    if message.content.startswith('!weather'): # Checking if the message in the server starts with !weather. If not it will ignore it
        msg = message.content.split(" ") # Converting the string into a list for simple parsing
        city = msg[1]
        response = requests.get(F'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={APPID}') # Using an F string to make an API call to grab the requested city
        status_code = response.status_code
        print(status_code)
        if status_code == 200: # Status code of 200 means good request
            json_obj = response.json() # Turn the response into a "json" object
            for key in json_obj: # Look for the desired section of the return object
                if key == 'main':
                    await message.channel.send(F'The weather in {city} right now is {json_obj[key]["temp"]} degrees.') # Have the bot send a message with the requested data
        else:
            await message.channel.send(F'{city} does not exist you fucking bafoon') # If the status code was not 200, tell them they fucked up

@client.event
async def on_ready():
    print('Bot has started!')

client.run(TOKEN) # starts the bot

