import os
import random

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

bot.run(TOKEN) 