import discord
from PrivateVariables import *
import pytesseract

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!info'):
        await message.channel.send('Hello! This discord bot will parse uploaded images for relevant health information')
    if len(message.attachments) > 0:
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
        outstring = pytesseract.image_to_string(message.attachments[0].filename)
        await message.channel.send(outstring)

client.run(BOTTOKEN)