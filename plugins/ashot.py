from kutana import Plugin
import psutil
import time
import os


plugin = Plugin(name="Ashot", description="Ashot Kantaria")


@plugin.on_commands(["a"])
async def _(msg, ctx):
    process = psutil.Process(os.getpid())

#    taken_memory = int(process.memory_info().rss / 2**20)
#    taken_time = time.time() - msg.date

    await ctx.reply("Ашот Кантария был очень богатым человеком")
