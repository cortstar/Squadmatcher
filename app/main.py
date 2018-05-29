import discord
import asyncio
import Squad

opt_in_time = 10
squad_size_max = 4
emoji = u"\u270B"
client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {}-{} \n".format(client.user.name, client.user.id))


@client.event
async def on_message(message):
    if client.user not in message.mentions:
        return

    msg = await client.send_message(message.channel, matching_message(10), tts=True)


    try:
        await client.add_reaction(msg, emoji)
    except discord.NotFound:
        await warn(message.channel,"emoji not found, misconfigured?")
        return

    await asyncio.sleep(1)

    for i in range(0, opt_in_time):
        await client.edit_message(msg, new_content=matching_message(opt_in_time-i))
        await asyncio.sleep(1)

    cache_msg = discord.utils.get(client.messages, id=msg.id)

    players = []
    try:
        reaction = [reaction for reaction in cache_msg.reactions if reaction.emoji == emoji][0]
        players = await client.get_reaction_users(reaction)
    except KeyError:
        await warn("The reactions were somehow deleted, cancelling match...")
        return

    players = [player.name for player in players]

    if client.user.name in players:
        players.remove(client.user.name)

    await client.edit_message(msg, new_content=Squad.SquadList(players, squad_size_max).toString())


async def warn(channel, warning_message):
    await client.send_message(channel, warning_message)

def matching_message(time):
    return "Squad up! React to opt in in {} seconds!".format(time)

try:
    with open("token.txt", "r") as token_file:
        client.run(token_file.readline().strip().strip("\n"))
        token_file.close()
except IOError:
    print("no token file - ensure that a token.txt exists in the directory.")




