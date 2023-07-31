import discord

from discord.ext import commands, tasks
from selenium_script import generate_exam_alert
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

intents = discord.Intents.default() 
intents.typing = False 
intents.presences = False  

bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    send_exam_alert.start()

@tasks.loop(hours=24)
async def send_exam_alert():
    channel_id = getenv("CHANNEL_ID")  
    channel = bot.get_channel(int(channel_id)) # channel id should be an integer
    exam_alert = await generate_exam_alert()
    await channel.send(exam_alert)

bot.run(getenv("DISCORD_TOKEN")) 