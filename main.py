import discord
import asyncio
import random
import config
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks

token = "inset your token here"

client = discord.Client()

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
@client.event
async def on_message(ctx):
    if ctx.author.id in config.blacklist: 
        return
    if ctx.author == client.user:
        return
    if ctx.author.bot: return
    sent = ctx.content.lower()
    if any(banned in sent for banned in config.banned):
      await ctx.reply(config.warning + " Remember, " + random.choice(config.propaganda) + """
      
      Your message will be deleted and forwarded to the Chinese Ministry of Security in 10 seconds.""")
      await asyncio.sleep(10)
      await ctx.delete() #deletes their message

client.run(token) 