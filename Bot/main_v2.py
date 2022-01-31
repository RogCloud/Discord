import discord
import os

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    #print('We have logged in as {0.user} has connected to Discord!'.format(client))
    print(f'{client.user.name} has connected to Discord!')

@client.event
#async def on_member_join(member):
async def on_message_join(member):
    channel = client.get_channel(936657801239986199)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    #embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!

    await channel.send(embed=embed)

    #mention=member.mention
    #guild=member.guild
    #await member.create_dm()
    #await member.dm_channel.send(str(
    #    f'Hi {mention}, welcome to my Discord server! {guild}').format(mention=mention, guild=guild))
    #await member.dm_channel.send(str()
    #    f'Hi {member.name}, welcome to my Discord server!'
    #)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#if TOKEN is not None :
client.run(TOKEN)
