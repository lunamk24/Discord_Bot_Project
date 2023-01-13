from discord.ext import commands
import aiohttp
import os
import discord
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Ready!')

@bot.command()
async def cat( ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('http://aws.random.cat/meow') as r:
            data = await r.json()

            embed = discord.Embed(title="Meow")
            embed.set_image(url=data['file'])
            embed.set_footer(text='http://aws.random.cat/')

            await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://random.dog/woof.json') as r:
            data = await r.json()

            embed = discord.Embed(title="Woof")
            embed.set_image(url=data['url'])
            embed.set_footer(text='https://random.dog/')

            await ctx.send(embed=embed)



bot.run('Token')
