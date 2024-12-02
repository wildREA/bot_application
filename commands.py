import os
import pytz
import random
import sqlite3
import discord
from io import BytesIO
from typing import Optional
import matplotlib.pyplot as plt # type: ignore
from discord import app_commands
from collections import Counter
from discord.ext import commands
from collections import defaultdict
from discord.ui import Button, View
from dateutil.relativedelta import relativedelta # type: ignore
from datetime import datetime, timedelta, timezone

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        # Variables
        self.bot = bot
        # Database
        self.DATABASE_PATH = "server_data.db"
        self.init_db()
        # Cogs defined
        print("CommandsCog initialized!")

# Initializes database
    def init_db(self):
        try:
            conn = sqlite3.connect(self.DATABASE_PATH)
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS user_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    server_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    event_type TEXT NOT NULL CHECK(event_type IN ('join', 'leave')),
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            conn.close()
            print("Database initialized.")
            print(f"Database path: {os.path.abspath(self.DATABASE_PATH)}")
        except Exception as e:
            print(f"Error initializing database: {e}")

# Adds cog
async def setup(bot):
    print("Loading CommandsCog...")
    await bot.add_cog(CommandsCog(bot))
