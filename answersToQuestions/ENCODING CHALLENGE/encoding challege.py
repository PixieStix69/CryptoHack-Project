# ============================================================================
# REFERENCES - Encoding Challenge Solution
# ============================================================================
# Key Concepts:
#   - Socket Programming with pwntools
#   - Multiple Encoding Schemes (base64, hex, rot13, bigint, utf-8)
#   - JSON Communication
#   - Remote Server Interaction
#
# Learning Resources Outside of College Work:
#   - Pwntools Documentation: https://docs.pwntools.com/
#   - Socket Programming: https://realpython.com/python-sockets/
#   - Python JSON: https://realpython.com/python-json/
#   - CTF Encoding: https://cryptohack.org/courses/intro/
#   - Base64: https://docs.python.org/3/library/base64.html
#   - ROT13: https://en.wikipedia.org/wiki/ROT13
#
# Python Functions Used:
#   - remote(): https://docs.pwntools.com/en/stable/tubes.html
#   - json.loads(): https://docs.python.org/3/library/json.html
#   - json.dumps(): https://docs.python.org/3/library/json.html
#   - base64.b64decode(): https://docs.python.org/3/library/base64.html
#   - codecs.decode(): https://docs.python.org/3/library/codecs.html
#   - bytes.fromhex(): https://docs.python.org/3/library/stdtypes.html#bytes.fromhex
# ============================================================================

from pwn import remote 
import json, base64, codecs 
from Crypto.Util.number import long_to_bytes

HOST, PORT = "socket.cryptohack.org", 13377 #host name n port num

def json_recv(r):
    line = r.recvline()
    return json.loads(line.decode())

def json_send(r, hsh):
    r.sendline(json.dumps(hsh).encode()) #fixed new line 


def decode_payload(typ, encoded) :
    #The server sends us a payload encoded in one of the following ways:
    #base64, hex, rot13, bigint, utf-8

    if typ == "base64" :
        return base64.b64decode(encoded).decode("utf-8")
    if typ == "hex" :
        return bytes.fromhex(encoded).decode("utf-8")
    if typ == "rot13" :
        return codecs.decode(encoded, "rot_13")
    if typ == "bigint" :

       # - The server takes the original text, turns it into bytes, then into a big integer,
       # - and finally shows that integer in hex with a "0x" prefix.
       # Example server path: "HELLO" -> b"HELLO" -> bytes_to_long(...) -> 0x48454c4c4f
        n = int(encoded, 16)
        return long_to_bytes(n).decode("utf-8")

    if typ == "utf-8" : #forgot to add utf-8 as an option
        #encoded is a list of byte values (ordinals) -> bytes -> str
        return bytes(encoded).decode("utf-8")
    raise ValueError(f"Unknown type: {typ}")



#main bit below!!

def main():
    r = remote(HOST, PORT, level="error")
    while True:
        data = json_recv(r) #FORGET TO ADD r ARGHHHH
        
        #server sends either a challenge or the final flag 
        if "flag" in data :
            print(data["flag"])
            break
        

        decoded = decode_payload(data["type"], data["encoded"]) #simplifying this into one line
        json_send(r, {"decoded": decoded})

if __name__ == "__main__":
    main()
    

