import discord
from bot_logic import gen_pass
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('password'):
        gen_pass(10)
    elif message.content.startswith('подбрось монетку'):
        a = random.randint('орёл', 'решка')
        print(a)
    
    elif message.content.startswith('смайлик'):
        def gen_emodji():
            emoji = [':)','=)','о_О',':-<','*О*']
            return random.choice(emoji)
    else:
        await message.channel.send(message.content)

