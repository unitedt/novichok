import asyncio
import random
import pymysql
from kutana import Plugin

plugin = Plugin(name="Jokes", description="Send random jokes in random time to subscribers")

subscribers = []
conn = pymysql.connect('localhost', 'root', '*', 'novichok')

async def bg_loop(vk):
    while True:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT anek FROM anekdots ORDER BY rand() LIMIT 1")
            joke = cursor.fetchone()
        
        for sub in subscribers:
            await vk.send_message(sub, joke[0])

        await asyncio.sleep(random.randrange(5, 30))

@plugin.on_start()
async def _(app):
    backend = app.get_backends()[0]

    # Run only if first backend is Vkontakte
    if backend.get_identity() == "vkontakte":
        asyncio.ensure_future(bg_loop(backend))

@plugin.on_commands(["jokes sub"])
async def _(msg, ctx):
    subscribers.append(msg.receiver_id)
    await ctx.reply("OK")


@plugin.on_commands(["jokes unsub"])
async def _(msg, ctx):
    subscribers.remove(msg.receiver_id)
    await ctx.reply("OK")
