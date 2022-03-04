import discord
from discord.ext import commands
from random import *
import random as rnd
from time import sleep

bot = commands.Bot(command_prefix=".")

@bot.command()
async def botnen(ctx):
    await ctx.reply("Hello\nLet me help you!\nThis is a list of my commands:")
    await ctx.reply(".hello\n.sivert\n.add\n.dice\n.flip\n.choose\n.ping")


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello" + " " + "I'm "+ "**BOTnen**" + ", a Discord Bot created by Hans Botnen\nFor a list of my functions, type .botnen")


@bot.command()
async def sivert(ctx):
    await ctx.reply("hmmmm Sivert... let me think")
    sleep(3)
    await ctx.reply("Sivert sound pretty retarded")


@bot.command()
async def add(ctx, num1, num2):
    await ctx.reply(float(num1)+float(num2))


@bot.command()
async def dice(ctx, dice):
    terning = randint(1, int(dice))
    await ctx.reply(str(terning))


@bot.command()
async def random(ctx, names, antall):
    liste = []
    



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
async def secretchoose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(choice(choices))


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    lol = ["lol", "LOL", "leauge", "Leauge of legends", "Lol"]
    liste = []
    for e in choices:
        if e not in lol:
            liste.append(str(e))

    rnd.shuffle(liste)
    
    await ctx.send("Dere skal spille"+" "+str(liste[0]))


@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")




bot.run("OTQ4MzY1NDU4NjU3MTMyNTU0.Yh6wKQ.hcxQcSP7to-S8Ck35EUhxQ2C2V0")
