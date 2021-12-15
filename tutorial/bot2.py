import os
import random
import discord 

from discord.ext import commands 
from dotenv import load_dotenv 

load_dotenv()
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='hi', help='responds back with a hi statement')
async def hi(ctx):
    await ctx.send("hello, how are you?")


@bot.command(name="dice_roll", help='simulate roling a dice, usage: !dice_roll [# of dice] [# of number of sides]')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [str(random.choice(range(1, number_of_sides + 1))) for _ in range(number_of_dice)]
    await ctx.send(', '.join(dice))



@bot.command(name='create-channel', help='create a channel, must be role eskree, eskwoop')
@commands.has_any_role('eskree', 'eskwoop')
async def create_channel(ctx, channel_name: str):
    if ctx.channel.name != 'bob':
        await ctx.send('Commands must be specified in the bob channel')
        return 
        
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


bot.run(TOKEN) 