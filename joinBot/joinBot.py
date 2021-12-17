import os
import discord 

from discord.ext import commands 
from dotenv import load_dotenv 

load_dotenv()
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

my_intents = discord.Intents.default()
my_intents.members = True 

bot = commands.Bot(command_prefix='!', intents=my_intents)


users_to_ping = {}


# event that pings the relavent users who wanted to
# know when a specific user enters a voice channel
@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if not before.channel and after.channel and member.id in users_to_ping:
        guild = discord.utils.get(bot.guilds, name=GUILD)

        for memb_id in users_to_ping[member.id]:
            dm_member = discord.utils.get(guild.members, id=memb_id)

            channel = await dm_member.create_dm()
            await channel.send(f'{member.name} is currently in the {after.channel} channel in {guild.name} server.')



# start up, creates channel 'point-bot' for
# all commands
@bot.command(name='start', help='create a channel, must be role role1, role2')
@commands.has_any_role('role1', 'role2')
async def start(ctx):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name='join-bot')

    if not existing_channel:
        print(f'Creating a new channel for commands: join-bot')
        await guild.create_text_channel('join-bot')



# if you want to be sent a DM each time a specific user enters
# a voice channel, use !ping-me [name]
@bot.command(name='ping-me', help='you will receive a DM whenever the user enters a voice channel')
async def ping_me(ctx, user_name: str):
    if ctx.channel.name != 'join-bot':
        await ctx.send('Commands must be specified in the join-bot channel')
        return 

    user = discord.utils.get(ctx.guild.members, name=user_name)

    if ctx.message.author.id == user.id:
        await ctx.send(f'Cannot use !ping-me on yourself')
        return 

    if user:
        users_to_ping.setdefault(user.id, set()).add(ctx.message.author.id)
    else:
        await ctx.send(f'{user_name} is not in this server or a typo.')    
    


@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



bot.run(TOKEN)