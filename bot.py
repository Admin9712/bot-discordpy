import discord
from discord.ext import commands
					
bot = commands.Bot(command_prefix='-') # PREFIJO DE EL BOT

@bot.event # EVENTO BOT INICICIADO
async def on_ready():
	actividad = discord.Game("Jugan2") 
	await bot.change_presence(status=discord.Status.online, activity=actividad)
	print("Loggeado en", bot.user) # MENSAJE HACIA LA CONSOLA DICIENDO QUE EL BOT YA ESTA INICIADO

@bot.command() # COMANDO PING
async def ping(ctx): 
    await ctx.send("Pong 🏓")

@bot.command() # COMANDO SUMA
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

@bot.command() # COMANDO INFOCANAL
async def infocanal(ctx):
    embed = discord.Embed(title=f"", description="", color=discord.Color.red())
    embed.add_field(name="Informacion de el este Canal", value=f"**__Nombre de el Canal__**: {ctx.channel.name}\n **__ID de el Canal__**: {ctx.channel.id}\n **__Canal Creado el__**: {ctx.channel.created_at}\n **__Tipo de Canal__**: {ctx.channel.type}\n **__Canal NSFW?__**: {ctx.channel.nsfw}")
    await ctx.send(embed=embed)

bot.run('') # TOKEN DE EL BOT
