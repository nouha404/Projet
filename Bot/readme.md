# Pour reagir a l'arriver d'un nouveau membre on utilise les Intents qu'on a cocher au debut "present intent" et "server member intent"
# quand un utilisateur arrive et quitte on utilise : la fonction on_member_join(member) , one_remove(member)
# une fois la variable creer un creer une instance default() pour heriter des permissions :
    #  default_intent = discord.Intents.default()
    # activer les intentes au membre : default_intent.member = True
    # et on le passe a notre client : client = discord.Client(intents=default_intent.member)
#pour recuperer un channel : "il faut dabord activer le mode developpeur =>parametre=>apparance"
#   general_channel : discord.TextChannel = client.getChannel(on copie le int de du salon)
#   await general_channel.send(content=f'Bienvenue {member.display.name}')
--------------------------------------------------------------
Methode client 
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Rogerrr')
    
@client.event
async def on_message(message):
    
    if message.content.lower() == 'one piece':
        await message.channel.send('Zehahahahahaha')
    elif message.content.lower() == "one piece c'est le best":
         await message.channel.send(f'Reel {message.author} ')
        
    print(message.content)

client.run('TOKEN')

