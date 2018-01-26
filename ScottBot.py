import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Praise_Scott'):
        await client.send_message(message.channel, 'Lord Scott Be Praised! https://cdn.discordapp.com/attachments/398220275893796884/404366781847961600/image.jpg')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!Pott_Manley'):
        await client.send_message(message.channel, 'https://fat.gfycat.com/JovialTalkativeCaterpillar.gif')
    elif message.content.startswith('!Commands'):
         await client.send_message(message.channel, '!Praise_Scott \n !Pott_Manley ')
    elif message.content.startswith('!Greet'):
         await client.send_message(message.channel, 'hi why did you come, this place is chaotic and very un-scott. You should run. Fast. And check the pinned messages, specifically the 4th and 5th ones down')
client.run('codehere')
