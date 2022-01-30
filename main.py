import discord
import os
import requests
import json
from keep_running import keep_running


my_secret = os.environ['token']

client = discord.Client()


def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
    print('We have logged in  as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#Hello'):
        await message.channel.send('Hello! how can I help You My Man🙂')

    if message.content.startswith('#News'):
        await message.channel.send('Hello! You can check news of Technology here👉 https://www.cnet.com/ ')

    if message.content.startswith('#Quotes'):
        quote = get_quotes()
        await message.channel.send(quote)

    if message.content.startswith('#HackingNews'):
        await message.channel.send('Hello! You can check news of Hacking here👉 https://thehackernews.com/')




keep_running()

client.run(os.environ.get('token'))
