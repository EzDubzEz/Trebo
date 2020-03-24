
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Gamers, we are good to go")

@bot.event
async def on_message(message):
    if message.content.startswith('!spam '):
        channel = message.channel
        await channel.send(message.content[5:])

bot.run('NjkxODEwODA1NzA4MjI2NjAy.XnlZgA.uVJDU2uBL_AukaXMRmWvEW6HtBo')