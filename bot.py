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
    await ctx.send("Pong 🏓")

@bot.command()
async def suma(ctx, sumNumUno: int, sumNumDos: int):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Resultado de tu Suma", value=f"{sumNumUno + sumNumDos}")
    await ctx.send(embed=embed)

@bot.command()
async def resta(ctx, resNumUno: int, resNumDos: int):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Resultado de tu Resta", value=f"{resNumUno - resNumDos}")
    await ctx.send(embed=embed)

@bot.command()
async def infoserver(ctx):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Informacion de el Servidor", value=f"**__Nombre de el Servidor__**: {ctx.guild.name}\n **__ID de el Servidor__**: {ctx.guild.id}\n **__Servidor Creado el__**: {ctx.guild.created_at}\n **__Region de el Servidor__**: {ctx.guild.region}")
    await ctx.send(embed=embed)

bot.run('')
