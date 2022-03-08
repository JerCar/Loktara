# bot.py
import os # operating system
import requests # Chuck Norris Jokes

import discord
from discord.ext import commands
from dotenv import load_dotenv # for working with environment variables

import random


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents = discord.Intents.default() # new since update
#intents.members = True

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='Chuck_Joke', help='Responds with a random Chuck Norris joke from http://api.icndb.com/jokes/random')
async def chuck(ctx): # ctx is the context, includes data such as channel and guild that user called command from
    response = requests.get(f"http://api.icndb.com/jokes/random")
    unparsedChuck = response.json()
    # print(unparsedChuck)
    response = unparsedChuck["value"]["joke"]
    response = response.replace('&quot;', '"')
    await ctx.send(response)

@bot.command(name='Daemon!', help='Respect where it belongs')
async def marles(ctx):
    replies = [
        'Hey Knight. Everyone! This guys the man!',
        'Sup Daemon. Welcome.',
        'Welcome back, lord Knight.'
    ]
    x = random.choice(replies)
    await ctx.send(x)

@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll(ctx, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
    ]
    await ctx.send(dice)

@bot.command(name='create_channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='Loktaria-Suburbs'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        channel = await guild.create_text_channel(channel_name)

bot.run(TOKEN)