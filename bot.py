import discord
import json
import requests
from discord.ext import commands, tasks


with open("config.json", "r") as file:
    cfg = json.load(file)

DISCORD_TOKEN = cfg["Token"]
YOUTUBE_API_KEY = cfg["ApiKey"]
# https://ytubetool.com/fr/tools/youtube-channel-id
YOUTUBE_CHANNEL_ID = cfg["ChanelId"]
DISCORD_CHANNEL_ID = cfg["SalonId_ytb"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

last_video_id = None

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    check_new_video.start()

@tasks.loop(minutes=5)
async def check_new_video():
    global last_video_id
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={YOUTUBE_CHANNEL_ID}&order=date&type=video&maxResults=1&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            video = data["items"][0]
            video_id = video["id"]["videoId"]
            video_title = video["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"


            if video_id != last_video_id:
                last_video_id = video_id 
                channel = bot.get_channel(DISCORD_CHANNEL_ID)
                if channel:
                    await channel.send(f"# Nouvelle vidéo publiée sur la chaine de Silverdium : \n# **[{video_title}]({video_url})**\n{video_url}")
    else:
        print(f"Erreur lors de l'accès à l'API YouTube : {response.status_code}")

bot.run(DISCORD_TOKEN)
