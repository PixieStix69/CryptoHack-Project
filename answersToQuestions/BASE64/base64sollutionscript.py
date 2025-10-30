# ============================================================================
# REFERENCES - Base64 Encoding Solution
# ============================================================================
# Key Concepts:
#   - Hexadecimal to Bytes Conversion
#   - Base64 Encoding
#   - String Methods (.strip(), .decode())
#
# Learning Resources Outside of College Work:
#   - Base64 Tutorial: https://www.base64encode.org/
#   - Python base64 module: https://docs.python.org/3/library/base64.html
#   - Hex to Base64: https://base64.guru/converter/encode/hex
#   - W3Schools Base64: https://www.w3schools.com/python/ref_base64.asp
#
# Python Functions Used:
#   - bytes.fromhex(): https://docs.python.org/3/library/stdtypes.html#bytes.fromhex
#   - base64.b64encode(): https://docs.python.org/3/library/base64.html
#   - .decode(): https://www.w3schools.com/python/ref_string_decode.asp
# ============================================================================

import base64

hex_input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#step 1: convert hex to raw bytes
raw_bytes = bytes.fromhex(hex_input.strip())

#step 2: enocde that new raw bytes to base64
base64_bytes = base64.b64encode(raw_bytes)

print(base64_bytes.decode("utf-8")) #step 3: just prints out the answer 

