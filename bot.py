#Import Discord Package
import discord
import datetime
from discord.embeds import Embed
from discord.ext import commands

bot = commands.Bot(command_prefix='peng!', description="This is the helper bot")

#Para crear comandos
@bot.command()
async def info(ctx):
    embedVar =  discord.Embed(title= f"{ctx.guild.name}", descriprion = "Server Information", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embedVar.add_field(name = "Server Owners", value = f"nosotros lol")
    embedVar.add_field(name = "Commands", value = f"peng!help")
    embedVar.add_field(name = "Web Page", value =f"toughpenguins.club")
    embedVar.set_thumbnail(url ="https://media.istockphoto.com/vectors/penguin-with-a-rocket-flat-design-vector-id1141624697")
    await ctx.send(embed = embedVar)

@bot.command()
async def hi(ctx):
    embedhi = discord.Embed(title=f"" , timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embedhi.add_field(name= "Greeting", value= "Hello, I hope you are well and don't forget to support the project. Write peng!helpu to know more commands")
    await ctx.send(embed=embedhi)

@bot.command()
async def sayrul(ctx, * , arg):
    embedRules = discord.Embed(title=f"", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embedRules.add_field(name= "Rules", value=arg)
    await ctx.send(embed=embedRules)

@bot.command()
async def sayann(ctx, arg1, arg2):
    embedann = discord.Embed(title=f"" , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embedann.add_field(name=arg1, value=arg2)
    await ctx.send(embed=embedann)

@bot.command()
async def helpu(ctx):
    embedcom = discord.Embed(title=f"" , timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embedcom.add_field(name= "Commands", value= "peng!ifno : Information about the server. \n peng!hi : To have a greeting.")
    await ctx.send(embed=embedcom)
#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="toughpenguins.club"))
    print('I wake up bitches')

bot.run('ODg2MzU0NzMwNTMwNTA4ODcw.YT0YKw.-2CXV8Rexk30uPS5knDpGo6G1bM')