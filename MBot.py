import discord

import asyncio

from discord.ext import commands
client = commands.Bot(command_prefix="m!")

#basic commands

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def pog(ctx):
    await ctx.send("pog")

@client.command()
async def repeat(ctx, arg):
        await ctx.send(str(arg))

@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    boostLevel = str(ctx.guild.premium_tier)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    boosts = str(ctx.guild.premium_subscription_count)
    rulesChannel = ("#" + str(ctx.guild.rules_channel))
    creationTime = (str(ctx.guild.created_at) + " UTC")


    embed = discord.Embed(
        title=name + " Server Information",
        description="Displays Information For " + name,
        color=discord.Color.purple()

    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server ID", value=str(ctx.guild.id), inline=True)
    embed.add_field(name="Rules Channel", value=rulesChannel, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Boost Level", value=boostLevel, inline=True)
    embed.add_field(name="Boosts", value=boosts, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Created At", value=creationTime, inline=True)


    await ctx.send(embed=embed)


@client.command()
async def cmds(ctx):
    mbotCommands = ("""
m!hello (says hello back)

m!repeat [word] (repeats whatever word comes after repeat; note: only one word is supported at this time)

m!pog (makes the bot respond with pog)

m!serverinfo (displays server information)

m!cmds (displays all mbot commands)

m!info (lists info about the bot)

m!hognose (sends a pic of a cute hognose snake)

m!moth (sends a pic of a cute moth)

m!gothmoth (sends a pic of liz)

m!ballpython (displays a whole sheet of information on ball pythons)

m!cornsnake (displays a whole sheet of information on corn snakes)

    """)
    sneak = ("https://cdn.discordapp.com/attachments/752046155306893344/761405809598267423/sneak.png")

    embed = discord.Embed(
        title="MBot Commands",
        description="Lists All Mbot Commands",
        color=discord.Color.purple()

    )
    embed.set_thumbnail(url=sneak)
    embed.add_field(name="Commands", value=mbotCommands, inline=False)

    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    mbotVersion = ("0.1")
    creator = ("marshall#0027")
    running = ("Python 3.8 and using Discord.py")

    sneak = ("https://cdn.discordapp.com/attachments/752046155306893344/761405809598267423/sneak.png")

    embed = discord.Embed(
        title="MBot Info",
        description="Lists MBot Information",
        color=discord.Color.purple()

    )
    embed.set_thumbnail(url=sneak)
    embed.add_field(name="Version", value=mbotVersion, inline=False)
    embed.add_field(name="Made by", value=creator, inline=False)
    embed.add_field(name="Running", value=running, inline=False)


    await ctx.send(embed=embed)

#animal commands

@client.command()
async def snakes(ctx):
    sneak = ("https://cdn.discordapp.com/attachments/752046155306893344/761405809598267423/sneak.png")

    embed = discord.Embed(
        title="Snake Info List",
        description="Lists All Snakes You Can Search",
        color=discord.Color.purple()

    )
    embed.set_thumbnail(url=sneak)
    embed.add_field(name="Snakes", value="""

        m!ballpython

         m!cornsnake
            """, inline=False)

    await ctx.send(embed=embed)

@client.command()
async def ballpython(ctx):

        ballpicon = ("https://cdn.discordapp.com/attachments/754806471186841600/761448358539558922/9k.png")

        embed = discord.Embed(
            title="Snake Info",
            description="Ball Python (Python regius)",
            color=discord.Color.purple()

        )
        embed.set_thumbnail(url=ballpicon)
        embed.add_field(name="General Info", value="""
        "...The ball python, is a python species native to West and Central Africa, where it lives in grasslands and shrublands. It is listed as Least Concern on the IUCN Red List because of its wide distribution. It is threatened by hunting for its meat and for the international pet trade. - Wikipedia""",inline=False)
        embed.add_field(name="Avg. Lifespan (Captivity)", value="20 to 30 Years", inline=False)
        embed.add_field(name="Ratings", value="""
        Aggression:◆◇◇◇◇
        Difficulty:◆◆◇◇◇
        Price:◆◆◇◇◇""", inline=False)
        embed.add_field(name="In Depth Care Sheet", value="https://www.goherping.com/ballpythons", inline=False)

        await ctx.send(embed=embed)

@client.command()
async def cornsnake(ctx):

        cornsnikon = ("https://cdn.discordapp.com/attachments/754806471186841600/761449308054224906/corn-snake-from-the-lower-florida-keys-530475947-588124bc5f9b58bdb3ec9f93.png")

        embed = discord.Embed(
            title="Snake Info",
            description="Corn Snake (Pantherophis guttatus)",
            color=discord.Color.purple()

        )
        embed.set_thumbnail(url=cornsnikon)
        embed.add_field(name="General Info", value="""
        "The corn snake is a North American species of rat snake that subdues its small prey by constriction. It is found throughout the southeastern and central United States." - Wikipedia""",inline=False)
        embed.add_field(name="Avg. Lifespan (Captivity)", value="10 - 15 Years", inline=False)
        embed.add_field(name="Ratings", value="""
        Aggression:◆◇◇◇◇
        Difficulty:◆◇◇◇◇
        Price:◆◇◇◇◇""", inline=False)
        embed.add_field(name="In Depth Care Sheet", value="https://www.goherping.com/corn-snakes", inline=False)

        await ctx.send(embed=embed)

@client.command()
async def hognose(ctx):
    await ctx.send("https://static.boredpanda.com/blog/wp-content/uploads/2015/11/cute-snakes-wear-hats-106__700.jpg")

@client.command()
async def moth(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/736867197170876437/761434077068132362/image1.jpg")

@client.command()
async def gothmoth(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/736867197170876437/761434210786476052/image0.jpg")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="m!cmds"))

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send(str(member) + " was muted.")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await ctx.send(str(member) + " was unmuted.")
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")


client.run('NzYxMzc5MTgyNDE5NzcxMzkz.X3Zvng.ySbaGtwavhUQdhpesmkg_DSmNis')