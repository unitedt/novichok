from kutana import Plugin, Attachment, HandlerResponse, get_path
import os
import re

plugin = Plugin(name="Music", description="Send music")


@plugin.on_commands(["m"])
async def _(msg, ctx):
    files = files_find("/home/hord/Музыка/", ctx.body)
    
    if (len(files) == 0):
        await ctx.reply("Нет такой музыки...")
        
    else:
        filepath = files.pop()
        
        with open(get_path(__file__, filepath), "rb") as fh:
            audio_message = Attachment.new(fh.read(), os.path.basename(filepath), "voice")
    
        await ctx.reply(os.path.basename(filepath), attachments=audio_message)

def files_find(catalog, f):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if re.search(f, name, re.IGNORECASE)]
    return find_files
