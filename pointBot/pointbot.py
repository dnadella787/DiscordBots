# look into add_check to automate the checks rather than do each one yourself maybe?
# its a global check
# convert into bbot for personal server usage
# test out server tomorrow


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



class member:
    def __init__(self, name):
        self.name = name
        self.points = 250 


member_list = []



@bot.command(name='start', help='create a channel, must be role role1, role2')
@commands.has_any_role('role1', 'role2')
async def start(ctx):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name='point-bot')

    if not existing_channel:
        print(f'Creating a new channel for commands: point-bot')
        await guild.create_text_channel('point-bot')




@bot.command(name='add', help='add a user to the point list, starts at 250')
@commands.has_any_role('role1', 'role2')
async def add_member(ctx, user_name: str):
    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    for memb in member_list:
        if memb.name == user_name:
            message = f'{user_name} is already in point list.Current point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
            await ctx.send(message)
            return


    user = discord.utils.get(ctx.guild.members, name=user_name)

    if user:
        member_list.append(member(user.name))
        member_list.sort(key = lambda x: x.points, reverse=True)
        message = f'{user.name} was added to point list. The new point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
        await ctx.send(message)
    else:
        await ctx.send(f'{user_name} does not exist in server or typo')




@bot.command(name='add-role', help='add all users that are under a certain role')
@commands.has_any_role('role1', 'role2')
async def add_member_role(ctx, role_name: str):
    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    role = discord.utils.get(ctx.guild.roles, name=role_name)
    curr_names = [x.name for x in member_list]

    if role:
        for user in ctx.guild.members:
            if role in user.roles and user.name not in curr_names:
                member_list.append(member(user.name))
        
        member_list.sort(key = lambda x: x.points, reverse=True)
        message = f'{role.name} has been added to point list. The new point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
        await ctx.send(message)
    else:
        await ctx.send(f'{role_name} does not exist in server or typo')




@bot.command(name='remove', help='remove a user from the point list')
@commands.has_any_role('role1', 'role2')
async def remove_member(ctx, user_name: str):
    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    if len(member_list) == 0:
        await ctx.send('Point list is empty, add members first')
        return 


    user = discord.utils.get(ctx.guild.members, name=user_name)

    if user:
        in_member_list = False  
        for i in range(len(member_list)):
            if member_list[i].name == user.name:
                del member_list[i]
                in_member_list = True 
                break

        if not in_member_list:
            message = f'{user.name} was never in the point list. Current point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
            await ctx.send(message)
            return 

        if len(member_list) == 0:
            message =  f'{user.name} was removed from point list. Point list is now empty.'
        else:
            member_list.sort(key = lambda x: x.points, reverse = True)
            message = f'{user.name} was removed from point list. The new point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
        
        await ctx.send(message)
    else:
        await ctx.send(f'{user_name} does not exist in server or typo')




@bot.command(name='increase', help='increase number of points by some number')
@commands.has_any_roles('role1', 'role2')
async def increase(ctx, user_name: str, num: int):
    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    if len(member_list) == 0:
        await ctx.send('Point list is empty, add members first')
        return 

    if num < 0:
        await ctx.send('Negative number used. To decrease points use !decrease command.')
        return 

    user = discord.utils.get(ctx.guild.members, name=user_name)

    if user:
        in_member_list = False  
        for i in range(len(member_list)):
            if member_list[i].name == user.name:
                member_list[i].points += num 
                in_member_list = True 
                break

        if not in_member_list:
            message = f'{user.name} is not in the point list. Current point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
            await ctx.send(message)
            return 

        member_list.sort(key = lambda x: x.points, reverse = True)
        message = f'New point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
    else:
        await ctx.send(f'{user_name} does not exist in server or typo')




@bot.command(name='decrease', help='decrease number of points by some number')
@commands.has_any_roles('role1', 'role2')
async def decrease(ctx, user_name: str, num: int):
    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    if len(member_list) == 0:
        await ctx.send('Point list is empty, add members first')
        return 

    if num > 0:
        await ctx.send('Negative number used. To increase points use !increase command.')
        return 

    user = discord.utils.get(ctx.guild.members, name=user_name)

    if user:
        in_member_list = False  
        for i in range(len(member_list)):
            if member_list[i].name == user.name:
                member_list[i].points -= num 
                in_member_list = True 
                break

        if not in_member_list:
            message = f'{user.name} is not in the point list. Current point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
            await ctx.send(message)
            return 

        member_list.sort(key = lambda x: x.points, reverse = True)
        message = f'New point list: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
    else:
        await ctx.send(f'{user_name} does not exist in server or typo')




@bot.command(name='print-points', help='print out the point list')
async def print_points(ctx):
    if len(member_list) == 0:
        await ctx.send('point list is empty, add members first')
        return 

    if ctx.channel.name != 'point-bot':
        await ctx.send('Commands must be specified in the point-bot channel')
        return 

    message = f'Point List: \n - ' + '\n - '.join([f'{memb.name}: {memb.points}' for memb in member_list])
    await ctx.send(message)
    



@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



bot.run(TOKEN)