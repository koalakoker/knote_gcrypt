'''
Created on 23/mag/2015

@author: koala
'''

import Cript

key = b'dfdfjdnjnjvnfkjn vnfj vjfk d nvkfd j'
plaintext = b'jfghksdjfghksdjfgksdhgljdkghjh fgh fhg jfhgdkjfkjg hkdfjg hkdfj ghkdf ghfdjk ghfdjkg hkdfjg h'
testoCriptato, seme, orLen = Cript.criptIt(plaintext, key)
testoDecriptato = Cript.deCriptIt(testoCriptato, key, seme, orLen)

# dec = cipher.decrypt(msg)

# def pr(iStr):
#     l = len(iStr)
#     print l
#     r = range(l)
#     print r
#     for i in r:
#         print i,iStr[i]

# print (Cript.hashIt("pippa"))
print (plaintext)
Cript.printHex(plaintext)
print ("seme")
Cript.printHex(seme)
print ("Testo Criptato")
Cript.printHex(testoCriptato)
print ("Testo decriptato")
print(testoDecriptato)
Cript.printHex(testoDecriptato)

if (plaintext != testoDecriptato):
    print ("Errore")
