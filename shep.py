from SHEP_AI import *
import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.bots={}
        
    async def on_message(self, message):
        #Assign a bot to each person
        if message.author == self.user:
            return
        if str(message.channel)=="shep-v009":
            self.bots[message.author]=self.bots.get(message.author,[CB("C:/Users/Dexter Shepherd/Documents/AI/V0.0.9/BOX/testCB/")])
            cleverBot=self.bots[message.author][0] #get current bot
            await message.channel.send("@"+message.author.name+" "+cleverBot.chat(message.content))
            
client = MyClient()
client.run('T')
    
