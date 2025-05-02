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
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Bot is logged in as {bot.user}")
    # Optional: Print connected servers (guilds)
    for guild in bot.guilds:
        print(f"Connected to: {guild.name} (id: {guild.id})")

# Ping command (for testing purposes)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Event: When a new member joins the server
@bot.event
async def on_member_join(member):
    print(f"👋 New member joined: {member.display_name}")

    try:
        await member.send(
            f"Hey {member.display_name}, welcome to The Arcane Circle! 🎉\n"
            "Please introduce yourself in the #self-intro channel and explore the community. 😊Appo enganaa!!! Polikkaa alleee??🥳"
        )
        print(f"✅ Welcome message sent to {member.display_name}")
    except discord.Forbidden:
        print(f"⚠️ Could not send DM to {member.display_name}. They may have DMs disabled.")
@bot.event
async def on_member_join(member):
    guild = member.guild
    system_channel = guild.system_channel

    # Try to find a fallback channel if system_channel is None
    if system_channel is None:
        # Replace 'general' with any known welcome/default channel in your server
        system_channel = discord.utils.get(guild.text_channels, name='system-messages')

    council_role = discord.utils.get(guild.roles, name="COUNCIL")  # Make sure role name matches exactly

    if system_channel and council_role:
        await system_channel.send(
            f"🎉 {member.mention} just joined the server!\n"
            f"{council_role.mention}, please welcome our new member!"
        )
        print(f"✅ Welcome message sent in {system_channel.name} for {member.display_name}")
    else:
        print("⚠️ Could not find system channel or Council role.")


# Run the bot
bot.run(TOKEN)
