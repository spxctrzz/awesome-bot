import discord
from discord.ext import commands
import random
import json
import string



TOKEN = "TOKEN HERE"

client = commands.Bot(command_prefix='ll!')
embed_color = 743448

with open("config.json", "r") as file:
    data = json.load(file)

@client.event
async def on_ready():
    print('--Successfully Started--')

# Harass
@client.listen()
async def on_message(message):
    with open('config.json', 'r+') as file:
        data = json.load(file)
    if message.author.id in data['victim_id']:
        await message.reply(f"{message.author.mention} {random.choice(data['responses'])}")

## Give Harrassment Perms
@client.command(aliases=['givehperms'])
async def give_hperms(ctx, user: discord.Member):
    with open("config.json", "r") as file:
        data = json.load(file)
    if ctx.author.id in data["owners"]:
        if user.id not in data["listen_to"]:
            with open("config.json", "w") as file:
                data["listen_to"].append(user.id)
                json.dump(data, file, indent=2)
            await ctx.send(embed=discord.Embed(description=f'{user.mention} now has harrassment permissions!', color=embed_color))
        else:
            await ctx.send(embed=discord.Embed(description=f'{user.mention} already has harrassment permissions!', color=embed_color))
    else:
        await ctx.send(embed=discord.Embed(description='no perms loser :joy_cat: :thumbsdown:', color=embed_color))

### Remove Harassment Perms
@client.command(aliases=['delhperms'])
async def remove_hperms(ctx, user: discord.Member):
    with open("config.json", "r") as file:
        data = json.load(file)
    if ctx.author.id in data["owners"]:
        if user.id in data["listen_to"]:
            with open("config.json", "w") as file:
                data["listen_to"].remove(user.id)
                json.dump(data, file, indent=2)
            await ctx.send(embed=discord.Embed(description=f'harrassment permissions removed from {user.mention}', color=embed_color))
        else:
            await ctx.send(embed=discord.Embed(description=f'{user.mention} does not have harrassment permissions!', color=embed_color))
    else:
        await ctx.send(embed=discord.Embed(description='no perms loser :joy_cat: :thumbsdown:', color=embed_color))

### Harass
@client.command(aliases=['harass'])
async def harass_member(ctx, user: discord.Member):
    with open("config.json", "r") as file:
        data = json.load(file)
    if ctx.author.id in data["listen_to"] or ctx.author.id in data["owners"]:
        if user.id not in data["victim_id"]:
            with open("config.json", "w") as file:
                data["victim_id"].append(user.id)
                json.dump(data, file, indent=2)
            await ctx.send(embed=discord.Embed(description=f'now harassing {user.mention}', color=embed_color))
        else:
            await ctx.send(embed=discord.Embed(description=f'already harassing {user.mention}', color=embed_color))
    else:
        await ctx.send(embed=discord.Embed(description='no perms loser :joy_cat: :thumbsdown:', color=embed_color))

### Unharass
@client.command(aliases=['unharass'])
async def unharass_member(ctx, user: discord.Member):
    with open("config.json", "r") as file:
        data = json.load(file)
    if ctx.author.id in data["listen_to"] or ctx.author.id in data["owners"]:
        if user.id in data["victim_id"]:
            with open("config.json", "w") as file:
                data["victim_id"].remove(user.id)
                json.dump(data, file, indent=2)
            await ctx.send(embed=discord.Embed(description=f'no longer harassing {user.mention}', color=embed_color))
        else:
            await ctx.send(embed=discord.Embed(description=f'{user.mention} is not being harassed', color=embed_color))
    else:
        await ctx.send(embed=discord.Embed(description='no perms loser :joy_cat: :thumbsdown:', color=embed_color))


client.run(TOKEN)