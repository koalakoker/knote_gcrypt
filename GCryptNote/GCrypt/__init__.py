'''
Created on 23/mag/2015

@author: koala
'''

import hashlib

from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

def hashIt(iStr):
    '''
    Used to hash the password and store it for later verification and access
    MD5 algorithm is used
    '''
    m = hashlib.md5()
    m.update(iStr)
    return m.hexdigest()

def criptIt(iStr,key):
    '''
    Used to crypt a string of text using a key. Crypted string is returned with the random seed and original text length
    Blowfish algorithm is used
    '''
    bs = Blowfish.block_size
    iv = Random.new().read(bs)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plen = bs - divmod(len(iStr),bs)[1]
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    return cipher.encrypt(iStr + padding), iv, len(iStr)
    
def deCriptIt(iStr,key,iv, originalLength):
    '''
    Used to decrypt a string of text. Key, seed and original length is required to decrypt original text.
    It returns the decrypted string. 
    Blowfish algorithm is used
    '''
    decipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return decipher.decrypt(iStr)[:originalLength]

def printHex(s):
    print(':'.join(x.encode('hex') for x in s))
