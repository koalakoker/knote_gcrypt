from GCrypt import GCrypt_Initialize 
from GCrypt import GCrypt 
from GCrypt import GHashPass
from GCrypt import toHex

m_pass = "pignbcolada"
hash = GHashPass(m_pass,len(m_pass))

print format(hash,'08x')

GCrypt_Initialize(m_pass,len(m_pass)); # Initialize GCrypt

#m_testo = unicode("Nel mezzo del cammin di nostra vita mi ritrovai con nel cul una matita")
m_testo = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Angelica Farobasso</title>
</head><body><b><i><span style="font-size: 15pt">Angelica Farobasso</span></i></b><br/>
<br/>
<i><b>Nome:</b></i>&nbsp;Angelica Farobasso<br/>
<i><b>Professione:</b></i>&nbsp;Novizia dell'ordine delle "Sorelle della Luce"<br/>
<i><b>Aspetto fisico:</b></i>&nbsp;Alta 1 e 66. Bionda con gli occhi azzurri. Incarnato pallido.<br/>
<i><b>Aspetto sociologico:</b></i>&nbsp;Ha una sorella che le ha fatto da madre.<br/>
<br/>
<img src="screenshot.png" /></body></html>"""
m_cript = GCrypt('c', m_testo, len(m_testo))
print (m_cript)
print (toHex(m_cript))
m_testo_decript = GCrypt('d', m_cript, len(m_cript))
print (m_testo_decript)

if (m_testo != m_testo_decript):
    print "Errore!"
