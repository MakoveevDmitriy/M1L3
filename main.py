import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passvord(ctx):
    
    await ctx.send(gen_pass(10))
    
@bot.command()
async def money(ctx):
    a = random.randint(1, 2)
    if a == 1:
        await ctx.send('решка')
    else:
        await ctx.send('орёл')


bot.run("токен")
