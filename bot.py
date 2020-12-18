import discord
from discord.ext import commands
					
bot = commands.Bot(command_prefix='-') # PREFIJO DE EL BOT

@bot.event
async def on_ready():
	actividad = discord.Game("Jugan2") # ESTADO DE EL BOT
	await bot.change_presence(status=discord.Status.online, activity=actividad)
	print("Loggeado en", bot.user) # BOT INICIADO

@bot.command() # COMANDO PING
async def ping(ctx): 
    await ctx.send("Pong 🏓")

@bot.command() # COMANDO 
async def suma(ctx, sumNumUno: int, sumNumDos: int): 
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Resultado de tu Suma", value=f"{sumNumUno + sumNumDos}")
    await ctx.send(embed=embed)

@bot.command() # COMANDO RESTA
async def resta(ctx, resNumUno: int, resNumDos: int):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Resultado de tu Resta", value=f"{resNumUno - resNumDos}")
    await ctx.send(embed=embed)

@bot.command() # COMANDO INFOSERVER
async def infoserver(ctx):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Informacion de el Servidor", value=f"**__Nombre de el Servidor__**: {ctx.guild.name}\n **__ID de el Servidor__**: {ctx.guild.id}\n **__Servidor Creado el__**: {ctx.guild.created_at}\n **__Region de el Servidor__**: {ctx.guild.region}")
    await ctx.send(embed=embed)

bot.run('Nzg4MDA0MDYzNTEzOTM1ODkz.X9dL-Q.bcuBQAbTyJ8tJ0-94tR6cQcB8rk') # LOGGEANDOSE A EL BOT
