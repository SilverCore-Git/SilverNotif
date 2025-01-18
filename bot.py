
# By = SilverCore - SilverNotif
# Version = 2.0
# Help SilverCore : https://fr.tipeee.com/silverdium
# Web site = https://core.silverdium.fr


# Import libs
import discord
import json
import requests
from discord.ext import commands, tasks

# import config
with open("config.json", "r") as file:
    cfg = json.load(file)

# get config
DISCORD_TOKEN = cfg["General"]["Token"]
YOUTUBE_API_KEY = cfg["General"]["ApiKey"]
YOUTUBE_CHANNEL_ID = cfg["ChanelId"]

PREFIX = cfg["Message"]["Prefix"]
PREFIX_ERR = cfg["Message"]["Prefix_ERR"]

MSG_CONECT = cfg["Message"]["BotConect"]
MSG_ERRORAPI = cfg["Message"]["APIConectERR"]
MSG_NEWVIDEO = cfg["Message"]["NewVideo"]

DISCORD_ACTIVITY = cfg["General"]["activity"]
DISCORD_CHANNEL_ID = cfg["Salon"]["SalonId_ytb"]

# Divers var
last_video_id = None
url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={YOUTUBE_CHANNEL_ID}&order=date&type=video&maxResults=1&key={YOUTUBE_API_KEY}"

# général bot config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot is on ready do :
@bot.event
async def on_ready():
    print(f"{PREFIX} {MSG_CONECT} : {bot.user}")
    activity = discord.CustomActivity(name=DISCORD_ACTIVITY)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    check_new_video.start()

# Every 5 minutes bot do :
@tasks.loop(minutes=5)
async def check_new_video():

    global last_video_id
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data["items"]:
            channelytb = data["items"][0]["snippet"]["channelTitle"]
            video = data["items"][0]
            video_id = video["id"]["videoId"]
            video_title = video["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            if video_id != last_video_id:
                last_video_id = video_id 
                channel = bot.get_channel(DISCORD_CHANNEL_ID)
                if channel:
                    await channel.send(f"# {MSG_NEWVIDEO} {channelytb} : \n# **[{video_title}]({video_url})**\n{video_url}")
                print(f"{PREFIX} {MSG_NEWVIDEO} {channelytb} :")
                print(f"{PREFIX} {video_url}")
                print(f"{PREFIX} {video_title}")

    else:
        print(f"{PREFIX_ERR} {MSG_ERRORAPI} : {response.status_code}")


# start the bot
bot.run(DISCORD_TOKEN)
