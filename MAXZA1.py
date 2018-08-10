from ARIFISTIFIK import *
from AR.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pafy, youtube_dl
botStart = time.time()
arif = LineClient(authToken='EvdsUhs2RCW60RVftAnf.K9hUseF6j4f/WE5DLTHHBW.aiRtAaup010QtKAlnsahVfxbh/QQlmElhqFc9zyegzg=')
arif.log("Auth Token : " + str(arif.authToken))
channel = LineChannel(arif)
arif.log("Channel Access Token : " + str(channel.channelAccessToken))
#======================
settingsOpen = codecs.open("arifbots.json","r","utf-8")
poll = LinePoll(arif)
clientProfile = arif.getProfile()
clientSettings = arif.getSettings()
mid = arif.profile.mid
call = LineCall(arif)
#======
#======
KAC = [arif]
#======
pnharfbot = []
linkprotect = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
msg_dict = {}
msg_dict1 = {}
cancelprotect = {}
PROTECT = {}
settings = json.load(settingsOpen)
if settings["restartPoint"] != None:
    arif.sendText(settings["restartPoint"], "Bot kembali aktif")
switch = {
    'winvite':False,
    'dinvite':False,
    'wblacklist':False,
    'dblacklist':False,
    'wpeki':False,
    'dpeki':False,
    'cp1':False,
    'cp2':False,
    'changePicture':False
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
myProfile1 = {
	"displayName1": "",
	"statusMessage1": "",
	"pictureStatus1": ""
}
myProfile2 = {
	"displayName2": "",
	"statusMessage2": "",
	"pictureStatus2": ""
}
myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
myProfile1["displayName1"] = clientProfile.displayName
myProfile1["statusMessage1"] = clientProfile.statusMessage
myProfile1["pictureStatus1"] = clientProfile.pictureStatus
myProfile2["displayName2"] = clientProfile.displayName
myProfile2["statusMessage2"] = clientProfile.statusMessage
myProfile2["pictureStatus2"] = clientProfile.pictureStatus
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()
def logError(text):
    arif.log("[ ERROR ] " + str(text))
    time = datetime.now()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = random.choice(settings["userAgent"])
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        logError(e)
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+70)
        end_content = s.find(',"ow"',start_content-70)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            page = page[end_content:]
    return items
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "[Mention {} User]\n".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "? "
            else:
                try:
                    no = "[ {} ]".format(str(arif.getGroup(to).name))
                except:
                    no = "[ Success ]"
        arif.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        arif.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def backupData():
    try:
        backup = settings
        f = codecs.open('arifbots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def help():
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n┣🇮🇩🇮🇩BOT INDONESIA🇮🇩🇮🇩\n╰━━━🇮🇩ARIF🇮🇩̰̰̈́MH🇮🇩━━╯\n╭━━━━━━━━━━━━━━━╮" + "\n" + \
                  "┣🇮🇩 " + clientProfile.displayName + " 🇮🇩" + "\n" + \
                  "┣🇮🇩Help" + "\n" + \
                  "┣🇮🇩Set" + "\n" + \
                  "┣🇮🇩Me" + "\n" + \
                  "┣🇮🇩Add" + "\n" + \
                  "┣🇮🇩Creator" + "\n" + \
                  "┣🇮🇩Gcreator" + "\n" + \
                  "┣🇮🇩Sp" + "\n" + \
                  "┣🇮🇩Respon" + "\n" + \
                  "┣🇮🇩Tag" + "\n" + \
                  "┣🇮🇩Yoitubemp4 *txt" + "\n" + \
                  "┣🇮🇩Youtubemp3 *txt" + "\n" + \
                  "┣🇮🇩Gcall" + "\n" + \
                  "┣🇮🇩Clearban" + "\n" + \
                  "┣🇮🇩Clearchat" + "\n" + \
                  "┣🇮🇩Setmypict" + "\n" + \
                  "┣🇮🇩Setpictgroup" + "\n" + \
                  "┣🇮🇩Restart" + "\n" + \
                  "┣🇮🇩Virus" + "\n" + \
                  "┣🇮🇩Fuckname @" + "\n" + \
                  "┣🇮🇩Fuck@sirichan" + "\n" + \
                  "┣🇮🇩Fuckban" + "\n" + \
                  "┣🇮🇩Broken" + "\n" + \
                  "┣🇮🇩Nuke" + "\n" + \
                  "┣🇮🇩Reinvite" + "\n" + \
                  "┣🇮🇩Leaveto *gid" + "\n" + \
                  "┣🇮🇩Bl:on" + "\n" + \
                  "┣🇮🇩Unbl:on" + "\n" + \
                  "┣🇮🇩Unban @" + "\n" + \
                  "┣🇮🇩Ban @" + "\n" + \
                  "┣🇮🇩Kick@ban" + "\n" + \
                  "┣🇮🇩Banlist" + "\n" + \
                  "┣🇮🇩Clearban" + "\n" + \
                  "┣🇮🇩Prolink:on|off" + "\n" + \
                  "┣🇮🇩Proinvite:on|off" + "\n" + \
                  "┣🇮🇩Pro:on|off" + "\n" + \
                  "┣🇮🇩Namelock:on|off" + "\n" + \
                  "╰━━━🇮🇩ARIF🇮🇩̰̰̈́MH🇮🇩━━╯\n╭━━━━━━━━━━━━━━━╮\n┣🇮🇩🇮🇩BOT INDONESIA🇮🇩🇮🇩\n╰━━━🇮🇩ARIF🇮🇩̰̰̈́MH🇮🇩━━╯"
    return helpMessage
groupParam = ""
def SiriGetOut(targ):
    arif.kickoutFromGroup(groupParam,[targ])
def byuh(targ):
    random.choice(KAC).kickoutFromGroup(groupParam,[targ])
def bot(op):
    global time
    global ast
    global groupParam
    try:
#-----------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in settings['pname']:
                    try:
                        G = arif.getGroup(op.param1)
                    except:
                        try:
                            G = arif.getGroup(op.param1)
                        except:
                            try:
                                G = arif.getGroup(op.param1)
                            except:
                                pass
                    G.name = settings['pro_name'][op.param1]
                    try:
                        arif.updateGroup(G)
                    except:
                        try:
                            arif.updateGroup(G)
                        except:
                            try:
                                arif.updateGroup(G)
                            except:
                                pass
                    if op.param2 in Bots:
                        pass
                    elif op.param2 not in Bots:
                        pass
                    else:
                        try:
                            arif.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                arif.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            # Check if in group chat or personal chat
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 13:
                   if switch["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                            arif.sendText(to,"Succes add to blacklist")
                            switch["wblacklist"] = False
                       else:
                            settings["blacklist"][msg.contentMetadata["mid"]] = True
                            switch["wblacklist"] = False
                            arif.sendText(to,"contact blacklist di tambahkan")
                            print([msg.contentMetadata["mid"]] + " ADD TO BLACKLIST")
                   elif switch["dblacklist"] == True:
                       if msg.contentMetadata["mid"] in settings["blacklist"]:
                            del settings["blacklist"][msg.contentMetadata["mid"]]
                            arif.sendText(to,"Succes you whitelist")
                            switch["dblacklist"] = False
                            print([msg.contentMetadata["mid"]] + " ADD TO WHITELIST")
                       else:
                            switch["dblacklist"] = False
                            arif.sendText(to,"not is blacklist")
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        if text.lower() == 'sp':
                            start = time.time()
                            elapsed_time = time.time() - start
                            arif.sendText(to,"SPEED BOT\n" + "%seconds" % (elapsed_time) + "\nARIF BOT")
                        if text.lower() == "help":
                            helpMessage = help()
                            arif.sendText(to, str(helpMessage))
                        elif text.lower() == 'tag':
                            group = arif.getGroup(msg.to)
                            k = len(group.members)//20
                            for j in range(k+1):
                                aa = []
                                for x in group.members:
                                    aa.append(x.mid)
                                try:
                                    arrData = ""
                                    textx = "[ Mention {} Members ]\n1 - ".format(str(len(aa)))
                                    arr = []
                                    no = 1
                                    b = 1
                                    for i in aa:
                                        b = b + 1
                                        end = "\n"
                                        mention = "@x\n"
                                        slen = str(len(textx))
                                        elen = str(len(textx) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':i}
                                        arr.append(arrData)
                                        textx += mention
                                        if no < len(aa):
                                            no += 1
                                            textx += str(b) + " - "
                                        else:
                                            try:
                                                no = "[ {} ]".format(str(arif.getGroup(msg.to).name))

                                            except:
                                               no = "[ Success ]"
                                    msg.to = msg.to
                                    msg.text = textx
                                    msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                    msg.contentType = 0
                                    arif.sendMessage1(msg)
                                except Exception as e:
                                    arif.sendText(msg.to,str(e))
                        elif text.lower() == 'botak':
                            group = arif.getGroup(msg.to)
                            k = len(group.members)//20
                            for j in range(k+1):
                                aa = []
                                for x in group.members:
                                    aa.append(x.mid)
                                try:
                                    arrData = ""
                                    textx = "     [ Mention {} Members ]    \n1 - ".format(str(len(aa)))
                                    arr = []
                                    no = 1
                                    b = 1
                                    for i in aa:
                                        b = b + 1
                                        end = "\n"
                                        mention = "@x\n"
                                        slen = str(len(textx))
                                        elen = str(len(textx) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':i}
                                        arr.append(arrData)
                                        textx += mention
                                        if no < len(aa):
                                            no += 1
                                            textx += str(b) + " - "
                                        else:
                                            try:
                                                no = "[ {} ]".format(str(arif.getGroup(msg.to).name))

                                            except:
                                               no = "[ Success ]"
                                    msg.to = msg.to
                                    msg.text = textx
                                    msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                    msg.contentType = 0
                                    arif.sendMessage1(msg)
                                except Exception as e:
                                    arif.sendText(msg.to,str(e))
                        elif text.lower() == 'me':
                            arif.sendContact(to, sender)
                        elif text.lower() == 'add':		
                            arif.sendText(to,"❂•••••••••✧••••••••••❂")
                            arif.sendContact(to, 'u65224f4e8812136f01b25275a54b5aef')
                            arif.sendContact(to, 'u65224f4e8812136f01b25275a54b5aef')
                            arif.sendContact(to, 'u65224f4e8812136f01b25275a54b5aef')
                            arif.sendText(to,"❂•••••••••✧••••••••••❂")
                        elif text.lower() == 'creator':		
                            arif.sendText(to,"❂•••••••••✧••••••••••❂")
                            arif.sendContact(to, 'u65224f4e8812136f01b25275a54b5aef')
                            arif.sendText(to,"❂•••••••••✧••••••••••❂")
                        elif 'fuck1 ' in text.lower():
                           ulti0 = msg.text.replace("fuck1 ","")
                           ulti1 = ulti0.lstrip()
                           ulti2 = ulti1.replace("@","")
                           ulti3 = ulti2.rstrip()
                           _name = ulti3
                           gs = arif.getGroup(msg.to)
                           ginfo = arif.getGroup(msg.to)
                           gs.preventedJoinByTicket = False
                           arif.updateGroup(gs)
                           invsend = 0
                           Ticket = arif.reissueGroupTicket(msg.to)
                           arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                           time.sleep(0.2)
                           targets = []
                           for s in gs.members:
                               if _name in s.displayName:
                                  targets.append(s.mid)
                           if targets == []:
                           	sendMessage(to,"user does not exist")
                           else:
                               for target in targets:
                                    try:
                                        arif.kickoutFromGroup(msg.to,[target])
                                        print((msg.to,[g.mid]))
                                    except:
                                        arif.leaveGroup(msg.to)
                                        gs = arif.getGroup(msg.to)
                                        gs.preventedJoinByTicket = True
                                        arif.updateGroup(gs)
                                        gs.preventedJoinByTicket(gs)
                                        arif.updateGroup(gs)
                        elif 'fuck2 ' in text.lower():
                           ulti0 = msg.text.replace("fuck2 ","")
                           ulti1 = ulti0.lstrip()
                           ulti2 = ulti1.replace("@","")
                           ulti3 = ulti2.rstrip()
                           _name = ulti3
                           gs = arif.getGroup(msg.to)
                           ginfo = arif.getGroup(msg.to)
                           gs.preventedJoinByTicket = False
                           arif.updateGroup(gs)
                           invsend = 0
                           Ticket = arif.reissueGroupTicket(msg.to)
                           arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                           time.sleep(0.2)
                           targets = []
                           for s in gs.members:
                               if _name in s.displayName:
                                  targets.append(s.mid)
                           if targets == []:
                           	sendMessage(to,"user does not exist")
                           else:
                               for target in targets:
                                    try:
                                        arif.kickoutFromGroup(msg.to,[target])
                                        print((msg.to,[g.mid]))
                                    except:
                                        arif.leaveGroup(msg.to)
                                        gs = arif.getGroup(msg.to)
                                        gs.preventedJoinByTicket = True
                                        arif.updateGroup(gs)
                                        gs.preventedJoinByTicket(gs)
                                        arif.updateGroup(gs)
                        elif text.lower() == 'nuke':
                            if msg.toType == 2:
                                gs = arif.getGroup(msg.to)
#                                gs = arif.getGroup(msg.to)
#                                gs = arif.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    arif.sendText(msg.to,"kayak nya limit")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[arif,arif,arif]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif text.lower() == 'broken':
                            if msg.toType == 2:
                                gs = arif.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                arif.updateGroup(gs)
                                invsend = 0
                                Ticket = arif.reissueGroupTicket(msg.to)
                                arif.acceptGroupInvitationByTicket(msg.to,Ticket)
#                                arif.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    arif.sendText(msg.to,"DRAG KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[arif]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif text.lower() == 'arif:in':
                            G = arif.getGroup(msg.to)
                            ginfo = arif.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            arif.updateGroup(G)
                            invsend = 0
                            Ti = arif.reissueGroupTicket(msg.to)
                            arif.acceptGroupInvitationByTicket(to,Ti)
#                            arif.acceptGroupInvitationByTicket(to,Ti)
                            G = arif.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            G.preventedJoinByTicket(G)
                            arif.updateGroup(G)
                        elif text.lower() == 'arif:out':
                            arif.leaveGroup(msg.to)
#                            arif.leaveGroup(msg.to)
                        elif text.lower() == 'reinvite':
                            arif.leaveGroup(msg.to)
#                            arif.leaveGroup(msg.to)
                            G = arif.getGroup(msg.to)
                            ginfo = arif.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            arif.updateGroup(G)
                            invsend = 0
                            Ti = arif.reissueGroupTicket(msg.to)
                            arif.acceptGroupInvitationByTicket(to,Ti)
#                            arif.acceptGroupInvitationByTicket(to,Ti)
                            G = arif.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            G.preventedJoinByTicket(G)
                            arif.updateGroup(G)
                        elif text.lower() == 'fuck@sirichan':
                            gs = arif.getGroup(msg.to)
#                            gs = arif.getGroup(msg.to)
#                            gs = arif.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん","0","1","2","3","4","5","6","7","8","9"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriGetOut,sirilist)
                                    p.close()
                                except:
                                    p.close()
                        elif text.lower() == 'fuckname ':
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                   groupParam = msg.to
                                   try:
                                       p = Pool(40)
                                       p.map(byuh,targets)
                                       p.close()
                                       p.terminate()
                                       p.join
                                   except Exception as error:
                                       p.close()
                                       return
                        elif 'leaveto ' in text.lower():
                            gids = msg.text.replace('leaveto ',"")
                            gid = arif.getGroup(gids)
                            try:
                                arif.leaveGroup(gids)
#                                arif.leaveGroup(gids)
                            except:
                                arif.sendText(to,"Succes leave to group " + gids.name)
#                                arif.sendText(to,"Succes leave to group " + gids.name)
                        elif text.lower() == 'mybots':		
                            arif.sendContact(to, mid)
#                            arif.sendContact(to, Bmid)
                        elif text.lower() == 'call':
                            if msg.toType == 2:
                                group = arif.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                arif.sendText(msg)
                        elif text.lower() == 'clearchat':
                            arif.removeAllMessages(op.param2)
                            arif.sendText(to, "Done")
                        elif 'youtubemp3 ' in text.lower():
                            try:
                                arif.sendText(msg.to,"Waitting progress...")
                                textToSearch = (msg.text).replace('youtubemp3 ', "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.audiostreams
                                for s in stream:
                                    start = timeit.timeit()
                                    vin = s.url
                                    img = vid.bigthumbhd
                                    hasil = vid.title
                                    hasil += '\n\nDi upload oleh ✍️ ' +str(vid.author)
                                    hasil += '\nDurasi ⏱️ ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                    hasil += '\nDi Like sebanyak👍 ' +str(vid.rating)
                                    hasil += '\nDi tonton sebanyak 👬 ' +str(vid.viewcount)+ 'x '
                                    hasil += '\nDi upload pada 📆 ' +vid.published
                                    hasil += '\n\nWaktunya⏲️ %s' % (start)
                                    hasil += '\n\n Waitting proses mp3....'
                                arif.sendAudioWithURL(msg.to,vin)
                                arif.sendImageWithURL(msg.to,img)
                                arif.sendText(msg.to,hasil)
                            except:
                                arif.sendText(msg.to,"Gagal Mencari...")
                        elif 'youtubemp4 ' in text.lower():
                            try:
                                arif.sendText(msg.to,"Waitting progress..")
                                textToSearch = (msg.text).replace('youtubemp4 ', "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = '🎀 Informasi 🎀\n\n'
                                    hasil += '★Judul video★\n ' + vid.title
                                    hasil += '\n Tunggu encoding selesai...'
                                arif.sendVideoWithURL(msg.to,vin)
                                arif.sendText(msg.to,hasil)
                                print("[Notif] Search Youtube Success")
                            except:
                                arif.sendText(msg.to,"Gagal")
#=====COMMEND SETTINGS=======
                        elif text.lower() == 'bl:on':
                            switch["wblacklist"] = True
                            arif.sendText(to,"Send contact")
                        elif text.lower() == 'unbl:on':
                            switch["dblacklist"] = True
                            arif.sendText(to,"Send contact")
                        elif text.lower() == 'clearban':
                            settings["blacklist"] = {}
                            arif.sendText(to,"BLACKLIST ALL DELETED")
                        elif 'unban ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del settings["blacklist"][ls]
                                        arif.sendText(to,"ðdoneð")
                                    except:
                                        arif.sendText(to,"Error")
                        elif text.lower() == 'kick@mbl':
                            group = arif.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in wait["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                arif.sendText(to,"Tak ada yang berdosa")
                                return
                            for jj in matched_list:
                                try:
                                    random.choice(KAC).kickoutFromGroup(to,[jj])
                                    print((to,[jj]))
                                except:
                                    pass
                        elif text.lower() == '_':
                            arif.sendContact(to, "'xxx")
                            arif.sendText(msg)  
                        elif 'ban ' in text.lower():
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["blacklist"][ls] = True
                                        arif.sendText(to,"â¨ï¸TARGET BLACKLIST DI TAMBAHKANâ¨ï¸")
                                    except:
                                        arif.sendText(to,"Error")
                        elif text.lower() == 'banlist':
                                if settings["blacklist"] == {}:
                                    arif.sendText(to,"Noting blacklist...")
                                else:
                                    arif.sendText(to,"Prossesing..")
                                    mc = "â ï¸ DAFTAR BLACKLIST â ï¸ \n\n"
                                    for mi_d in settings["blacklist"]:
                                        mc += "ð¤  " +arif.getContact(mi_d).displayName + "\n"
                                    arif.sendText(to,mc)
#=================+
                        elif text.lower() == 'gcreator':
                            try:
                                group = arif.getGroup(msg.to)
                                GS = group.creator.mid
                                arif.sendContact(to, GS)
                                arif.sendText(msg.to,"PEMBUAT GRUP INI") 
                            except:
                                W = group.members[0].mid
                                arif.sendContact(to, W)
                                arif.sendText(msg.to,"PEMBUAT GRUP INI") 

#======PROTECT======#
                        elif text.lower() == 'prolink:on':
                                settings["linkprotect"][msg.to] = True
                                arif.sendText(to,"GROUP QR ALREADY BLOCKED")
                                print("[PROTECT QR DI AKTIFKAN]")
                        elif text.lower() == 'prolink:off':
                                try:
                                    del settings["linkprotect"][msg.to]
                                    arif.sendText(to,"QR CODE ALREADY UNBLOCKED")
                                except:
                                    arif.sendText(to,"QR CODE DONE UNBLOCKED")
                                    print("[PROTECT QR DIMATIKAN]")
                        elif text.lower() == 'namelock:on':
                            if msg.to in settings['pname']:
                                arif.sendText(to,"GROUP NAME ALREADY BLOCKED")
                            else:
                                arif.sendText(to,"GROUP NAME HAS BEN BLOCKED")
                                settings['pname'][msg.to] = True
                                settings['pro_name'][msg.to] = arif.getGroup(msg.to).name
                        elif text.lower() == 'namelock:off':
                            if msg.to in settings['pname']:
                                arif.sendText(to,"GROUP NAME ALREADY UNBLOCKED")
                                del settings['pname'][msg.to]
                            else:
                                arif.sendText(to,"GROUP NAME HAS BEN UNBLOCKED")          
                        elif text.lower() == 'proinvite:on':
                                settings["cancelprotect"][msg.to] = True
                                arif.sendText(to,"GROUP INVITE ALREADY BLOCKED")
                                print("[PROTECT INVITE DI AKTIFKAN]")
                        elif text.lower() == 'proinvite:off':
                                try:
                                    del settings["cancelprotect"][msg.to]
                                    arif.sendText(to,"GROUP INVITE ALREADY UNBLOCKED")
                                except:
                                    arif.sendText(to,"GROUP INVITE HAS BEN UNBLOCKED")
                                    print("[PROTECT INVITE DIMATIKAN]")
                        elif text.lower() == 'pro:on':
                             try:
                                settings["PROTECT"][msg.to] = True
                                arif.sendText(to,"BLOCKED MEMBER ALREADY ACTIVE")
                                print("[Perintah]block kick")
                             except:
                                arif.sendText(to,"BLOCKED MEMBER HAS BEN ACTIVE")
                        elif text.lower() == 'pro:off':
                                try:
                                    del settings["PROTECT"][msg.to]
                                    arif.sendText(to,"ALREADY UNBLOCKED MEMBER")
                                except:
                                    arif.sendText(to,"BLOCKED MEMBER HAS BEN NON ACTIVE")
                                    print("[Perintah]Allow kick")
                        elif text.lower() == 'set':
                                 md = "╔▬▬∂ґ в❍тs▬▬╗\n║▬▬▬ă▬▬в▬▬▬║\n"
                                 if msg.to in settings["cancelprotect"]: md+="║☆║PROIVITE:ON➡️📱\n"
                                 else: md+="║☆║PROINVITE:OFF➡️📴\n"
                                 if msg.to in settings["PROTECT"]: md+="║☆║PROTECT:ON➡️📱\n"
                                 else: md+="║☆║PROTECT:OFF➡️📴\n"
                                 if msg.to in settings["linkprotect"]: md+="║☆║PROLINK:ON➡️📱\n"
                                 else: md+="║☆║PROLINK:OFF➡️📴\n"
                                 if msg.to in settings["pname"]: md+="║☆║NAMELOCK:ON➡️📱\n"
                                 else: md+="║☆║NAMELOCK:OFF➡️📴\n"
                                 arif.sendText(to,md + "║▬▬▬ă▬▬в▬▬▬║\n╚▬▬∂ґ в❍тs▬▬╝")
#=================+
                        elif text.lower() == 'setmypict':
                            switch["changePicture"] = True
                            arif.sendText(to, "Send to pictures")
                        elif text.lower() == 'setbotpict1':
                            switch["cp1"] = True
                            arif.sendText(to, "Send asisten 1 pictures")
                        elif text.lower() == 'setbotpict2':
                            switch["cp2"] = True
                            arif.sendText(to, "Send asisten 2 pictures")
                        elif text.lower() == 'setpictgrup':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                arif.sendText(to, "Send group pictures")
                        elif text.lower() == 'respon':
                            s1 = arif.getProfile()
                            s2 = arif.getProfile()
                            arif.sendText(msg.to, s1.displayName + " Already..")
#                            arif.sendText(msg.to, s2.displayName + " Already..")
#---------------------------------------------------
                        elif msg.text in ['cancel']:
                            if msg.toType == 2:
                                group = arif.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    arif.cancelGroupInvitation(msg.to,[_mid]) 
                elif msg.contentType == 1:
                    if switch["changePicture"] == True:
                        path = arif.downloadObjectMsg(msg_id)
                        switch["changePicture"] = False
                        arif.updateProfilePicture(path)
                        arif.sendText(to, "PP diganti")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = arif.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            arif.updateGroupPicture(to, path)
                            arif.sendText(to, "Berhasil mengubah foto group")
                    if switch["cp1"] == True:
                        path = arif.downloadObjectMsg(msg_id)
                        switch["cp1"] = False
                        arif.updateProfilePicture(path)
                        arif.sendText(to, "PP bot 1 diganti")
                    if switch["cp2"] == True:
                        path = arif.downloadObjectMsg(msg_id)
                        switch["cp2"] = False
                        arif.updateProfilePicture(path)
                        arif.sendText(to, "PP bot 2 diganti")
        if op.type == 19:
            if mid in op.param3:
                print("Asist 1 backup selfbot")
                if op.param2 in Bots:
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        print("Bots1 Joined openqr")
                    except:
                        pass
            if Amid in op.param3:
                print("Asist 1 backup selfbot")
                if op.param2 in Bots:
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        print("Bots1 Joined openqr")
                    except:
                        pass
            if Bmid in op.param3:
                print("Asist 1 backup selfbot")
                if op.param2 in Bots:
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                    arif.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = arif.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    arif.updateGroup(X)
                    Ti = arif.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    print("Kicker has been blacklist")
                    try:
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
#                        arif.acceptGroupInvitationByTicket(op.param1,Ti)
                        X = arif.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        arif.updateGroup(X)
                        Ti = arif.reissueGroupTicket(op.param1)
                        arif.kickoutFromGroup(op.param1,[op.param2])
                        print("Bots1 Joined openqr")
                    except:
                        pass
        if op.param3 == "4":
          if op.param1 in settings["linkprotect"]:
            if op.param1 in settings["PROTECT"]:
             if op.param2 not in Bots:
                pass
             else:
                 arif.kickoutFromGroup(op.param1,[op.param2])
                 settings["blacklist"][op.param2] = True
                 arif.reissueGroupTicket(op.param1)
                 X = arif.getGroup(op.param1)
                 X.preventedJoinByTicket = True
                 arif.updateGroup(X)
                 settings["blacklist"][op.param2] = True
            else:
             if op.param2 in Bots:
                pass
             else:
                 arif.reissueGroupTicket(op.param1)
                 X = arif.getGroup(op.param1)
                 X.preventedJoinByTicket = True
                 arif.updateGroup(X)
        if op.type == 32:
          if op.param1 in settings["PROTECT"]:
            if op.param2 in Bots:
                pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                contact = arif.getContact(op.param2)
                arif.kickoutFromGroup(op.param1,[op.param2])
                settings["blacklist"][op.param2] = True
        if op.type == 13:
         if op.param1 in settings["cancelprotect"]:
          if op.param1 in settings["PROTECT"]:
            if op.param2 not in Bots:
               pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                for _mid in InviterX:
                    arif.cancelGroupInvitation(op.param1,[_mid])
                arif.kickoutFromGroup(op.param1,[op.param2])
                settings["blacklist"][op.param2] = True
          else:
            if op.param2 in Bots:
               pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                for _mid in InviterX:
                    arif.cancelGroupInvitation(op.param1,[_mid])
                arif.cancelGroupInvitation(op.param1,InviterX)
        if op.type == 17:
            if mid in op.param3:
                    group = arif.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in settings["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        arif.sendText(to,"nothing blacklist")
                        return
                    for jj in matched_list:
                        arif.kickoutFromGroup(to,[jj])
#                        arif.kickoutFromGroup(to,[jj])
#                        arif.kickoutFromGroup(to,[jj])
                    arif.sendText(to,"done")
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
            	if op.param2 not in Bots:
                   arif.kickoutFromGroup(op.param1,[op.param2])
                   arif.sendContact(op.param1,[op.param2])
                   arif.sendText(op.param1,"di blacklist goblok\etaterngkanlah...")
            else:
                pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
        backupData()
    except Exception as error:
        logError(error)
while True:
    try:
        autoRestart()
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        logError(e)
