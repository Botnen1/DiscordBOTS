import discord
import responses1
 
async def send_message(message, user_message, is_private):
        try:
            respons = responses1.get_response(user_message)
            await message.author.send(respons) if is_private else await message.channel.send(respons)
            
        except Exception as e:
            print(e) 
        
def run_discord_bot():
    
    token = 'insert token here'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.event
    async def on_delete():
        pass
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        liste = message.id
        
        
        
        with open("log.txt", "a") as f:
            f.write("user : ")
            f.write(username)
            f.write("\n")
            f.write("said : ")
            f.write(user_message)
            f.write("\n")
            f.write("in channel : ")
            f.write(channel)
            f.write("\n")
            f.write("message ID : ")
            f.write(str(liste))
            f.write("\n")
            f.write("\n")
            
            
            
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token)
