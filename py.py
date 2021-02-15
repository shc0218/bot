import discord
import asyncio
from discord.utils import get
from discord.ext import commands

client = discord.Client()

token = "ODEwODQ3ODU3ODAwMjQ5Mzg1.YCpm6g.v3bX-10ScBlOOYN6axNqRvWk4KQ"

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.name)
    print("봇시작!")
    game = discord.Game("연초서버 확인")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message,member: discord.Member=None):
    if message.content == "!인증":
        await message.author.add_roles(get(message.guild.roles, name="[💚일반 유저💚]"))
        await message.author.remove_roles(get(message.guild.roles, name="[💚새 유저💚]"))
        await message.channel.send(str(message.author) + "에게 역할이 적용되었습니다.")
    if message.content == "!범법자":
        member = member or message.author
        await member.add_roles(get(message.guild.roles, name="[📵 범법자 📵]"))
        await message.channel.send(str(member) + "를 범법자로 보냈습니다.")



client.run(token)
