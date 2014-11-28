#!/usr/bin/python3.3

#-*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import wikicontenthandler as wch

class Application():
    
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.createWidgets()
        
    def setText(self):
        self.txtEntry1.insert("1.0", wch.getContentDidYouKnow())
        self.txtEntry1['state'] = "disable"
        self.txtEntry2.insert("1.0", wch.getContentLightOn())
        self.txtEntry2['state'] = "disable"
        
    def createWidgets(self):
        self.t1 = tk.Label(self.mainWindow, text="Le saviez-vous ?")
        self.t1.pack()
        self.txtEntry1 = tk.Text(self.mainWindow, width=80, height=12, wrap="word")
        self.txtEntry1.pack()
        
        self.t2 = tk.Label(self.mainWindow, text="Lumière sur :")
        self.t2.pack()
        self.txtEntry2 = tk.Text(self.mainWindow, width=80, height=12, wrap="word")
        self.txtEntry2.pack()
        
        self.setText()
    
if __name__ == "__main__":
    
    app = Application()
    app.mainWindow.title("Trivia")
    app.mainWindow.mainloop()
    

  

