#!/usr/bin/python

import Tkinter as tk
import wikicontenthandler as wch

class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def setText(self):
        self.txtEntry.insert("1.0", wch.getContent())
        self.txtEntry['state'] = "disable"
        
    def createWidgets(self):
        self.txtEntry = tk.Text(self, width=80, height=25, wrap="word")
        
        self.setText()
        
        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.txtEntry.grid()
        self.btnQuit.grid()

def main():
    app = Application()
    app.master.title("Le saviez-vous ?")
    app.mainloop()
    
if __name__ == "__main__":
    main()
    

