from email import message
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Rogerrr')
 
@bot.command(name='del')
async def delete(ctx, number_of_message : int):
    #recupere l'historique du salon 
    message = await ctx.channel.history(limit=number_of_message +1).flatten()
    pass

    for m in message:
        await m.delete()
    

bot.run('TOKEN')
