from sh import ping, nslookup, whois
import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import asyncio

class Networking:
    """Networking Commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bping(self, someip):
        """Ping an IP/FQDN"""
        try:
            await self.bot.say(ping("-c 4 ",someip))
        except Exception as e:
            print(e)

    @commands.command()
    async def bnslookup(self, someip):
        """nslookup IP/FQDN"""
        try:
            await self.bot.say(nslookup(someip))
        except Exception as e:
            print(e)

    @commands.command()
    async def bwhois(self, someip):
        """whois IP/FQDN"""
        try:
            whatever = whois(someip)
            self.bot.say(whatever)
        except Exception as e:
            print(e)


def setup(bot):
    n = Networking(bot)
    bot.add_cog(n)


