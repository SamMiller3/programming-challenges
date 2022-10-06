# discordbot.py, 14th January 2021
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
@client.command()
async def dice(ctx):
    embedVar = discord.Embed(title="Dice", description="by Samuel Miller", color=0x00ff00)
    embedVar.add_field(name="Value 1", value=random.randint(1,6), inline=False)
    embedVar.add_field(name="Value 2", value=random.randint(1,6), inline=False)
    await ctx.send(embed=embedVar)
client.run(TOKEN)
