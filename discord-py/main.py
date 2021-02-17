# pip install -U discord.py
import discord
import requests
import json


class myClient(discord.Client):
  # Coroutine to login
    async def on_ready(self):
        print(f'Howdy 👋 ! Logged in as {client.user}'.format(client))

  # Coroutine to answer messages
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.startswith('hello'):
            await ctx.channel.send('Howdy, friend 👋')
        elif ctx.content.startswith('make me laugh'):
            await ctx.channel.send('Would you like to hear a Chuck Norris joke 😛 ?')
            res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
            if res.content.lower() == ('yes'):
                # code to fetch the jokes from Chuck Norris API
                # print('fetching a joke from C Norris API')
                # await ctx.channel.send('Cool 👍! on it ...')
                async def get_joke(self):
                    response = requests.get(
                        'https://api.chucknorris.io/jokes/random')
                    joke = json.loads(response.text)
                    # print(joke)
                    return(joke['value'])
                the_joke = await get_joke(self)
                await ctx.channel.send(the_joke)
            else:
                await ctx.channel.send('no problem!')
        elif ctx.content.startswith('salut'):
            await ctx.channel.send('salut, mon ami 👋')
        elif ctx.content.startswith('привет'):
            await ctx.channel.send('привет мои друг 👋')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
client.run('your token goes here')
