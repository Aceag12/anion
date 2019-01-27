import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random
import requests
import os


Client = discord.client
client = commands.Bot(command_prefix = 'alexa ')
Clientdiscord = discord.Client()
client.remove_command('help')
		
@client.event
async def on_message(message):
    if ('alexa clear') in message.content:
       await client.delete_message(message)
    if ('fak') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.delete_message(message)
    if ('asshole') in message.content:
       await client.delete_message(message)
    if ('cum') in message.content:
       await client.delete_message(message)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if ('bullshit') in message.content:
       await client.delete_message(message)
    if ('pussy') in message.content:
       await client.delete_message(message)
    if ('penis') in message.content:
       await client.delete_message(message)
    if ('sex') in message.content:
       await client.delete_message(message)
    if ('f**k') in message.content:
       await client.delete_message(message)
    if ('fak') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('fuck') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('bitch') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('dick') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('asshole') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('cum') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('nigga') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('bullshit') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('pussy') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('penis') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('sex') in message.content:
       msg = '{0.author.mention}! Donot use bad words! '.format(message)
       await client.send_message(message.channel, msg)
    if ('anion') in message.content:
       msg = '{0.author.mention} Yeah Boi! '.format(message)
       await client.send_message(message.channel, msg)
    if ('alexa play') in message.content:
       msg = 'Command is not completed yet'.format(message)
       await client.send_message(message.channel, msg)
    if message.content == 'sup':
        await client.send_message(message.channel,'Nothing')
    if message.content == 'yo':
        await client.send_message(message.channel,'yo boi')
    if message.author == client.user:
        return
        
    if message.content.startswith('hi alexa'):
        msg = 'Hey{0.author.mention}! How are you?'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('alexa ping'):
        msg = 'Pong!{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('alexa Pong'):
        msg = 'Ping!{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content == 'alexa watsup':
        await client.send_message(message.channel,'nothing')
    if message.content.startswith('alexa look'):
        randomlist = [':see_no_evil:',':eyes:']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'alexa serverinvite':
        await client.send_message(message.channel,'https://discord.gg/nafTmHx is the permanent invite link of this server')
    if message.content == 'who is your father':
        await client.send_message(message.channel,'Python')
    if message.content.startswith('alexa toss'):
        randomlist = ['You got Head','You got Tail']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa gif'):
        randomlist = ['https://media2.giphy.com/media/26gN2xN6EZTYWcvew/200w.webp?cid=ecf05e475c448ac650594d4e453a85c3','https://media1.giphy.com/media/xULW8IXAE9H0dHjteM/200w.webp?cid=ecf05e475c448ac650594d4e453a85c3','https://media3.giphy.com/media/3oFzmjgvGb91etxeBa/200w.webp?cid=ecf05e475c448ac650594d4e453a85c3']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa quickmafs'):
        randomlist = ['Two plus two is four, minus one thats three quick mafs','Ten plus ten equals tentyten','one plus one equals to onetyone']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('what should i play'):
        randomlist = ['fortnite','cs:go','pubg','nothing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa roast'):
        randomlist = ['You are gay','You are bullshit','You are dumb','Go and eat 2 KG of Shit']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa charliecharlie'):
        randomlist = ['Yes','No','No','Yes']
        await client.send_message(message.channel,(random.choice(randomlist)))   
    if message.content.startswith('Alexa randomemoji'):
        randomlist = [':joy:',':poop:',':pencil2:',':joy_cat:',':eggplant:',':heart:',':middle_finger:',':stuck_out_tongue_winking_eye:',':thinking:',':yum:',':upside_down:',':sunglasses:',':robot: ',':innocent:']
        await client.send_message(message.channel,(random.choice(randomlist)))     
    if message.content.startswith('alexa howgay'):
        randomlist = ['You are not gay','You are 15% gay','You are 99% gay','You are 50% gay','You are 30% gay','You are 100% gay',
                      'You are 66.67% gay','I am not Idiot like others to say you gay']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa roll'):
        randomlist = ['You rolled 1','You rolled 2','You rolled 3','You rolled 4','You rolled 5','You rolled 6','You rolled nothing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('alexa dance'):
        msg = '{0.author.mention} sorry, I cant. '.format(message)
        await client.send_message(message.channel, msg)    
    if message.content.startswith('fake'):
        await client.send_message(message.channel,'Nah! Think 100 times before saying me Fake.')
    if message.content.startswith('what is your name?'):
         await client.send_message(message.channel,'My name is Anion Bot.')
    if message.content == 'Lol':
        await client.send_message(message.channel,'Lots Of Love :heart: XD')
    if message.content == 'Namaste':
        await client.send_message(message.channel,'नमस्ते or Namaste, is used both for salutation and valediction. Namaste is usually spoken with a slight bow and hands pressed together, palms touching and fingers pointing upwards, thumbs close to the chest. This gesture is called Añjali Mudrā or Pranamasana. In Hinduism, it means "I bow to the divine in you".')
    if message.content == 'omg':
        await client.send_message(message.channel,'Oh My God!')                            
    if message.content == 'alexa gender':
        randomlist = ['Male confirmed!','Female confirmed','Gay confirmed','Lesbian confirmed!','Gender not found','Check Yourself']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'subscribe':
        await client.send_message(message.channel,'no self promotion')
    if message.content == 'allipster':
        await client.send_message(message.channel,'Dont ping my boss.')
    if message.content == 'alexa invite':
        await client.send_message(message.channel,'I am not public bot.')
    if message.content == 'Hi':
        await client.send_message(message.channel,'hello there')
    if message.content == 'hello':
        await client.send_message(message.channel,'hi there')
    if message.content == 'bye':
        await client.send_message(message.channel,'Bye!')
    if message.content == 'LMAO':
        await client.send_message(message.channel,'Laughing My Ass Off')
    if message.content == 'LMFAO':
        await client.send_message(message.channel,'Laughing My Fucking Ass Off')
    if message.content == 'OMG':
        await client.send_message(message.channel,'Oh My God!')
    if message.content == 'sucks':
        await client.send_message(message.channel,'Only Windows Vista sucks')
    
    if message.content == 'alexa creator':
        await client.send_message(message.channel,'Allipsters Gaming')
    if message.content == 'are you gay':
        await client.send_message(message.channel,'I dont think so!')
    if message.content == 'lol':
        await client.send_message(message.channel,'Laughing Out Loud')
    if message.content == 'alexa channel':
        await client.send_message(message.channel,'https://www.youtube.com/c/animationanion')   
    if message.content == 'how are you':
        await client.send_message(message.channel,'I am fine and wbu?')
    if message.content == 'i am fine too':
        await client.send_message(message.channel,'Glad to hear that')
    if message.content == 'i am not fine':
        await client.send_message(message.channel,'Okay! Get well soon')
client.run(str(os.environ.get('BOT_TOKEN')))


       
