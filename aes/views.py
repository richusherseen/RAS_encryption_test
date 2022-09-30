import re
from django.shortcuts import render
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64decode, b16decode
# Create your views here.

def unpad(s): return s[0:-s[-1]]

def home(request):
    print(request.method)
    if request.method == 'GET':
        print('in')
        return render(request, 'test.html')
    else:
        print(request.POST)
        print(request.POST['password'])
        # KEY = 'A1A2A3A4A5A6A7A8A9A1A2A3A4A5CAFE'.encode('utf8')
        # IV = 'A1A2A3A4A5A6A7A8'.encode('utf-8')
        # enc = base64.b64decode(request.POST['password'])
        # cipher = AES.new(KEY, AES.MODE_CBC, IV)
        # a = cipher.decrypt(enc)
        # print('a',a)
        # plain_text = unpad(a).decode('utf8')
        # print('plain_text',plain_text)
        decrypt(request.POST['password'])
        
def decrypt(crypt_text):
    private_key = """MIICXgIBAAKBgQCSuz3Ojj3+JvTx2tvtITUS+1xNeWZjiJEUcglj3j8VI4ZzcK96
    gyiU0gX81G+BVJXfL5wsOVG4Io/qPWbUXLGeiCtEXzfQr5aqX1tkjnp/7BmKDAto
    iRh3H4rfFAJsa8xzWvahvVH8Bo8qdDLxGr/rZTlFGzTAIppNusli1BeBOQIDAQAB
    AoGAOAh/Atk4/UxdL9r3L2gF/5iz1/YrTolBdgBSa6vchTMKzhzTNkLOBX7qwHFT
    n5zwmslwp0bAWUQBl18ZXLGFNkQXXDqx5WTBYR9+b73ao2NdWGmdePuESTPuciO9
    qYPinm58X76pakWQBdRDxoLpfjIff78gWA78qD5Lq0foIvECQQDFLljuVvM77d4z
    Rg2EFkzH4M2qI+TIoUvTiQWligOLS74XmKjbr/AHtQxKu3A7WhCwpyQkij5ev2Lu
    b2YSHm7dAkEAvoBT6J4B+QQ8QyoU+AQtmO0tR6CZ+B5VYwalX92NCnsj6J4oETIs
    aUqfP5iYqxt/u6RjhvRowHuFBUlpGM1gDQJBALbahx/nREMUEFXOJeSS5XsKDs8z
    4ArqAS5WyAS+WxEHGW46ZITtwBL1o0N+VNLFb+rR5ON5y+MDapQgfDBbRoUCQQCJ
    q6/4EgiW72qll0nkGxDgzbbFZtkeqL1IfUsSRshg5LEEsRd/peTWiukfSqY6MftT
    ne+XXhY91IZDVdQv6mwZAkEAjC7+rh5CUM/JwXRVKmHC7OUjvd3ym868fTxz6Xd8
    dLtLshBQztL5sxC2vMQ9fcPX/GEpTp8XhtlP5qsol99N5A=="""
    decode_data = b64decode(crypt_text)
    if len(decode_data) == 127:
        hex_fixed = '00' + decode_data.hex()
        decode_data = b16decode(hex_fixed.upper())
    other_private_key = RSA.importKey(b64decode(private_key))
    cipher = Cipher_PKCS1_v1_5.new(other_private_key)
    decrypt_text = cipher.decrypt(decode_data, None).decode()
    print(decrypt_text)