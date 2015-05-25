'''
Created on 24/mag/2015

@author: koala
'''

import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

class debugView:
    """debug view"""
    
    def __init__(self,path):
        
        self.gladefile = path + "/debugView.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        
    def debugTxt(self, iStr):
        obj = self.builder.get_object("debugDialog")
        obj.show()
        txtEdit = self.builder.get_object("debugTxt")
        txtEdit.get_buffer().set_text(iStr)