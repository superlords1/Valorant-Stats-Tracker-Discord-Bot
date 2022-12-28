import discord
from discord import app_commands
from discord.ext import commands
from stats import getCompData
from utils import get_url

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.command(name = "stats")
async def stats(ctx, args):
    if "#" not in args:
        await ctx.send(embed = discord.Embed(title = "Please send your username followed by the tag"))
        return
    username_tag = args.split("#")
    url = get_url(username_tag[0], username_tag[1])
    
    await ctx.send(embed = getCompData(url, username_tag))


bot.run("MTA1NzMxMTYwMDM4MzYzOTY1Mg.GstKc9.D9_A52AKemEooeuUelMd6Fp94mGp4nvGKFNLLU")
