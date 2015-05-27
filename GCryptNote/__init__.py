#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 24/mag/2015

@author: koala
'''

from keepnote.gui import extension

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
         
        self.gladefile = path + "/debugViewXML.glade"
        self.wTree = gtk.glade.XML(self.gladefile) 
        dic = {"on_CloseBtn_clicked" : self.on_CloseBtn_clicked}
        self.wTree.signal_autoconnect(dic)

    def debugTxt(self, iStr):
        #obj = self.builder.get_object("debugDialog")
        obj = self.wTree.get_widget("debugDialog")
        obj.show()
        #txtEdit = self.builder.get_object("debugTxt")
        txtEdit = self.wTree.get_widget("debugTxt")
        txtEdit.get_buffer().set_text(iStr)
        
    def on_CloseBtn_clicked(self,sender):
        obj = self.wTree.get_widget("debugDialog")
        obj.destroy()

class Extension (extension.Extension):
    
    lPath = ""
    
    def __init__(self, app):
        """Initialize extension"""
        
        extension.Extension.__init__(self, app)
        self.app = app
        
    def get_depends(self):
        return [("keepnote", ">=", (0, 7, 1))]


    def on_add_ui(self, window):
        """Initialize extension for a particular window"""
        
        # add menu options
        self.add_action(
            window, "Set password", _("Set password"),
            lambda w: self.on_setPassword(
                window, window.get_notebook()),
            tooltip=_("Set password for the notebook"))
        
        # TODO: Fix up the ordering on the affected menus.
        self.add_ui(window,
            """
            <ui>
            <menubar name="main_menu_bar">
               <menu action="File">
                   <menuitem action="Set password"/>
               </menu>
            </menubar>
            </ui>
            """)
        
        self.lPath = self.get_base_dir(False)
        self.hwg = debugView(self.lPath)
        
        #Gigi
        window.get_notebook()


    def on_setPassword(self, window, notebook):
        """Callback from gui for importing a plain text file"""
        
#         self.hwg.debugTxt(
#         """
#         Questa è una fidestra di debug in cui è possibile scrivere più o meno quello che si vuole
#         Proviamo a scrivere qualcosa su più righe
#         Solo per vedere come funziona!!!!
#         """)

        sys.path.append(self.lPath)
        
        from GCrypt import GCrypt_Initialize 
        from GCrypt import GCrypt 
        from GCrypt import GHashPass
        from GCrypt import toHex
        
        m_pass = "pignbcolada"
        hash = GHashPass(m_pass,len(m_pass))
        
        print format(hash,'08x')
        
        GCrypt_Initialize(m_pass,len(m_pass)); # Initialize GCrypt
        
        in_file = open(self.lPath + "/page.html","r")
        m_testo = in_file.read()
        in_file.close()
        
        m_cript = GCrypt('c', m_testo, len(m_testo))
        print (m_cript)
        print (toHex(m_cript))
        m_testo_decript = GCrypt('d', m_cript, len(m_cript))
        print (m_testo_decript)
        
        if (m_testo != m_testo_decript):
            print "Errore!"
        
        self.hwg.debugTxt(m_testo + "\n" + toHex(m_cript))