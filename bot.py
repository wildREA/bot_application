import os
import discord
import tracemalloc
from discord.ext import commands
from flask import Flask
from threading import Thread

# Flask setup
app = Flask("")

@app.route("/")
def index():
    return "Bot is running!"

def run():
    # No...

# Runs Flask server in separate thread to keep as active
thread = Thread(target=run)
thread.start()

# Stats tracemalloc
tracemalloc.start()

# Loads token
TOKEN = os.getenv("TOKEN")

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Loads cogs
async def load_cogs():
    for cog in ["commands", "events"]:
        try:
            await bot.load_extension(f"cogs.{cog}")
            print(f"Loaded cog: {cog}")
        except Exception as e:
            print(f"Failed to load cog {cog}: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Syncing commands...")
    await load_cogs()  # Await the load_cogs coroutine now
    await bot.tree.sync()  # Awaits until sync
    print("Commands synced!")

# Run bot
bot.run(TOKEN)
