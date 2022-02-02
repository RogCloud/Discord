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
async def on_member_join(member):
    guild = client.get_guild(936657801239986196)
    channel = guild.get_channel(936657801239986199)
    await channel.send(f'Bienvenue sur le serveur {member.mention} !')
    await member.send(f'Bienvenue sur le {guild.name} server, {member.mention}!')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel_message = str(message.channel)
    print(f'{username}: {user_message} ({channel_message})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'general':
        if user_message.lower() == 'bonjours':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'aurevoir':
            await message.channel.send(f'à bientôt {username}!')
            return
    
client.run(TOKEN)
