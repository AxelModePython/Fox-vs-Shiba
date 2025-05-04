import discord
from discord.ext import commands
from detector import identify
import os
import uuid

# Inisialisasi bot
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def upload(ctx):
    # Memeriksa apakah ada lampiran
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            # Mendapatkan nama file dan membuat nama unik
            unique_filename = f"{uuid.uuid4()}_{attachment.filename}"
            # Menyimpan lampiran
            await attachment.save(os.path.join('image', unique_filename))
            hasil = identify('image/' + unique_filename)
            if hasil == 'Shiba inu':
                await ctx.send('That animal is a shiba inu.')
            else:
                await ctx.send('That animal is a fox')
    else:
        await ctx.send("Tidak ada gambar yang diunggah. Silakan unggah gambar.")

# Jalankan bot
bot.run('Token')