#this is a simple python calculator
#could be more, but ...
#you are welcome to add Kitty to your discord server (foc)
#copy and paste the link below to your browser, you must be login first
#https://discord.com/api/oauth2/authorize?client_id=786533215224987658&permissions=2048&scope=bot
#ps: please run this script to wake Kitty up

import discord
import os
import requests
import json
import random
import urllib
from replit import db
from keep_alive import keep_alive

#import math
from kittym import *

#from ftest import test
#test()

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person. Bots are too.!",
    "You are already a winner.", "Tomorrow is always a new day.",
    "Darkness can never stop the light of day."
]

if "responding" not in db.keys():
	db["responding"] = True


def get_mz(q):
	usr = os.getenv('MZ_USER')
	tok = os.getenv('MZ_TOKEN')

	q = q.replace(' ', '')
	#q=urllib.parse.urlencode(q)
	#print(q)

	response = requests.get("https://mathzilla.app/api.php?user=" + usr +
	                        "&token=" + tok + "&q=" + q)

	json_data = json.loads(response.text)
	ans = json_data['ans']
	return (ans)


#testing
#print(get_mz("1+1"))


def get_py(q):
	#q="math."+q
	try:
		#a=eval(q)
		a = eval_py(q)
		a = "Ans = " + str(a)
	except Exception as e:
		#print(e)
		a = 'Error = ' + str(e)
	return a


def get_help(q):
	a = kitty_help(q)
	return a


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	#response = requests.get("https://zenquotes.io/api/quotes/author/sun-tzu/key")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return (quote)


def get_fortune():
	fortune = requests.get("http://yerkee.com/api/fortune/wisdom")
	#fortune=requests.get("http://private-anon-0ce376ceb2-fortunecookie.apiary-proxy.com/v1/fortunes/1")
	json_data = json.loads(fortune.text)
	quote = json_data['fortune']
	return (quote)


def update_encouragements(encouraging_message):
	if "encouragements" in db.keys():
		encouragements = db["encouragements"]
		encouragements.append(encouraging_message)
		db["encouragements"] = encouragements
	else:
		db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
	encouragements = db["encouragements"]
	if len(encouragements) > index:
		del encouragements[index]
		db["encouragements"] = encouragements
		return True
	else:
		return False


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content

	#fun response
	if msg.startswith('Hi Kitty') or msg.startswith('Hi, Kitty'):
		await message.channel.send("Meeow, " + message.author.name + "!")
	if msg.startswith('Kitty hi') or msg.startswith('Kitty Hi'):
		await message.channel.send("Meeow, " + message.author.name + "!")
	if msg.startswith('Kitty Kitty') or msg.startswith('Kitty, Kitty'):
		await message.channel.send("Meeow, meow, " + message.author.name + "!")
	if msg.startswith('Hello Kitty') or msg.startswith('Hello, Kitty'):
		await message.channel.send("I'm not a toy.")

	if msg.startswith('Kitty inspire me'):
		quote = get_quote()
		await message.channel.send(quote)

	if msg.startswith('Kitty fortune cookies'):
		quote = get_fortune()
		await message.channel.send(quote)

	#autorepond to sad words
	if db["responding"]:
		options = starter_encouragements
		if "encouragements" in db.keys():
			options = options + db["encouragements"]
		if any(word in msg for word in sad_words):
			await message.channel.send(random.choice(options))

	if msg.startswith('Kitty help'):
		q = msg
		#print(q)
		ans = get_help(q)
		await message.channel.send(ans)

	if msg.startswith('Kitty blog'):
		q = 'Kitty help blog'
		#print(q)
		ans = get_help(q)
		await message.channel.send(ans)

	if msg.startswith('Kitty eval'):
		q = msg.split("Kitty eval ", 1)
		if len(q) == 1:
			return
		if len(q) == 2:
			q = q[1]
			ans = get_py(q)
		await message.channel.send(ans)

	if msg.startswith('Kitty calc'):
		q = msg.split("Kitty calc ", 1)[1]
		if len(q) == 1:
			return
		if len(q) == 2:
			q = q[1]
		ans = get_mz(q)
		#ans="Sorry, we are upgrading. Please use eval."
		await message.channel.send(ans)

	#event after this is for lm only, dm got no guild name
	if message.author.name != "lm":
		return
	if message.guild is not None and message.guild.name == "This is not a server.":
		if msg.startswith("$new"):
			encouraging_message = msg.split("$new ", 1)[1]
			update_encouragements(encouraging_message)
			await message.channel.send("New encouraging message added.")

		if msg.startswith("$del"):
			encouragements = []
			if "encouragements" in db.keys():
				index = int(msg.split("$del", 1)[1])
				if delete_encouragment(index):
					encouragements = db["encouragements"]
					await message.channel.send("Index " + str(index) +
					                           " is deleted.")
				else:
					await message.channel.send("Index " + str(index) +
					                           " is not in the list.")
			await message.channel.send(encouragements)

		if msg.startswith("$list"):
			i = 0
			if "encouragements" in db.keys():
				encouragements = db["encouragements"]
				#await message.channel.send(encouragements)
				for m in db["encouragements"]:
					await message.channel.send(str(i) + " => " + m)
					i += 1

		if msg.startswith("$responding"):
			responds = msg.split("$responding ", 1)
			if len(responds) == 1:
				await message.channel.send("Responding is set to " +
				                           str(db["responding"]))
			elif len(responds) == 2:
				value = responds[1]
				if value.lower() == "true":
					db["responding"] = True
					await message.channel.send("Responding is on.")
				else:
					db["responding"] = False
					await message.channel.send("Responding is off.")


#keep_alive()
client.run(os.getenv('TOKEN'))
