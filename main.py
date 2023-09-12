import discord
from discord import app_commands
from determinant import Determinant
from build import Build
import sqlite3


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


async def on_message(message):
    if "привет" in message.content.lower() and "азимов" in message.content.lower() and not message.author.bot:
        channel = message.channel
        await channel.send("Угу... Если это что-то не очень важное то попрошу не отвлекать...")
    elif "asimov" in message.content.lower() or "азимов" in message.content.lower() and not message.author.bot:
        channel = message.channel
        await channel.send('А, чего звал?')


client = aclient()
tree = app_commands.CommandTree(client)
determinant = Determinant()


@tree.command(name="info", description="Кто я")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Видимо тебе память отшибло? Позволь напомнить, я Азимов - "
                                            "человек, ответственный за Научный совет и член Совета Вавилонии. Я "
                                            "отвечаю за ведение научных и технических дел в Вавилонии. Я "
                                            "посвятил себя научным исследованиям и могу сказать, что добился "
                                            "нескольких огромных"
                                            "достижений в столь молодом возрасте.")


@tree.command(name="build", description="Сборка фрейма и советы")
async def bld(interaction: discord.Interaction, frame: str):
    frameinf = determinant.determination(frame)
    if frameinf:
        try:
            build = Build()
            builds = build.build(frameinf[0].lower())
            embed = []
            keys = [*builds.keys()]
            items = [*builds.values()]
            embedVar = discord.Embed(title=f"{' '.join(frameinf[2])} {frameinf[1]} - {frameinf[0]} {frameinf[3]}",
                                     description="Сборки")
            embedVar.set_thumbnail(url=f"{frameinf[4]}.png")
            for i in range(len(keys)):
                embedVar.add_field(name=f"{keys[i]}", value="", inline=False)
                embedVar.set_image(url=f"{items[i]}.png")
                embed.append(embedVar)
                embedVar = discord.Embed()
            await interaction.response.send_message(embeds=embed)
        except IndexError:
            await interaction.response.send_message("Не помню такого фрейма, если честно... Может быть он вскоре "
                                                    "появится...")
    else:
        await interaction.response.send_message("Не помню такого фрейма, если честно... Может быть он вскоре "
                                                "появится...")


client.run("")
