import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio

class Bitcoin:
    """Bitcoin commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def btc(self):
        """BTC price in USD"""
        search = "https://chain.so/api/v2/get_price/BTC/USD"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
                exchangeUSD = result['data']['prices'][1]['exchange']
                currencyUSD = result['data']['prices'][1]['price_base']
                priceUSD = result['data']['prices'][1]['price']
                await self.bot.say("BTC PRICE " + priceUSD)
        except:
            await self.bot.say("Error.")


def setup(bot):
    n = Bitcoin(bot)
    bot.add_cog(n)
