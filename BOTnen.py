import discord
from discord.ext import commands
from random import *
import random as rnd
from time import sleep
from webserver import keep_alive
import os
from tekst import *
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
  print("Bot is ONLINE!...")


@bot.command()
async def botnen(ctx):
    await ctx.reply("Hello\nLet me help you!\nThis is a list of my commands:")
    await ctx.reply(".hello\n.sivert\n.audun\n.chris\n.william\n.teams - for making two random teams\n.add\n.dice\n.flip - flip a coin\n.choose - for choosing between games etc\n.ping")


@bot.event
async def on_ready():
    activity = discord.Game(name="with myself", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello" + " " + "I'm "+ "**BOTnen**" + ", a Discord Bot created by Hans Botnen\nFor a list of my functions, type .botnen")


@bot.command()
async def fuckyou(ctx):
    await ctx.reply("Fuck you too, human!")


@bot.command()
async def dice(ctx, dice):
    terning = randint(1, int(dice))
    await ctx.reply(str(terning))

	
@bot.command()
async def teams(ctx, *names: str):
    navn = []
    for e in names:
        navn.append(str(e))
    rnd.shuffle(navn)
    length = len(navn)
    midten = length//2
    lag1 = []
    lag2 = []
    lag1.append(navn[:midten])
    lag2.append(navn[midten:])
    await ctx.reply("Dette blir spennede...")
    sleep(1)
    await ctx.reply("LAG 1 -->   " + str(lag1))
    await ctx.reply("LAG 2 --> " + str(lag2))


@bot.command()
async def flip(ctx):
    terning = randint(1, 2)
    await ctx.reply("Flipping... 50/50")
    sleep(0.2)
    await ctx.reply("5")
    sleep(0.4)
    await ctx.reply("4")
    sleep(0.4)
    await ctx.reply("3")
    sleep(0.4)
    await ctx.reply("2")
    sleep(0.4)
    await ctx.reply("1")
    sleep(0.4)
    if terning == 1:
        await ctx.reply("Heads!")
    else:
        await ctx.reply("Tails!")

"""
This one does not allow you to play leauge, EVER! 
You´re Welcome
"""
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    lol = ["lol", "LOL", "leauge", "Leauge of legends", "Lol", "league", "League of legends"]
    liste = []
    for e in choices:
        if e not in lol:
            liste.append(str(e))

    rnd.shuffle(liste)
    
    await ctx.send("Dere skal spille"+" "+str(liste[0]))


@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")



keep_alive()
tOken = os.environ.get("HemmeligKODE")
bot.run(tOken)
