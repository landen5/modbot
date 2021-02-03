import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'ODA2MjY3NTQyOTYwMDc4ODg4.YBm9KQ.KJ45k96BSJmzSQ2hOdlaxNqoeVg'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    #str(message.author) == TARGET_USER:
    if discord.utils.get(message.author.roles, name="Unsafe"):
        print("User from unsafe role sent a message")

        word = "example bad word"
        if word in message.content or message.attachments:
            await message.delete()
            await message.channel.send("Removed " + str(message.author) + "'s message - Please keep this server clean")
client.run(TOKEN)