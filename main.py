from dotenv import dotenv_values
import discord
from discord.ext import commands
import lyricsgenius as lg


# import token from .env file
env = dotenv_values(".env") # will give us a dictionary with all values from .env


# initialize the genius API
genius = lg.Genius(env["GENIUS_TOKEN"])


# initialize the bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="-", intents=intents, help_command=None)


# * ============
# * Commands
# * ============

# help command
@bot.command()
async def help(ctx, arg=""):
    embed=(discord.Embed(title="__List of Commands__",  color=0xE10101)
                        .add_field(name="-help", value="Get information on a command.", inline=False)
                        .set_footer(text="For more information on each command use -help [command]"))
    await ctx.send(embed=embed)

# testing genius API command
@bot.command()
async def test(ctx):
    # todo use arg as a way to pass a full string
    # todo we can then use a lookup system using *arg

    song = genius.search_song("Fly Me to the Moon", "Frank Sinatra")
    await ctx.send(song.lyrics)


# run the bot
bot.run(env["TOKEN"])
