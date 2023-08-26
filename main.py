import disnake
from disnake.ext import commands
from disnake.utils import get

import datetime
import random

from config import TOKEN, PREFIX, BANNED_WORDS, HASH_CODE_MASTER

# Flags
flag_to_delete = False
flag_to_logs = False

# Instances
bot = commands.Bot(command_prefix=PREFIX, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} jest gotowy do pracy")


@bot.command(name="timeDelete")
async def time_delete(context: commands.Context):
    global flag_to_delete
    flag_to_delete = not flag_to_delete if (context.message.author.id == 694834354769362986) else flag_to_delete


@bot.command()
async def hello(context: commands.Context):
    print(context.message.content)
    await context.send('Hello World! I wanna eat Niggers!')


@bot.event
async def on_message(message: disnake.Message):
    global flag_to_delete
    global flag_to_logs
    user = message.author
    text = message.content.lower()
    # # 694834354769362986

    await bot.process_commands(message)
    if message.content.startswith(PREFIX):
        return

    if flag_to_logs:
        with open("BotLogs.txt", "a", encoding="windows 1251") as log_file:
            string = f"{user}: {message.content}" \
                     f"\nServer: {message.guild.name}" \
                     f"\nChannel: {message.channel}" \
                     f"\nTime: {datetime.datetime.now().replace(microsecond=0)}\n" \
                     f"|------------------------------------|\n"
            log_file.write(string)

    if text in BANNED_WORDS:
        await message.channel.send(f"{user.mention} You do not ought to write these words."
                                   " Else one big human will fuck your tiny ass",
                                   delete_after=7.0)
        await message.delete(delay=7.0)

    if (str(user) == "Cute bot#1081") and ("ты заебал со" in text):
        await message.channel.send("Иди нахуй", delete_after=4.0)

    # if random.randint(1, 7) == 3:
    #     await message.add_reaction(":)")

    # Super function for ShinkiMinkiNon
    if flag_to_delete:
        await message.delete(delay=4.0)


# New function to logging (Maybe changed (Need to recheck))
# Check 100%
@bot.command()
async def logging(context: commands.Context):
    global flag_to_logs
    flag_to_logs = not flag_to_logs if (context.message.author.id == HASH_CODE_MASTER) else flag_to_logs


# Write it later
@bot.slash_command(description="Приказывает человеку закончить теребоньканье")
async def fup(context: disnake.ApplicationCommandInteraction, member: disnake.Member):
    mentioned_member = get(context.guild.members, id=member.id)
    await context.send(f"Хватит теребонькать {mentioned_member.mention}! Иди сюда!")


@bot.command(name="matataCall")
async def matata_call(context: commands.Context):
    matata = get(context.guild.members, id=HASH_CODE_MASTER)
    await context.send(f"Я призываю Великого и Неповторимого МАТАТУ.\nО МАТАТА, ХРАНИТЕЛЬ ПОЛЫХАЮЩЕЙ КОЧЕРГИ, ПРИДИ!"
                       f"\n{matata.mention}")


@bot.slash_command(name="call", description="Оформляет призыв охотника некоторое количество раз")
async def call_hunter(context: disnake.ApplicationCommandInteraction, member: disnake.Member, text: str):
    for i in range(random.randint(1, 10)):
        await context.send(f"{member.mention}, епт. {text}")


bot.run(TOKEN)
