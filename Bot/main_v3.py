import discord
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user} has connected to Discord!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$argent'):
        await message.channel.send('your_message')

@client.event
async def on_member_join(member):
    guild = client.get_guild(id_guild)
    channel = guild.get_channel(id_guild)
    await channel.send(f'Bienvenue sur le {guild.name} server, {member.name}!')
    await member.send(f'Bienvenue sur le serveur {member.mention} !')
    

client.run(TOKEN)
