# ============================================================================
# REFERENCES - XOR Starter Solution
# ============================================================================
# Key Concepts:
#   - XOR (Exclusive OR) Operation
#   - Bitwise Operations
#   - Pwntools Library
#
# Learning Resources Outside of College Work:
#   - XOR Cipher: https://en.wikipedia.org/wiki/XOR_cipher
#   - Python Bitwise Operators: https://realpython.com/python-bitwise-operators/
#   - W3Schools Operators: https://www.w3schools.com/python/python_operators.asp
#   - Pwntools XOR: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.xor
#
# Python Functions Used:
#   - xor() from pwntools: https://docs.pwntools.com/en/stable/util/fiddling.html
#   - .decode(): https://www.w3schools.com/python/ref_string_decode.asp
#   - f-strings: https://realpython.com/python-f-strings/
# ============================================================================

from pwn import xor #importing xor from pwntools

a =b"label"
b = 13

res = xor(a, b)
print(f"crypto{{{res.decode()}}}") 