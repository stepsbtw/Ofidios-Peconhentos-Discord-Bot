import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE2OTcwNzMxOTk3ODg5MzM1Mg.Gm2EGm.fx0iQpb4BtznCZcmrpmpcxKWV9Aq5CTwmpd7Yc'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' at ({channel})")

        while message.attachments:
            print("There is an attachment")
            img = await message.attachments.to_file(filename=attachment)
            print(img)
        else:
            print("There is no attachment")

        '''
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        '''


    client.run(TOKEN)