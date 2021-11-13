import nextcord
import asyncio
import random
import config
import nextcord.ext
from nextcord.utils import get
from nextcord.ext import commands, tasks

token = "ok"

client = nextcord.Client()

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
      await ctx.reply(config.warning1 + random.randrange(10,150) + config.warning2 + " Remember, " + random.choice(config.propaganda) + """

Your message will be deleted and forwarded to the Chinese Ministry of Security in 10 seconds.""")
      await asyncio.sleep(10)
      await ctx.delete() #deletes their message

@client.event # Keeps people silenced
async def on_message(ctx):
    if ctx.author.id in config.silenced:
        await ctx.delete()
        print("Message \"" + ctx.content + "\" deleted from " + ctx.author.name)


client.run(token)
