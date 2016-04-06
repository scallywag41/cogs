import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio
from translate import translator

class Translate:
    """Translate to Sweetish for trigger"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sweet(self, input):
        """Translates your text to sweetish for trigger."""
        try:
                priceUSD = result['data']['prices'][1]['price']
                await self.bot.say("BTC PRICE " + priceUSD)
        except:
            await self.bot.say("Error.")


def setup(bot):
    n = Bitcoin(bot)
    bot.add_cog(n)
