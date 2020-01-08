import discord
from discord.ext import commands
import random


#Join our Discord server : https://discord.gg/fPMRvjz

bot = commands.Bot(command_prefix='!')#Defines the prefix "!"
client = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------')

bot.remove_command('help')
@bot.command() #help command
async def help(ctx):
    embed = discord.Embed(title='XS-GEN', description=''+ctx.message.author.mention, color=0x008000)
    embed.add_field(name='ABOUT', value=' XS-GEN is an account generator with additional features like auto-delete after generate & public stock reveal.\n!gen spotify to Genrerate!')
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)#Cooldown of 30 seconds
async def gen(ctx,errors):

    if ctx.message.author == client.user:
        return
    elif ctx.message.channel.name == 'dm':
        return
    else:
        discordinput = (ctx.message.content[5:])


        if discordinput != 'spotify':
            embed = discord.Embed(title='Syntax Incorrect', description=''+ctx.message.author.mention, color=0xFFFF00)
            embed.add_field(name='', value='Type "!help" to know more')
            await ctx.send(embed=embed)


        elif discordinput == 'spotify':#generates random line from accounts.txt and deletes the line
            with open('accounts.txt',"r") as f:
                lines = [line.rstrip('\n') for line in f]
            rnd_line = random.choice(lines)
            with open("accounts.txt", "w") as f:
                for line in lines:
                    if line.rstrip('\n') != rnd_line:
                        f.write(line+'\n')

            out = rnd_line
            embed = discord.Embed(title='Generated', description=''+ctx.message.author.mention, color=0xeee657)
            embed.add_field(name='Credentials: ', value=''+out)
            inbuiltem = embed = discord.Embed(title='DM Sent', description=''+ctx.message.author.mention, color=0xeee657)
            await ctx.send(embed=inbuiltem)
            await ctx.message.author.create_dm()
            await ctx.message.author.dm_channel.send(embed=embed)

@bot.command()
async def donate(ctx):#saves the account on account_donated.txt file
    discordinput = (ctx.message.content[8:])
    hs = open("accounts_donated.txt","a")
    hs.write(discordinput + "\n")
    hs.close()
    embed = discord.Embed(title='Added To Donation List', description=''+ctx.message.author.mention, color=0xeee657)
    embed.add_field(name='Donated Accounts need to be verified before adding it to stock list.', value='Your help is appreciated!')
    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command()
async def stock(ctx):#reads the number of lines in accounts.txt
    counts = len(open('accounts.txt').readlines(  ))
    embed = discord.Embed(title='SPOTIFY STOCKS', description=''+ctx.message.author.mention, color=0x008000)
    embed.add_field(name='NO OF ACCOUNTS', value=counts)
    await ctx.send(embed=embed)

bot.run('XXXX')#paste your token here