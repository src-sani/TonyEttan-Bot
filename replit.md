# Discord Bot - TonyEttan

## Overview
This is a Discord bot called TonyEttan that welcomes new members to "The Arcane Circle" server. The bot sends personalized direct messages to new members when they join the server.

## Project Setup
- **Language**: Python 3.11
- **Main File**: TonyEttan.py
- **Dependencies**: discord.py, python-dotenv

## Architecture
- **Bot Type**: Discord bot using discord.py library
- **Command Prefix**: `!`
- **Intents**: Message content, members, and presences enabled
- **Features**:
  - Ping command for testing
  - Auto-welcome messages for new members
  - DM new members with a welcome message

## Configuration
- **Required Secret**: `DISCORD_TOKEN` - The Discord bot token for authentication
- **Workflow**: Runs `python TonyEttan.py` in console mode

## Recent Changes
- 2025-09-30: Initial setup in Replit environment
  - Installed Python 3.11
  - Installed dependencies (discord.py, python-dotenv)
  - Configured workflow to run the bot
  - Updated .gitignore with Python-specific patterns

## How to Run
1. Set the `DISCORD_TOKEN` secret in the Replit Secrets tab
2. The bot will automatically run via the configured workflow
3. The bot will log in and be ready to welcome new members
