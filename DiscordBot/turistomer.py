import discord
import time
import random
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
import urllib
import requests
from datetime import datetime

from urllib.request import urlopen
TOKEN = "ODc3Nzk3MzYxMjY1NTY5Nzk0.YR32fw.yqKIuGBxLo_qxKmG3aS9Qx6cpL8"

client = discord.Client()
bot = Bot(command_prefix="!")
now = datetime.now()
current_time = now.strftime("%D:%m:%H:%M:%S")


@bot.event
async def on_ready():
    print("Bot Hazır " + str(bot.user))

@bot.event
async def on_message(message):
    print("[{}][{}]{}: {}\n".format(message.guild.name,current_time,message.author.name,message.content))
    log = open("log.txt","a")
    log.write("[{}][{}]{}: {}\n".format(message.guild.name,current_time,message.author.name,message.content))
    if message.author == client.user:
        return

    if message.content == "sa":
        await message.channel.send("as {}" .format(message.author.name))

    if message.content == "Merhaba" or message.content =="merhaba":
        await message.channel.send("Merhabana merhaba {}" .format(message.author.name))

    if message.content == "!tahmin r6":
        await message.channel.send("Mavi vs Turuncu")
        await message.channel.send("Düşünüyorum...")
        time.sleep(2)
        x = random.randint(1,2)
        takim = 0
        if x == 1:
            takim = "Mavi"
        if x == 2:
            takim = "Turuncu"
        await message.channel.send("Bu maçı {} takım kazanır bileğinize kuvvet Yüce Kudretli ALLAHIN aslanları".format(takim))

    quest= message.content
    quest = quest.split()

    if quest[0] == "!skor":
        url = "https://www.google.com.tr/search?q="+quest[1]
        headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        sayfa = requests.get(url,headers=headersparam)
        soup = BeautifulSoup(sayfa.content,"lxml", from_encoding='UTF-8')
        div = soup.find_all("div", attrs={"class": "imso_mh__l-tm-sc imso_mh__scr-it imso-light-font"})
        div2 = soup.find_all("div", attrs={"class": "imso_mh__r-tm-sc imso_mh__scr-it imso-light-font"})
        bastir = str(div)
        bastir2 = str(div2)
        xtakimadi1 = soup.find_all("div",attrs={"class":"imso_mh__first-tn-ed imso_mh__tnal-cont imso-tnol"})
        xtakimadi2 = soup.find_all("div", attrs={"class": "imso_mh__second-tn-ed imso_mh__tnal-cont imso-tnol"})
        takimadi1 = str(xtakimadi1)
        takimadi2 = str(xtakimadi2)
        await message.channel.send("{} : {} - {} : {}" .format(takimadi1[748:-26],bastir[63:-7],takimadi2[749:-26],bastir2[63:-7]))

    if quest[0] == "!stats":
        url = "https://r6.tracker.network/profile/pc/"+quest[1]
        headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        sayfa = requests.get(url,headers=headersparam)
        soup = BeautifulSoup(sayfa.content,"lxml", from_encoding='UTF-8')
        kd = soup.find_all("div", attrs={"data-stat":"RankedKDRatio"})
        kd = str(kd)
        kd = kd[59:-8]
        wins = soup.find_all("div",attrs={"data-stat":"RankedWLRatio"})
        wins = str(wins)
        wins = wins[59:-8]
        hs = soup.find_all("div",attrs={"data-stat":"PVPAccuracy"})
        hs = str(hs)
        hs = hs[57:-7]
        print( "İsim: {} \n" "KD:{}\n Kazanılan Maç Oranı:{}\n Kafadan Vuruş Oranı:{} ".format(quest[1],kd,wins,hs))
        await message.channel.send( "İsim: {} \n" "KD:{}\n Kazanılan Maç Oranı:{}\n Kafadan Vuruş Oranı:{} ".format(quest[1],kd,wins,hs))
bot.run(TOKEN)
