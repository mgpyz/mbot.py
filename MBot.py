import discord

from discord.ext import commands
client = commands.Bot(command_prefix="m!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def pog(ctx):
    await ctx.send("pog")

@client.command()
async def repeat(ctx, arg):
        await ctx.send(arg)

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


client.run('NzYxMzc5MTgyNDE5NzcxMzkz.X3Zvng.7RYeKXJjifpyyP3ABxhPBp1WvqA')