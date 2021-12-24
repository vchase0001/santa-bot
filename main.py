import discord
import random
import os
from dotenv import load_dotenv
import asyncio
import requests
import json

load_dotenv()


def christmas_joke():
	r = requests.get('https://v2.jokeapi.dev/joke/Christmas')
	data = json.loads(r.text)
	return [data['setup'], data['delivery']]



#intents = discord.Intents().all()
client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=" out for Christmas cookies."))
	print('We have logged in as {0.user}'.format(client))
	#text_channel = client.get_channel(835119138338242622)
	#await client.get_channel(837231785778610226).send(f"@everyone, it's Go Skateboarding Day today (June 21).\nLet\'s skate together - post a short video in the {text_channel.mention} chat!", file=discord.File('skate.mp4'))


@client.event
async def on_message(message):
	#################################
	if message.author == client.user:
		return
	#################################
	
	if message.content.lower().startswith('tell me a joke, santa'):
		joke = christmas_joke()
		await message.reply(joke[0])
		await asyncio.sleep(2)
		await message.channel.send(joke[1])
	
	if 'merry christmas' in message.content.lower() or 'happy holidays' in message.content.lower() or 'happy christmas' in message.content.lower():
		greeter = f"<@{message.author.id}>"
		saved_greetings = [
		f"Merry Christmas, {greeter}! Best wishes for a joyous Christmas filled with love, happiness and prosperity.",
		f"Merry Christmas, {greeter}! May all that is beautiful, meaningful and brings you joy be yours this holiday season and throughout the coming year.",
		f"Merry Christmas to you, {greeter}! Wishing you all the happiness your holiday can hold!",
		f"May your holidays sparkle with joy and laughter. Merry Christmas, {greeter}!",
		f"Merry Christmas, {greeter}! I hope the magic of Christmas fills every corner of your heart and home with joy — now and always.",
		f"I wish you love, joy and peace today, tomorrow and always. Merry Christmas, {greeter}!",
		f"May your family have a holiday season that is full of wonderful surprises, treats and nonstop laughter. Merry Christmas, {greeter}!",
		f"Merry Christmas, {greeter}! Wishing you all the best this holiday season!",
		f"Wishing you a Christmas that's merry and bright, {greeter}!",
		f"We hope you have a safe and relaxing holiday season. Merry Christmas to you, {greeter}!",
		f"I hope your holiday season is full of peace, joy and happiness. Merry Christmas, {greeter}!",
		f"Merry Christmas with lots of love, {greeter}.",
		f"I hope your Christmas is filled with joy this year, {greeter}. Merry Christmas!",
		f"Happy Holidays, {greeter}! I hope all of your Christmas wishes come true.",
		f"Wishing you a white Christmas, {greeter}! (And when you run out of white, just open a bottle of red).",
		f"A Christmas reminder, {greeter}: Don’t try to borrow any money from elves... they're always a little short! Have a Merry Christmas!",
		f"Merry Christmas {greeter}! Wishing you hope, peace and lots of Christmas cookies this holiday season!",
		f"They say the best Christmas gifts come from the heart… but cash and gift cards do wonders too! Happy Holidays, {greeter}!",
		f"Remember, Santa is watching. Everything. Yes, even that. Anyway, Merry Christmas, {greeter}!",
		f"Merry Christmas, {greeter}! May your happiness be large and your bills be small.",
		f"Merry Christmas {greeter}! This holiday season, let’s make it a point to cherish what’s truly important in our lives: cookies.",
		f"I told Santa you were good this year and sent him a link to your Pinterest board. Merry Christmas to you, {greeter}!",
		f"Happy Holidays, {greeter}! This Christmas, may your family be functional and all your batteries be included.",
		f"Merry Christmas, {greeter}! I put so much thought into your gift that now it's too late to get it.",
		f"Christmas is mostly for children. But we adults can enjoy it too, until the credit card bills arrive. Happy Holidays, {greeter}!",
		f"Eat. Drink. Be Merry. Have a wonderful Christmas, {greeter}!"
		]
		await message.reply(random.choice(saved_greetings))

		
@client.event
async def on_voice_state_update(member, before, after):
	if before.channel is None and after.channel is not None:
		if member == client.user:
			return
		else:
			chance = random.randint(1,3)
			if chance == 3:
				#print(after.channel.members)
				#print(member.voice)
				choices = ['hohoho.mp3', 'hohoho2.mp3']
				player = await member.voice.channel.connect()
				player.play(discord.FFmpegPCMAudio(random.choice(choices)))
				while player.is_playing():
					await asyncio.sleep(1)
				await player.disconnect()

client.run(os.getenv('TOKEN'))
