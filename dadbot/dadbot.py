import discord
from discord.ext import commands
import asyncio
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
import os

class dadbot:
    """Makes dad jokes automatically!"""

    def __init__(self, bot):
        self.bot = bot
        self.settingspath = "data/dadbot/settings.json"
        self.settings = dataIO.load_json(self.settingspath)

    def save_db(self):
        dataIO.save_json(self.dbpath, self.db)


    @commands.group(name="dadbot", pass_context=True, no_pm=True )
    @checks.admin
    async def dadbot(self, ctx):
        """Manage dadbot settings"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @dadbot.command(name="on", pass_context=True, no_pm=True)
    async def _dadbot_on(self, ctx, msg):
        """Activates dadbot in a channel"""
        if msg.channel.id in self.settings["channels"]:
            await self.bot.say("Dadbot already activated in:" + msg.channel.id)
        else:
            self.settings["channels"].append(msg.channel.id)
            dataIO.save_json(self.settingspath, self.settings)
            await self.bot.say("Dadbot activated in: " + msg.channel.id)

    @dadbot.command(name="off", pass_context=True, no_pm=True)
    async def _dadbot_off(self, ctx, channel):
        """Deactivates dadbot in a channel"""
        if msg.channel.id in self.settings["channels"]:
            self.settings["channels"].remove(msg.channel.id)
            dataIO.save_json(self.settingspath, self.settings)
            await self.bot.say("Dadbot deactivated in: " + msg.channel.id)
        else:
            await self.bot.say("Dadbot was not active in:" + msg.channel.id)

    def is_command(self, msg):
        if callable(self.bot.command_prefix):
            prefixes = self.bot.command_prefix(self.bot, msg)
        else:
            prefixes = self.bot.command_prefix
        for p in prefixes:
            if msg.content.startswith(p):
                return True
        return False

    async def on_message(self, message):
        if message.channel.id not in self.settings["channels"]:
            return
        if message.author == self.bot.user and not self.settings.get("bot", False):
            return
        if self.is_command(message):
            return
        try:
            out = ""
            building = False
            triggers = ["i'm", "im"]
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            words = message.split(" ")

            for word in words:
                if lower(word) in triggers:
                    active = True
                elif building:
                    if word[-1] in char:
                        word = word.strip(char)
                        break
                    out+=word
            if building:
                await self.bot.say("Hi {}, I'm Dad!".format(out))

        except discord.errors.HTTPException:
            pass



def check_folders():
    f = "data/dadbot"
    if not os.path.exists(f):
        print("creating data/dadbot directory")
        os.mkdir(f)

def check_files():
    setp = 'data/dadbot/settings.json'
    if not os.path.isfile(setp):
        default = {}
        print('Creating default dadbot/settings.json...')
        dataIO.save_json(setp, default)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Mycog(bot))
