import discord
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

ID_TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user} has connected to Discord!'.format(client))

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome on the new server {member.mention} !')
    #guild = client.get_guild(id_guild))
    #channel = client.get_channel(id_channels)
    #await member.send(f'Bienvenue sur le {guild.name} server, {member.mention}!')

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'{member.mention} has just leave the server !')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel_message = str(message.channel)
    #print(f'{username}: {user_message} ({channel_message})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'general':
        if user_message.lower() == 'bonjours':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'aurevoir':
            await message.channel.send(f'à bientôt {username}!')
            return

client.run(ID_TOKEN)
