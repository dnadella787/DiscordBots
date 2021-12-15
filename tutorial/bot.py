import os 
import discord

from discord import integrations 
from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)


# when the bot joins the server, execute
# the following code
@client.event 
async def on_ready():
    # if the bot is connected to multiple servers
    # find the specific desired server

    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


    # owner = discord.utils.find(lambda m: m.name == "dman", guild.members)
    owner = discord.utils.get(guild.members, name="dman")
    print(f'\nThe owner of this server is: {owner}')


# when a member joins your discord server,
# send them a message
@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the python tutorial discord server'
    )

# if a message sent in a text channel that the discord
# server has access to, then respond
@client.event
async def on_message(message):
    # don't let the bot respond to itself, make sure
    # that the person that sends it is a user, and not the bot
    if message.author == client.user:
        return 

    if message.content == "How are you guys today?":
        await message.channel.send("Good, how are you?")
    elif message.content == 'raise-exception':
        raise discord.DiscordException 
    

@client.event 
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == "on_message":
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise 

client.run(TOKEN)