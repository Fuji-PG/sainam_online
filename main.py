import os
import time
from keep_alive import keep_alive
try:
    import discord
except:
    from setup import install
    install()
    import discord

print("""\
██╗░░░██╗░█████╗░██╗░█████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░
██║░░░██║██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║
░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║
░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
**Version: 1.0.0**""")
time.sleep(0.5)
client = discord.Client(intents=discord.Intents.default())
Token = os.getenv("Token")
Id = os.getenv("IdVc")

@client.event
async def on_ready():
    voice_channel = client.get_channel(Id)
    
    # เปลี่ยนเป็นสถานะ Streaming (สีม่วง)
    stream_status = discord.Streaming(
        name="Treasure",  # ชื่อสตรีมที่แสดง
        url="https://www.twitch.tv/fujipp"  # ใส่ลิงก์ Twitch หรืออะไรก็ได้ที่ valid
    )
    await client.change_presence(activity=stream_status)
    
    await voice_channel.connect()

    print('Logged in as {0.user}'.format(client))
    print('Connected to voice channel: {}'.format(voice_channel))


keep_alive()
client.run(Token, bot=False)