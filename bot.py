import os

import discord
from dotenv import load_dotenv #not be using, might implement in the future

load_dotenv() #not implemented fully, it will make source code more secure tho
TOKEN = 'ODA2MjY3NTQyOTYwMDc4ODg4.YBm9KQ.KJ45k96BSJmzSQ2hOdlaxNqoeVg' #discord bot token

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!') #prints to console - bot is online

@client.event
async def on_message(message):
    #str(message.author) == TARGET_USER:
    if discord.utils.get(message.author.roles, name="Unsafe"): #checks if message is sent from user w/ specific role
        print("User from unsafe role sent a message") #prints to console

        word = "example bad word" 
        if word in message.content or message.attachments: #check if message contains bad word or has an attachment
            await message.delete()
            await message.channel.send("Removed " + str(message.author) + "'s message - Please keep this server clean")
client.run(TOKEN)