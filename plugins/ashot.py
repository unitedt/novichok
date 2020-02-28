from kutana import Plugin


plugin = Plugin(name="Ashot", description="Ashot Kantaria")


@plugin.on_commands(["a"])
async def _(msg, ctx):
    await ctx.reply("Ашот Кантария был очень богатым человеком")
