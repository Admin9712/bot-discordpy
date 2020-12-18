import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')
@bot.event
async def on_ready():
	actividad = discord.Game("Jugan2")
	await bot.change_presence(status=discord.Status.online, activity=actividad)
	print("Loggeado en", bot.user)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('')
