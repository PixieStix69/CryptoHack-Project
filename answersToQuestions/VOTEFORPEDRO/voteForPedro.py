# ============================================================================
# REFERENCES - Vote for Pedro Solution
# ============================================================================
# Key Concepts:
#   - RSA Low Exponent Attack (e=3)
#   - Signature Forgery
#   - Cube Root Computation
#   - Modular Arithmetic
#
# Learning Resources Outside of College Work:
#   - RSA Attacks: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks
#   - Low Exponent Attack: https://crypto.stackexchange.com/questions/6713/low-public-exponent-attack-for-rsa
#   - CryptoHack RSA: https://cryptohack.org/courses/public-key/
#   - Boneh's RSA Attacks: http://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
#   - GitHub Reference: https://github.com/AurtharPaul13/CRYPTOHACK-CHALLENGE/blob/main/Vote%20for%20Pedro.py
#
# Python Functions Used:
#   - pow(base, exp, mod): https://docs.python.org/3/library/functions.html#pow
#   - gmpy2.iroot(): https://gmpy2.readthedocs.io/en/latest/mpz.html#mpz-functions
#   - bytes_to_long(): https://pycryptodome.readthedocs.io/en/latest/src/util/util.html
#   - long_to_bytes(): https://pycryptodome.readthedocs.io/en/latest/src/util/util.html
# ============================================================================
from pwn import *
from json import *
from Crypto.Util.number import long_to_bytes, bytes_to_long 
import gmpy2 #for precise integer arithmetic

def send(hsh):#send the message to the server
    return r.sendline(dumps(hsh)) #send the message to the server

#Alice's public key
alice_N = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525181014287214350136557941201445475540830225059514652125310445352175047408966028497316806142156338927162621004774769949534239479839334209147097793526879762417526445739552772039876568156469224491682030314994880247983332964121759307658270083947005466578077153185206199759569902810832114058818478518470715726064960617482910172035743003538122402440142861494899725720505181663738931151677884218457824676140190841393217857683627886497104915390385283364971133316672332846071665082777884028170668140862010444247560019193505999704028222347577
alice_E = 3 #small public exponent

#The message we want after decryption
message = b'VOTE FOR PEDRO'

#need to add padding to the message so that when cubed (mod N) it equals the message
#3 > N 
padded_message = b'\x00' * 15 + message

#moved connection to the server further down 

#converting into integer
m = bytes_to_long(padded_message)

#compute the cube root of m
#need to find exact cude root so we need to find k such that k^3 = m
#have to use gmpy2 for precise integer arithmetic
vote, is_exact = gmpy2.iroot(m, 3)

# if the vote is not exact, increment it by 1 until we find the perfect cube!!
if not is_exact:
    vote = vote + 1

print(f"Message: {message}") #the message we want after decryption
print(f"Padded message: {padded_message}") #the padded message
print(f"Vote value: {vote}") #the vote value
print(f"Vote^3 mod N: {pow(vote, 3, alice_N)}") #the cube root of the padded message
print(f"Verification: {long_to_bytes(pow(vote, 3, alice_N))}") #the verification
print(f"After split: {long_to_bytes(pow(vote, 3, alice_N)).split(b'\\x00')[-1]}") #the message after splitting


r = remote("socket.cryptohack.org", 13375) #connection to the server
print(r.recv()) #print the message from the server


#####THIS CODE HERE IS FROM THAT GITHUB I REFERENCED, ITS BEEN EDITED BUT THE ORIGINAL CODE IS FROM THAT REPO!!#####
vote = 855520592299350692515886317752220783
option = {
    'option': 'vote',
    'vote': hex(vote)
}
send(option)

#add the reponse as get instead of get 
response = loads(r.recv().decode())
print(f"Response: {response}")

if 'flag' in response:
    print(f"Flag: {response['flag']}")
else:
    print(f"Error: {response['error']}")

r.close()

#########################################################