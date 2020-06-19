
import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix='=', description='KotoriBot v 0.1\n Standard prefix: "="')

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

if __name__ == "__main__":
 token = os.environ.get('BOT_TOKEN')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="a game"))

token = os.environ.get('BOT_TOKEN')