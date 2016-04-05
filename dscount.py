import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio
from datetime import datetime, time

class DarkSouls:
    """Dark Souls"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dscount(self):
        """Countdown to Dark Souls 3"""
        leaving_date = datetime.strptime('2016-04-12 00:00:00', '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        timedelta = leaving_date - now
        var_seconds = timedelta.days * 24 * 3600 + timedelta.seconds
        minutes, seconds = divmod(var_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        var_full = (days, hours, minutes, seconds)
        await self.bot.say("%d days, %d hours, %d minutes, %d seconds until DARK SOULS III!!!" % var_full)

def setup(bot):
    n = DarkSouls(bot)
    bot.add_cog(n)

