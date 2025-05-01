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
    print(f"✅ Bot is logged in as {bot.user}")

# Event: When a new member joins the server
@bot.event
async def on_member_join(member):
    print(f"👋 New member joined: {member.display_name}")

    try:
        await member.send(
            f"Hey {member.display_name}, welcome to The Arcane Circle! 🎉\n"
            "Please introduce yourself in the #self-intro channel and explore the community. 😊"
        )
        print(f"✅ Welcome message sent to {member.display_name}")
     except Exception as e:
        print(f"❌ Could not send DM to {member}: {e}")

# Run the bot
bot.run(TOKEN)
