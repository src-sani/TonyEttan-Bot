import discord
from discord.ext import commands
import os

# Retrieve the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Debugging: Check if the token is successfully retrieved
if TOKEN is None:
    print("ERROR: DISCORD_TOKEN is not set correctly.")
else:
    print("DISCORD_TOKEN found, proceeding with bot login...")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# Create the bot instance with the specified intents
bot = commands.Bot(command_prefix="/", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

# Start the bot using the token
bot.run(TOKEN)
