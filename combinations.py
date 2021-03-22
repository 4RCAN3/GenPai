from itertools import product
import discord 
from discord.ext import commands, tasks

token = 'NzkzOTMwNjYyNzA0NTc4NjAx.X-zbjA.xBMgkw5qQN6cT2tLPzILy5DpSdE'

something = commands.Bot(command_prefix='$', case_insensitive=True)
something.remove_command('help')

def getPlaces(leet, password):
    num = []
    for i in password:
        num.append(leet[ord(i.upper()) - 65])
        
    return num

def getAllCombinations(password):
    leet = ["A4a","Bb8","Cc", "Dd","Ee3","Ff","Gg6","Hh","Ii","Jj","Kk",
    "Ll","Mm","Nn","Oo0","Pp","Qq","Rr","Ss5","Tt","Uu","Vv",
    "Ww","Xx","Yy","Zz2"]
    
    '''
    for i in range(0, len(password.split(" "))):
        getPlaces = lambda password: [leet[ord(el.upper()) - 65] for el in password.split(" ")[i]]
        words.extend(getPlaces)'''
    
    all_combs = []
    for word in password.split(" "):
        for letters in product(*getPlaces(leet, word)):
            all_combs.append("".join(letters))
    
    return all_combs

final_combs = ""
@something.event
async def on_message(message):
        await something.process_commands(message)
        global final_combs
        if message.channel.id == 811231209254289449:
            all_combs = getAllCombinations(message.content)
            f = open("combs.txt", "w")
            words = []
            words.extend(all_combs)
            combs = []
            combs.extend(words)
            print(len(words))
            for word in words:
                new_1 = "pw: " + word
                combs.append(new_1)
                new_2 = "pw:" + word
                combs.append(new_2)
            
            print(combs)
            
            for comb in combs:
                final_combs += comb + '\n'

            print(final_combs)
            f.write(final_combs)

            await message.channel.send(combs)

@something.command()
async def file(ctx):
    with open("combs.txt", "rb") as file:
        await ctx.send(file=discord.File(file))

something.run(token)
