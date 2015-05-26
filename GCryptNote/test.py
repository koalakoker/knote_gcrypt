from GCrypt import GCrypt_Initialize 
from GCrypt import GCrypt 
from GCrypt import GHashPass
from GCrypt import toHex

m_pass = "pignbcolada"
hash = GHashPass(m_pass,len(m_pass))

print format(hash,'08x')

GCrypt_Initialize(m_pass,len(m_pass)); # Initialize GCrypt

#m_testo = unicode("Nel mezzo del cammin di nostra vita mi ritrovai con nel cul una matita")
m_testo = "Nel mezzo del cammin di nostra vita mi ritrovai con nel cul una matita"
m_cript = GCrypt('c', m_testo, len(m_testo))
print (m_cript)
print (toHex(m_cript))
m_testo_decript = GCrypt('d', m_cript, len(m_cript))
print (m_testo_decript)

if (m_testo != m_testo_decript):
    print "Errore!"