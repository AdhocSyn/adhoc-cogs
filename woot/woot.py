import discord
from discord.ext import commands

class woot:
    """woot: cheers when a user types \o/"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def woo(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("Huzzah! \o/")

def setup(bot):
    bot.add_cog(woot(bot))