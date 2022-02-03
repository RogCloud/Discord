from operator import imod
import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

ID_TOKEN = os.getenv('DISCORD_TOKEN')

#  _________
# /         \
#  Bot start
# \_________/
@client.event
async def on_ready():
    print('We have logged in as {0.user} has connected to Discord!'.format(client))

#   ___________________________
# /                            \
#  New Member Join Notification
# \____________________________/
@client.event
async def on_member_join(member):
    mention = member.mention
    guild = member.guild
    await member.create_dm()
    await member.dm_channel.send(str(f'{mention}, Welcome on the new server {guild}').format(mention=mention, guild=guild))

    embed = discord.Embed(title=str("***New Member Joined***"), colour=0x33c946, description=str(f'{mention} joined to the {guild}').format(mention=mention, guild=guild))
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
    embed.timestamp=datetime.datetime.utcnow()
    embed.add_field(name='User ID :', value=member.id)
    embed.add_field(name='User Name :', value=member.display_name)
    embed.add_field(name='Server Name :', value=guild)
    embed.add_field(name='User Serial :', value=len(list(guild.members)))
    embed.add_field(name='Created_at :', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='Joined_at :', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    
    channel = discord.utils.get(member.guild.channels, name='join-member')
    await channel.send(embed=embed)

#  _________________________
# /                         \
#  Member Leave Notification
# \_________________________/

@client.event
async def on_member_remove(member):
    mention = member.mention
    guild = member.guild

    embed = discord.Embed(title=str("***New Member Leaved***"), colour=0x33c946, description=str(f'{mention} leave from {guild}').format(mention=mention, guild=guild))
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')
    embed.timestamp=datetime.datetime.utcnow()
    embed.add_field(name='User ID :', value=member.id)
    embed.add_field(name='User Name :', value=member.display_name)
    embed.add_field(name='Server Name :', value=guild)
    embed.add_field(name='User Serial :', value=len(list(guild.members)))
    embed.add_field(name='Created_at :', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='leaved_at :', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    
    channel = discord.utils.get(member.guild.channels, name='leave-member')
    await channel.send(embed=embed)

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
