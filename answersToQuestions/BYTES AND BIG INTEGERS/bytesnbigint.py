# ============================================================================
# REFERENCES - Bytes and Big Integers Solution
# ============================================================================
# Key Concepts:
#   - Large Integer Handling
#   - Integer to Bytes Conversion
#   - Multi-line String Concatenation
#   - ASCII Encoding
#
# Learning Resources Outside of College Work:
#   - Python Large Numbers: https://realpython.com/python-numbers/
#   - PyCryptodome Utilities: https://pycryptodome.readthedocs.io/en/latest/src/util/util.html
#   - ASCII Encoding: https://www.asciitable.com/
#   - Python int(): https://docs.python.org/3/library/functions.html#int
#
# Python Functions Used:
#   - long_to_bytes(): https://pycryptodome.readthedocs.io/en/latest/src/util/util.html
#   - int(): https://www.w3schools.com/python/ref_func_int.asp
#   - .decode(): https://docs.python.org/3/library/codecs.html
#   - f-strings: https://realpython.com/python-f-strings/
# ============================================================================

from Crypto.Util.number import long_to_bytes

n = int(
    "11515195063862318899931685488813747395775516" #first message
    "287289682636499965282714637259206269" #second message
    )
msg = long_to_bytes(n).decode("ascii") #use that function from the PyCryptodome library, then decode the message into ascii
print(f"crypto{{{msg}}}") #print the flag

#NOTE: flag prints weird for some reason I think its double wrapped but idk how to fix it :(