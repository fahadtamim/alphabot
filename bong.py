from random import random

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=";")


# f = open("rules.txt","r")
# rules = f.readlines()

@client.event
async def on_ready():
    print("bot is ready")


# @client.command(aliases=['rules'])
# async def rule(ctx,*,number):
#	await ctx.send(rules[int(number)-1])

@client.command()
async def hello(ctx):
    await ctx.send("মনি আমার দলে আয়ছো")

@client.command()
async def good_morning(ctx):
	await ctx.send("দাত মেজে আয়")

@client.command()
async def good_night(ctx):
	await ctx.send("মুতে এসে,ঘুমা")


@client.command()
async def ping(ctx):
    await ctx.send(f"নে দেখ {round(client.latency * 1000)}ms")


@client.command()
async def janu(ctx, *,question):
    r = ['হোগা মারা খা',
                 'আয়নায় নিজের মুখ দেখ',
                 'তোর নানির পুটকি সই',
                 'বাল বাল করিস না',
                 'বাবু খাইসো?',
                 'ভারী লজ্জার কথা',
                 'হোগা মারা সারা',
                 'বিড়ি খা',
                 'মদ খা মানুস হ',
                 'আমার আকাশ ভোরা তারা',
                 'ছ্যাকা খাইসো',
                 'দাদা খাইছেন নাকি যেয়ে খাবেন?',
                 'মুতি আয় হুতি যা',
                 'একটু হাই হয়ে গেছিলাম বাড়া',
                 'শালা মারবো এখানে লাশ পড়বে শ্মশানে',
                 'সবই পিনিক',
                 'বোকাচোদা',
                 'মর শালা']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(r)}')


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, members: discord.Member, *, reason="No reason provided"):
    await member.send("তোমাকে লাথি মারা হয়েছে, কারণ:" + reason)
    await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, members: discord.Member, *, reason="No reason provided"):
    await member.send(member.name + "has been banned from ALPHA, Because:" + reason)
    await member.ban(reason=reason)


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, members):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_enter in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + "has been unbanned!")
            return

    await ctx.send(member + "was not found")


client.run("Nzc1NzE5OTYzMzY5NDA2NDg1.X6qbgw.XZ_8l-gv8lUOmqI5jFlR9hJQ6A4")
