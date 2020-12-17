import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Loggeado en', self.user)

    async def on_message(self, message):
        
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('')
