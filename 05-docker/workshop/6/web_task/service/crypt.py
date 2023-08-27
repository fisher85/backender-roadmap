from Crypto.Cipher import AES
import hashlib

BLOCK_SIZE = 16  # Bytes
pad = lambda s: ( s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE) )
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def MakeCookie(name):
    f = open("flag.txt", "r")
    flag = f.read()
    flag = flag[:-1]
    f.close()
    key = hashlib.sha256(flag.encode('utf-8')).hexdigest()
    c = AES.new(bytes.fromhex(key[0:32]), AES.MODE_ECB)
    print((pad(name + flag)).encode('utf-8').hex())
    cipher = (c.encrypt( (pad(name + flag)).encode('utf-8') ))
    cipher = cipher.hex()
    return cipher