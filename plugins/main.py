import pyrogram
from pyrogram import Client
from pyrogram import filters
import bypasser
import os
import ddl
import requests
import threading

# bot
bot_token = os.environ.get("BOT_TOKEN", "")
api_hash = os.environ.get("API_HASH", "") 
api_id = os.environ.get("API_ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  

# ENVs
GDTot_Crypt = os.environ.get("GD_CRYPT","")
Laravel_Session = os.environ.get("Laravel_Session","")
XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
KCRYPT = os.environ.get("KOLOP_CRYPT","")
DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
HCRYPT = os.environ.get("HUBDRIVE_CRYPT","")
KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")


# main thread
def mainthread(cmd,message):

    try:
        url = str(message.reply_to_message.text)
    except:
        try:
            url = str(message.text.split(f"{cmd} ")[1])
        except:
            app.send_message(message.chat.id, f"⚠️ __Invalid format, either__ **reply** __to a__ **link** __or use like this ->__ **{cmd} link**", reply_to_message_id=message.id)
            return

    # ola movies
    if cmd == "/ol":
        print("You Have Entered ola movies:",url)
        msg = app.send_message(message.chat.id, "🔎 __this might take some time...__", reply_to_message_id=message.id)
        link = bypasser.olamovies(url)
        
    # script links
    elif cmd == "/sc":
        print("You Have Entered script link:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        try:
            link = bypasser.getfirst(url)
        except:
            sess = requests.session()
            link = bypasser.getfinal(f'https://{url.split("/")[-2]}/',url, sess)
        
    # direct download link
    elif cmd == "/dl":
        print("You Have Entered ddl:",url)
        msg = app.send_message(message.chat.id, "⚡ __generating...__", reply_to_message_id=message.id)
        link = ddl.direct_link_generator(url)
        
    # katdrive
    elif cmd == "/kd":
        if KATCRYPT == "":
            app.send_message(message.chat.id, "🚫 __You can't use this because__ **KATDRIVE_CRYPT** __ENV is not set__", reply_to_message_id=message.id)
            return

        print("Entered Link katdrive:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.katdrive_dl(url, KATCRYPT)
        

    # hubdrive
    elif cmd == "/hd":
        if HCRYPT == "":
            app.send_message(message.chat.id, "🚫 __You can't use this because__ **HUBDRIVE_CRYPT** __ENV is not set__", reply_to_message_id=message.id)
            return

        print("Entered Link hubdrive:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.hubdrive_dl(url, HCRYPT)
        

    # drivefire
    elif cmd == "/df":
        if DCRYPT == "":
            app.send_message(message.chat.id, "🚫 __You can't use this because__ **DRIVEFIRE_CRYPT** __ENV is not set__", reply_to_message_id=message.id)
            return

        print("Entered Link drivefire:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.drivefire_dl(url, DCRYPT)
        

    # kolop
    elif cmd == "/ko":
        if KCRYPT == "":
            app.send_message(message.chat.id, "🚫 __You can't use this because__ **KOLOP_CRYPT** __ENV is not set__", reply_to_message_id=message.id)
            return

        print("Entered Link kolop:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.kolop_dl(url, KCRYPT)
        

    # filecrypt
    elif cmd == "/fc":
        print("You Have Entered filecrypt:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.filecrypt(url)
        

    # shareus
    elif cmd == "/su":
        print("You Have Entered shareus:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.shareus(url)
        

    # shortingly
    elif cmd == "/sg":
        print("You Have Entered shortingly:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.shortlingly(url)
        

    # gyanilinks
    elif cmd == "/gy":
        print("You Have Entered gyanilinks:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.gyanilinks(url)
        

    # pixl
    elif cmd == "/pi":
        print("You Have Entered pixl:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.pixl(url)
        

    # shorte
    elif cmd == "/st":
        print("You Have Entered shorte:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.sh_st_bypass(url)
        

    # psa
    elif cmd == "/ps":
        print("You Have Entered psa:",url)
        msg = app.send_message(message.chat.id, "🔎 __this might take some time...__", reply_to_message_id=message.id)
        link = bypasser.psa_bypasser(url)
        

    # sharer pw
    elif cmd == "/sh":
        if XSRF_TOKEN == "" or Laravel_Session == "":
            app.send_message(message.chat.id, "🚫 __You can't use this because__ **XSRF_TOKEN** __and__ **Laravel_Session** __ENV is not set__", reply_to_message_id=message.id)
            return

        print("Entered Link sharer:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.sharer_pw(url, Laravel_Session, XSRF_TOKEN)
        

    # gdtot url
    elif cmd == "/gt":
        print("Entered Link gdtot:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.gdtot(url,GDTot_Crypt)
        

    # adfly
    elif cmd == "/af":
        print("You Have Entered adfly:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        out = bypasser.adfly(url)
        link = out['bypassed_url']
 
    # gplinks
    elif cmd == "/gp":
        print("Entered Link gplink:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.gplinks(url)
        
    # droplink
    elif cmd == "/dp":
        print("You Have Entered droplink:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.droplink(url)
        
    # linkvertise
    elif cmd == "/lv":
        print("You Have Entered linkvertise:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.linkvertise(url)
        
    # rocklinks
    elif cmd == "/rl":
        print("You Have Entered rocklinks:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.rocklinks(url)
        
    # ouo
    elif cmd == "/ou":
        print("You Have Entered ouo:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.ouo(url)

    # gdrive look alike
    elif cmd == "/gd":
        print("You Have Entered gdrive:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.unified(url)

    # others
    elif cmd == "/ot":
        print("You Have Entered others:",url)
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        link = bypasser.others(url)

    # finnaly
    try:
        app.edit_message_text(message.chat.id, msg.id, f'__{link}__')
    except:
        app.edit_message_text(message.chat.id, msg.id, "__Failed to Bypass__")


AvailableCommands = ['ol','sc','dl','kd','hd','df','ko','fc','su','sg','gy','pi','st','ps','sh','gt','af','gp','dp','lv','rl','ou','gd','ot']
# commands
@app.on_message(filters.command(AvailableCommands))
def receive(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    bypass = threading.Thread(target=lambda:mainthread(message.text.split(" ")[0],message),daemon=True)
    bypass.start()


# start command
@app.on_message(filters.command(["start"]))
def send_welcome(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, "🔗 **Available Sites** \n\n  \
 `/dl` - __direct download link (/ddllist)__ \n  \
 `/af` - __adfly__ \n  \
 `/gp` - __gplinks__ \n  \
 `/dp` - __droplink__ \n  \
 `/lv` - __linkvertise__ \n  \
 `/rl` - __rocklinks__ \n  \
 `/gd` - __gdrive look-alike (/gdlist)__ \n  \
 `/ot` - __others (/otlist)__ \n  \
 `/ou` - __ouo__ \n  \
 `/gt` - __gdtot__ \n  \
 `/sh` - __sharer__ \n  \
 `/ps` - __psa__ \n  \
 `/st` - __shorte__ \n  \
 `/pi` - __pixl__ \n  \
 `/gy` - __gyanilinks__ \n  \
 `/sg` - __shortingly__ \n  \
 `/su` - __shareus__ \n  \
 `/fc` - __filecrypt__ \n  \
 `/ko` - __kolop__ \n  \
 `/df` - __drivefire__ \n  \
 `/hd` - __hubdrive__ \n  \
 `/kd` - __katdrive__ \n  \
 `/sc` - __script links__ \n  \
 `/ol` - __olamovies__ \n\n\
__reply to the link with command or use format /xx link__",
reply_to_message_id=message.id)


# gd list
@app.on_message(filters.command(['gdlist']))
def gdlis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list = """__- appdrive.in \n\
- driveapp.in \n\
- drivehub.in \n\
- gdflix.pro \n\
- drivesharer.in \n\
- drivebit.in \n\
- drivelinks.in \n\
- driveace.in \n\
- drivepro.in \n\
          __"""
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)


# others list
@app.on_message(filters.command(['otlist']))
def otlis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list="""__- exe.io/exey.io \n\
- sub2unlock.net/sub2unlock.com \n\
- rekonise.com \n\
- letsboost.net \n\
- ph.apps2app.com \n\
- mboost.me	\n\
- sub4unlock.com \n\
- ytsubme.com \n\
- bit.ly \n\
- social-unlock.com	\n\
- boost.ink	\n\
- goo.gl \n\
- shrto.ml \n\
- t.co \n\
- tinyurl.com
    __"""
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)    


# ddl list
@app.on_message(filters.command(['ddllist']))
def ddllis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list="""__- disk.yandex.com \n\
- mediafire.com \n\
- uptobox.com \n\
- osdn.net \n\
- github.com \n\
- hxfile.co \n\
- anonfiles.com \n\
- letsupload.io \n\
- 1drv.ms(onedrive) \n\
- pixeldrain.com \n\
- antfiles.com \n\
- streamtape.com \n\
- bayfiles.com \n\
- racaty.net \n\
- 1fichier.com \n\
- solidfiles.com \n\
- krakenfiles.com \n\
- upload.ee \n\
- mdisk.me \n\
- wetransfer.com \n\
- gofile.io \n\
- dropbox.com \n\
- zippyshare.com \n\
- megaup.net \n\
- fembed.net, fembed.com, femax20.com, fcdn.stream, feurl.com, layarkacaxxi.icu, naniplay.nanime.in, naniplay.nanime.biz, naniplay.com, mm9842.com \n\
- sbembed.com, watchsb.com, streamsb.net, sbplay.org
    __"""
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)     


# server loop
print("bot started")
app.run()
