import discord
from discord.ext import commands
from random import *
import random as rnd
from time import sleep
from webserver import keep_alive
import os
from tekst import *
import youtube_dl
from quotes import *
import time
import asyncio
import requests
from dotenv import load_dotenv
import utilities


bot = commands.Bot(command_prefix=".")


      
@bot.command()
async def lol(ctx):
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  await ctx.reply("League of Legends suger")
  
  await ctx.message.delete()
  

@bot.command()
async def databrus(ctx):
  await ctx.reply("Forskning viser at voldsomme mengder databrus **faktisk er bra for deg!**\nKjøp det her..."+"\n\n"+"https://www.amazon.com/Monster-Energy-Drink-Green-Original/dp/B019AKA6YU?th=1")
  await ctx.reply("....*sponsored by monster energy*")
  await ctx.message.delete()
  


@bot.event
async def on_ready():
  print("Bot is ONLINE!...")


@bot.command()
async def botnen(ctx):
    await ctx.reply("Hello\nLet me help you!\nThis is a list of my commands:")
    await ctx.reply("\n.botnen\n.add\n.choose\n.dice\n.flip\n.hello\n.lol\n.teams\n.status\n.databrus\n.ping\n.fuckyou")


@bot.event
async def on_ready():
    activity = discord.Game(name="with siverts hair", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.command()
async def status(ctx):
  await ctx.reply("Status:\nI am currently playing with Siverts hair, and i LOVE it")
  await ctx.message.delete()


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello" + " " + "I'm "+ "**BOTnen**" + ", a Discord Bot created by Hans Botnen\nFor a list of my functions, type .botnen")





@bot.command()
async def add(ctx, num1, num2):
    await ctx.reply(float(num1)+float(num2))


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


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    lol = ["lol", "LOL", "leauge", "Leauge of legends", "Lol", "league", "League of legends"]
    liste = []
    for e in choices:
        if e not in lol:
            liste.append(str(e))

    rnd.shuffle(liste)
    
    await ctx.send("Jeg velger..."+" "+str(liste[0]))


@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")



keep_alive()
tOken = os.environ.get("insert discordBOT token")
bot.run(tOken)
