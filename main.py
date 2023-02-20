import discord
import os
import random
import requests
import json
import wikipediaapi
import youtube_dl as yt
from discord.ext import commands, tasks
import pickle
#os.system("cls")

intents = discord.Intents.all()
client = discord.Client(intents=intents)



testnum = 0
testnum = pickle.load(open("testnumgilbert","rb"))

quotes = ["this is a quote", "squishing cum into my old wallet so i can find it by smell if i lose it", "youre a walnut"]
quotes = pickle.load(open("gilbertquotes","rb"))

todo = ["credits","music","words"]
todo = pickle.load(open("gilberttodo","rb"))

print("hi guy")
mee = "breh"
#GILBERT
wiki_wiki = wikipediaapi.Wikipedia('en')
hello_words=["howdy","hello","hi","yo","hey","greetings","hello there"]



@client.event
async def on_ready():
	print("we ready and im {0.user}".format(client))

@client.event
async def on_message(m):
	msg = m.content.lower()
	if m.author == client.user:
		return
	wiiii=True
#test 
	if msg.startswith("gilbert test"):
		wiiii = False
		global testnum
		testnum = testnum + 1
		pickle.dump(testnum,open("testnumgilbert","wb"))
		print ("Test has been used "+ str(testnum) + " times.")
		await m.reply("thats not how you test it")
#guessing game
	if msg.startswith("gilbert guessing game"):
		wiiii = False
		num = random.randint(0,100)
		await m.channel.send("0 to what number?")
		new_msg = await client.wait_for('message')
		if m.author != new_msg.author:
			if new_msg.author==client.user:
				new_msg = await client.wait_for('message')
			else:
				await m.channel.send("bruh start your own game")
				return
		try:
			int(new_msg.content)
		except ValueError:
			await m.reply("gotta be a number broski restart")
			return
		num = int(new_msg.content)
		num = random.randint(0,num)
		await m.reply("number has been genarated whats your first guess?")
		new_msg = await client.wait_for('message', timeout=60.0)
		gn=0
		if m.author != new_msg.author:
			await m.channel.send("bruh start your own game")
			return
		try:
			int(new_msg.content)
		except ValueError:
			await m.reply("gotta be a number broski restart")
			return
		cg = int(new_msg.content)
		while (cg !=num):
			gn+=1
			if cg>num:
				await m.reply("too high walnut\nguess again")
			if cg<num:
				await m.reply("too low walnut\nguess again")
			new_msg = await client.wait_for('message', timeout=60.0)
			if m.author != new_msg.author:
				await m.channel.send("bruh start your own game")
				return
			try:
				int(new_msg.content)
			except ValueError:
				await m.reply("gotta be a number broski restart")
				return
			cg = int(new_msg.content)
		if cg==num:
			gn+=1
			await m.reply("nice only took "+str(gn)+" guesses")
		else:
			await m.reply("@callan#8322 im broked")

#mmm
	if msg.startswith("gilbert nt"):
		wiiii=False
		mmm=int(msg.split("gilbert nt",1)[1])
		for x in range(mmm):
			await m.channel.send(x)

#gilbert help
	if msg.startswith("gilbert help"):
		wiiii = False
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.set_thumbnail(url=client.user.avatar_url)
		embed.add_field(name=("**help**"), value=('type gilbert + any of the following commands or type gilbert help and then the command for more details but not yet```\nquote\nadd quote\nall quotes\nhow many quotes\ntomboy\nstats player name\nwiki whatever\nhello\nflip a coin\nadd this and what you want gilbert to do```'))
		embed.set_footer(text="gilbert created by the_callan101")
		await m.channel.send(embed = embed)
#add this
	if msg.startswith("gilbert add this "):
		wiiii = False
		todo = pickle.load(open("gilberttodo","rb"))
		todo.append(msg.split("gilbert add this ",1)[1])
		pickle.dump(todo,open("gilberttodo","wb"))
		await m.channel.send("callan might do it")
#todo
	if msg.startswith("gilbert todo"):
		wiiii = False
		todo = pickle.load(open("gilberttodo","rb"))
		for x in todo:
			await m.channel.send(x)
#i finished
	if msg.startswith("gilbert i finished "):
		wiiii = False
		thingy = (msg.split("gilbert i finished ",1)[1])
		todo = pickle.load(open("gilberttodo","rb"))
		for x in todo:
			if thingy == x:
				todo.remove(x)
		pickle.dump(todo,open("gilberttodo","wb"))
		await m.channel.send("done")
#all quotes
	if msg.startswith("gilbert all quotes"):
		wiiii = False
		for x in quotes:
			await m.channel.send(x)
#addquote
	if msg.startswith("gilbert add quote "):
		wiiii = False
		quotes.append(msg.split("gilbert add quote ",1)[1])
		pickle.dump(quotes,open("gilbertquotes","wb"))
		await m.channel.send("ok")
#HOW MANY QUOTES
	if msg.startswith("gilbert how many quotes"):
		wiiii = False
		await m.channel.send(len(quotes))
#quote
	if msg.startswith("gilbert quote"):
		wiiii = False
		await m.channel.send(random.choice(quotes))

#if you say
	if msg.startswith("gilbert if you say"):
		headers = {
			'x-rapidapi-key':
			"eada209357msh8f365a92ad33226p178e88jsn7f5d0e81886e",'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
			}
		url1 = "https://wordsapiv1.p.rapidapi.com/words/"
		querystring = {"random":"true"}
		response = requests.request("GET", url1, headers=headers,params=querystring)
		data = json.loads(response.text)
		wiiii = False
		await m.channel.send(data["word"])
#fuck
	if msg.startswith("gilbert fuck"):
		wiiii = False
		await m.channel.send("what do u want")
#music
	if msg.startswith("gilbert play"):
		wiiii = False
		await m.channel.send("no")
#ignite stats
	if msg.startswith("gilbert stats "):
		wiiii = False
		player_name = (msg.split("gilbert stats ",1)[1])
		headers = ("")#removed for ignite reasons if you are trying to run this code and you see this either dm me on discord, vts or franz
		payload = {'player_name': player_name, 'fuzzy_search': True}
		r = requests.get("https://ignitevr.gg/cgi-bin/EchoStats.cgi/get_player_stats", headers=headers, params=payload)
		data = json.loads(r.text)
		#print(data["vrml_player"])
		embed = discord.Embed(colour=discord.Colour.orange())

		if (str(data["vrml_player"]) != "[]"):
			embed.set_thumbnail(url=data["vrml_player"]["player_logo"])

		embed.add_field(name=("**" + player_name + "**"), value=('```level       |   ' + str(data["player"][0]["level"]) + '\nGames       |   at least ' + str(data["player"][0]["game_count"]) +'\nGoals       |   at least ' + str(data["player"][0]["total_goals"]) + '\n3 pointers  |   at least ' + str(data["player"][0]["total_3_pointers"]) + '\n2 pointers  |   at least ' + str(data["player"][0]["total_2_pointers"]) + '\nwin rate    |   ' + str((data["player"][0]["total_wins"]) / (data["player"][0]["game_count"])) + "```"))
		embed.set_footer(text="stats powered by ignitevr.gg")
		await m.channel.send(embed = embed)
#wiki
	if msg.startswith("gilbert what\'s a ") and wiiii == True:
		wiiii = False
		page = wiki_wiki.page(msg.split("gilbert what\'s a ",1)[1])
		psum = page.summary
		if psum.find(" ") == -1:
			#if it doesnt have a page
			await m.channel.send("wikipedia does not have a page for that")
		else:#if it does have a page
			if (len(psum)>= 2000):
				await m.channel.send("the summary is " + str(len(psum)) + " characters long. discord only lets me send messages shorter than 2000 characters. go to https://en.wikipedia.org/wiki/" + (msg.split("gilbert wiki ",1)[1]))
			else:
				await m.channel.send(psum)
	if (msg.startswith("gilbert whats a ") and wiiii == True):
		wiiii = False
		page = wiki_wiki.page(msg.split("gilbert whats a ",1)[1])
		psum = page.summary
		if (psum.find(" ") == -1 or psum.find("a") == -1 or psum.find("e") == -1):
			#if it doesnt have a page
			await m.channel.send("wikipedia does not have a page for that")
		else:#if it does have a page
			if (len(psum)>= 2000):
				await m.channel.send("the summary is " + str(len(psum)) + " characters long. discord only lets me send messages shorter than 2000 characters. go to https://en.wikipedia.org/wiki/" + (msg.split("gilbert wiki ",1)[1]))
			else:
				await m.channel.send(psum)
	if (msg.startswith("gilbert what\'s ") and wiiii == True):
		wiiii = False
		page = wiki_wiki.page(msg.split("gilbert what\'s ",1)[1])
		psum = page.summary
		if (psum.find(" ") == -1 or psum.find("a") == -1 or psum.find("e") == -1):
			#if it doesnt have a page
			await m.channel.send("wikipedia does not have a page for that")
		else:#if it does have a page
			if (len(psum)>= 2000):
				await m.channel.send("the summary is " + str(len(psum)) + " characters long. discord only lets me send messages shorter than 2000 characters. go to https://en.wikipedia.org/wiki/" + (msg.split("gilbert wiki ",1)[1]))
			else:
				await m.channel.send(psum)
	if (msg.startswith("gilbert whats ") and wiiii == True):
		wiiii = False
		page = wiki_wiki.page(msg.split("gilbert whats ",1)[1])
		psum = page.summary
		if (psum.find(" ") == -1 or psum.find("a") == -1 or psum.find("e") == -1):
			#if it doesnt have a page
			await m.channel.send("wikipedia does not have a page for that")
		else:#if it does have a page
			if (len(psum)>= 2000):
				await m.channel.send("the summary is " + str(len(psum)) + " characters long. discord only lets me send messages shorter than 2000 characters. go to https://en.wikipedia.org/wiki/" + (msg.split("gilbert wiki ",1)[1]))
			else:
				await m.channel.send(psum)
	if (msg.startswith("gilbert wiki ") and wiiii == True):
		wiiii = False
		page = wiki_wiki.page(msg.split("gilbert wiki ",1)[1])
		psum = page.summary
		if (psum.find(" ") == -1 or psum.find("a") == -1 or psum.find("e") == -1):
			#if it doesnt have a page
			await m.channel.send("wikipedia does not have a page for that")
		else:#if it does have a page
			if (len(psum)>= 2000):
				await m.channel.send("the summary is " + str(len(psum)) + " characters long. discord only lets me send messages shorter than 2000 characters. go to https://en.wikipedia.org/wiki/" + (msg.split("gilbert wiki ",1)[1]))
			else:
				await m.channel.send(psum)
#good morning
	if (msg.startswith("gilbert morning") or msg.startswith("gilbert good morning") or msg.startswith("gilbert mornin")):
		wiiii = False
		await m.channel.send("mornin gamer")
#status

#gilbert
	if (msg.startswith("gilbert gilbert")):
		wiiii = False
		await m.channel.send("thats my name dont wear it out")
#hello
	if(msg.startswith("gilbert hi") or msg.startswith("gilbert hey") or msg.startswith("gilbert hello") or msg.startswith("gilbert howdy") or msg.startswith("gilbert yo")):
		wiiii = False
		await m.channel.send(random.choice(hello_words))
#fuck u
	if ((msg.startswith("gilbert fuck u") or msg.startswith("gilbert f u") or msg.startswith("gilbert fuck you") or msg.startswith("gilbert fu")) and wiiii == True):
		wiiii = False
		await m.channel.send("youre a goddamn walnut")
#go to hell
	if (msg.startswith("gilbert go to hell")):
		wiiii = False
		await m.channel.send("no u")
#coin flip
	if (msg.startswith("gilbert coin") or msg.startswith("gilbert flip") or msg.startswith("gilbert coin flip") or msg.startswith("gilbert flip a coin")):
		wiiii = False
		coin =["tails never fails","tails failed"]
		await m.channel.send(random.choice(coin))
#other 
	if (msg.startswith("gilbert") and wiiii == True):
	    await m.channel.send("no")
#_______________________________________________________________________


@client.event
async def on_raw_reaction_add(payload):
	msg_id = payload.message_id
	if msg_id == 814758271776849960:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)


		if payload.emoji.name == 'car':
			#print('car')
			role = discord.utils.get(guild.roles, name = 'racing')
		elif payload.emoji.name == 'hourse':
			#print('hourse')
			role = discord.utils.get(guild.roles, name = 'horse')
		elif payload.emoji.name == 'sharky':
			#print('shakry')
			role = discord.utils.get(guild.roles, name = 'sharks and minows')
		else:
			role = discord.utils.get(guild.roles, name = payload.emoji.name)
		#role = discord.utils.get(guild.roles, name = '')
		if role is not None:
			print(role.name)
			member = payload.member
			if member is not None:
				await member.add_roles(role)
				print("done")
			else:
				print("member not found")
		else:
			print("role not found")

@client.event
async def on_raw_reaction_remove(payload):
	msg_id = payload.message_id
	if msg_id == 814758271776849960:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

		
		if payload.emoji.name == 'car':
			#print('car')
			role = discord.utils.get(guild.roles, name = 'racing')
		elif payload.emoji.name == 'hourse':
			#print('hourse')
			role = discord.utils.get(guild.roles, name = 'horse')
		elif payload.emoji.name == 'sharky':
			#print('shakry')
			role = discord.utils.get(guild.roles, name = 'sharks and minows')
		else:
			role = discord.utils.get(guild.roles, name = payload.emoji.name)
		if role is not None:
			print(role.name)
			member = guild.get_member(payload.user_id)
			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("member not found")
		else:
			print("role not found")



client.run("TOKEN")
