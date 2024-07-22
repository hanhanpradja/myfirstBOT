import discord
from discord.ext import commands
from kodland_utils import *
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('images'))
    with open(f'images/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# DAFTAR SAMPAH

organik = ['sayur busuk', 'makanan basi', 'kotoran hewan', 'dedaunan']
kertas = ['kardus', 'kertas gorengan', 'kertas', 'paperbag', 'tisu']
plastik = ['kresek', 'botol plastik', 'cup plastik', 'mangkok plastik']
logam = ['kaleng', 'baterai', 'hp', 'elektronik', 'kabel', 'besi berkarat']

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('Apa sampah yang anda ingin periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    # PENGECEKAN
    if message.lower() in organik:
        await ctx.send('ITU ADALAH SAMPAH **ORGANIK**')
        await ctx.send('Sebaiknya, kalian gunakan itu menjadi *PUPUK*')
    elif message.lower() in kertas:
        await ctx.send('ITUMAH SAMPAH **KERTASS**')
        await ctx.send('Bagusnya sih kalian kumpulkan lalu buat lagi jadi kertas')
        await ctx.send('hmm.. atau kalian jadikan kerajinan unikk')
    elif message.lower() in plastik:
        pass
    elif message.lower() in logam:
        pass
    else:
        await ctx.send('DUDE,, ITUMAH BUKAN SAMPAH!')
