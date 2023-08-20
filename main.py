import discord
from discord import app_commands


class aclient(discord.Client):

    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('Азимов прибыл.')

    async def on_message(self, message):
        if "привет" in message.content.lower() and "азимов" in message.content.lower() and not message.author.bot:
            channel = message.channel
            await channel.send("Угу... Если это что-то не очень важное то попрошу не отвлекать...")
        elif "asimov" in message.content.lower() or "азимов" in message.content.lower() and not message.author.bot:
            channel = message.channel
            await channel.send('А, чего звал?')


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="info", description="Кто я")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Видимо тебе память отшибло? Позволь напомнить, я Азимов - "
                                            "человек, ответственный за Научный совет и член Совета Вавилонии. Я "
                                            "отвечаю за ведение научных и технических дел в Вавилонии. Я полностью "
                                            "посвятил себя научным исследованиям и уже добился нескольких огромных "
                                            "достижений в молодом возрасте, однако к сожалению у меня напрочь "
                                            "отсутствуют социальные навыки. Поэтому не всегда могу выразить мысль "
                                            "правильно, не думайте, что я злой.")


client.run("")
