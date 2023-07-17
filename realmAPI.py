#access minecraft realms from the unoffical xbox api
#a pretty early project, my first time using APIs
#made December 2020
import requests
from datetime import date
from requests.auth import HTTPBasicAuth
print("to use this you must make an xapi.us account since this uses their API")
token = input("enter your token")
my_headers = {'X-AUTH' : token}
choose = ""
while choose != 1 and choose != 2 and choose != 3 and choose != 4:
    choose = int(input("would you like to (enter 1) see info on a realm, (enter 2) start tracking a realm, (enter 3) update a realm your tracking or (enter 4) view data collected from tracked realm")) 
if choose == 1:
    owner = input("enter an owner/members username")
    print('Please wait while you acsess the xbox API')
    owner = requests.get('https://xapi.us/v2/xuid/' + owner, headers=my_headers)
    if str(owner.json()) == '{"success":false,"error_code":404,"error_message":"XUID not found"}':
        print("could not find user.")
    else:
        clubs = requests.get('https://xapi.us/v2/clubs/joined/' + str(owner.json()), headers=my_headers)
        i = 0
        name = ""
        club = str(clubs.json())
        if club == '{"headers":{}}':
            print("in no realms")
        else:
            while i < len(club):
                if club[i] == "m" and club[i+1] == "e" and club[i+2] == "m" and club[i+3] == "b" and club[i+4] == "e" and club[i+5] == "r" and club[i+6] == "s" and club[i+7] == "C" and club[i+8] == "o" and club[i+9] == "u" and club[i+10] == "n" and club[i+11] == "t":
                    i +=14
                    flw = ""
                    while club[i] != ",":
                        flw = flw + club[i]
                        i+=1
                        print(name + " " + flw)
                elif club[i] == "n" and club[i+1] == "a" and club[i+2] == "m" and club[i+3] == "e":
                    i+=7
                    name = ""
                    while club[i] != ",":
                        name = name + club[i]
                        i+=1
                        name[:-1]
                else:
                    i+=1
if choose == 2:
    owner = input("enter an owner/members username")
    print('Please wait while you acsess the xbox API')
    owner = requests.get('https://xapi.us/v2/xuid/' + owner, headers=my_headers)
    if str(owner.json()) == '{"success":false,"error_code":404,"error_message":"XUID not found"}':
        print("could not find user")
    else:
        clubs = requests.get('https://xapi.us/v2/clubs/joined/' + str(owner.json()), headers=my_headers)
        i = 0
        name = ""
        club = str(clubs.json())
        if club == '{"headers":{}}':
            print("in no realms")
        else:
            print("copy and paste from the list which realm you would like to track:")
            trealms = []
            trealmsf = []
            while i < len(club):
                if club[i] == "n" and club[i+1] == "a" and club[i+2] == "m" and club[i+3] == "e":
                    i+=7
                    name = ""
                    while club[i] != ",":
                        name = name + club[i]
                        i+=1
                        name[:-1]
                    print(name)
                    trealms.append(name)
                elif club[i] == "m" and club[i+1] == "e" and club[i+2] == "m" and club[i+3] == "b" and club[i+4] == "e" and club[i+5] == "r" and club[i+6] == "s" and club[i+7] == "C" and club[i+8] == "o" and club[i+9] == "u" and club[i+10] == "n" and club[i+11] == "t":
                    i +=14
                    flw = ""
                    while club[i] != ",":
                        flw = flw + club[i]
                        i+=1
                    trealmsf.append(flw)
                else:
                    i+=1
            realm = ""
            while realm not in trealms:
                realm = input("enter the name of the realm you want to track from that")
            try:
                f = open(realm + ".txt", "x")
                i = 0
                while str(trealms[i]) != realm:
                  i+=1
                print(trealmsf[i])
                f.write("owner: " + str(owner) + ";" + "\n")
                f.write("name: " + realm + ";" + "\n")
                f.write("members: " + str(trealmsf[i]) + " on "  + str(date.today()))
                f.close()
            except:
                print("you are already tracking this realm!")
                f.close()
if choose == 3:
    file = input("choose the realm")
if choose == 4:
    file = input("choose the realm")
    f = open(file + ".txt", "r")
    print(f.read())
