import discord
from discord.ext import commands

import datetime
import os

class HuBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="h!",
            intents=discord.Intents.all(),)
        self.start_time = datetime.datetime.now()

    async def on_ready(self):
        for file in os.listdir(f"./cogs"):
            if file.endswith(".py") and not file.endswith("_"):
                try:
                    self.load_extension(f"cogs.{file[:-3]}")
                    print(f"Loaded extension: cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Could not loaded cogs.{file[:-3]} {e}")
        print(f"Logging at {self.user.name} ({self.user.id})")
