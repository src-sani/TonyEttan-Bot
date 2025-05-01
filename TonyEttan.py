import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
# Enable required intents
intents = discord.Intents.default()  # Get the default intents
intents.message_content = True  # Enable message content intent (for reading message content)
intents.members = True  # Enable member intent (for accessing member information)
intents.presences = True  # Enable presence updates (optional)

# Create bot with the intents enabled
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

# Event: When a new member joins the server
@bot.event
async def on_member_join(member):
    print(f"New member joined: {member.display_name}")  # Debugging: Check if the event is triggered

    # Get the category where your 'self-intro' channel is located (replace 'YourCategory' with the category name)
    category = discord.utils.get(member.guild.categories, name='Community Zone')  # Replace with your category name

    if category:
        # Get the 'self-intro' channel within that category
        intro_channel = discord.utils.get(category.text_channels, name='self-intro')

        if intro_channel:
            # Create the link to the intro channel
            intro_channel_link = intro_channel.mention
            print(f"Intro channel found: {intro_channel.name}")  # Debugging: Confirm intro channel

            try:
                # Send a welcome message with a link to the intro channel
                await member.send(
                    f"Hey {member.display_name}, welcome to The Arcane Circle! 🎉. Please introduce yourself in {intro_channel_link} and let us know a bit about you. Explore the community😊")
            except discord.errors.Forbidden:
                print(f"Could not send DM to {member.display_name}. The user may have DMs disabled.")
        else:
            print(f"Intro channel not found in category {category.name}.")  # Debugging: Intro channel not found
    else:
        print("Category not found!")  # Debugging: Category not found

bot.run(TOKEN)

