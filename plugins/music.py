from kutana import Plugin, Attachment, get_path


plugin = Plugin(name="Music", description="Send music")


@plugin.on_commands(["m"])
async def _(msg, ctx):
    with open(get_path(__file__, "assets/09. car_de_luxe.mp3"), "rb") as fh:
        audio_message = Attachment.new(fh.read(), "car_de_luxe.mp3", "voice")

    await ctx.reply("Audio message", attachments=audio_message)
