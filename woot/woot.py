import discord
from discord.ext import commands
import random

class woot:
    """woot: cheers when a user types \o/"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def woo(self):
        """This does stuff!"""

        words = ['Huzzah!', 'Woo!', 'Hurrah!']
        out = random.choice(words)
        await self.bot.say(out+ " \o/")

def setup(bot):
    bot.add_cog(woot(bot))