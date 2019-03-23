import discord
import json
import os
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN= 'NTU4NTg4MjUyNjE4MjI3NzEz.D3fipg.IgGf81X7eIzCPi4oxomQtVT3yOo'

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')
os.chdir(r'C:\Users\User\Desktop\Autist bot')

@bot.event
async def on_ready():
  await bot.change_presence(game=discord.Game(name= 'Fortnite'))
  print('Bot on')

@bot.command(pass_contex=True)
async def help():

  embed = discord.Embed(
    colour = discord.Colour.purple()
  )

  embed.set_author(name= 'Помощь')
  embed.add_field(name= "help", value= "Покажет то что вы сейчас смотрите -_-")
  embed.add_field(name= 'hi', value='Бот приветствуется c вами')
  embed.add_field(name= "im", value= "Бот расскажет про себя")
  embed.add_field(name= "info", value= "Покажет инфу про человека которого вы укажите ")
  await bot.say(embed=embed)

@bot.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name= 'AUTIST')
  await bot.add_roles(member, role)

@bot.command()
async def hi(): await bot.say('Приветсвую вас в нашем раю!')

@bot.command()
async def im():
  await bot.say("Я бот созданный великим программистом felon! Я создан толька для Autism community!")

@bot.command()
async def echo(*args):
  output = ''
  for word in args:
    output += word
    output += ' '
  await bot.say(output)

@bot.command()
async def info(user: discord.User):
  emb = discord.Embed(title= "Info", color= 0xFFA2A2)
  emb.add_field(name= "Name", value= user.name)
  emb.set_author(name= bot.user.name)
  emb.set_footer(text= "Required by", icon_url= user.avatar_url)
  await bot.say(embed= emb)



bot.run(TOKEN)
