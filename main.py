import pythonbible as bible

#MTA2MjY5MTU1OTkyMjk5OTM2Ng.GsZygD.si81qz8OybNrq82LF6_UQm8Jdqls0ao_l70x_A
import discord
from discord.ext import commands

TOKEN = 'MTA4NjQ4NDgzNjc5MDg0NTQ2Mg.GUUUpp.qgOvCJEigVXxiIkN3RaPW_jsGh2CdADffzW0uc'

intents = discord.Intents.default()
intents.message_content = True




client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if message.author == client.user:
        return

    if channel == "bible":
        text = user_message
        y = 0
        references = bible.get_references(text)
        formatted_reference = bible.format_scripture_references(references)
        x = formatted_reference.split(";")
        for i in range(0, len(x)):
            await message.channel.send(f'**{x[i]}**')
            try:
                reference = bible.get_references(formatted_reference)[y]  # Get first (and only) Reference object from the list
                y += 1
                verse_ids = bible.convert_reference_to_verse_ids(reference)
                for i in list(verse_ids):
                    verse_text = bible.get_verse_text(i, version=bible.Version.KING_JAMES)
                    print(verse_text)
                    try:
                        last_three = int(str(i)[-3:])
                        await message.channel.send(f'{last_three}: {verse_text}')
                    except discord.errors.HTTPException:
                        await message.channel.send("Hi")
            except IndexError:
                pass




client.run(TOKEN)







