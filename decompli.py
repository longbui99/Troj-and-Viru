from Crypto.Cipher import AES
with open("vrb2l.py", "rb") as f:
    nonces = f.read(16)
    data = f.read()
    action = AES.new(bytes("cecea2f38817e832c3e98309ae23c432",'utf-8'),mode=AES.MODE_EAX, nonce=nonces)
    result = action.decrypt(data)
    f.close()
    with open('vrb2l.py','wb') as fs:
        fs.write(result)
        fs.close()