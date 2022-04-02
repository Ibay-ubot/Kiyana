import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 ]


@register(pattern="apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))

PERASAAN_STRING = ["gombal", 
                 "Iya", 
                 "Buang saja", 
                 "Kasian mana masih muda",
                 ]


@register(pattern="perasaan ?(.*)")
async def perasaan(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(PERASAAN_STRING))
