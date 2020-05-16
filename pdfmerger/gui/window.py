import tkinter as tk
from ..lib.loggingC import logging as l

class Window:
    def __init__(self, name = 'no name'):
        self._window = _createWindow(name)

    def mainloop(self):
        self._window.mainloop()

    def getWindow(self):
        return self._window

    

def _createWindow(name):
    l.debug('creating window')
    newWindow = tk.Tk()
    newWindow.title(name)
    newWindow.rowconfigure([0,1,2], weight=1, minsize=100)
    newWindow.columnconfigure([0], weight=1, minsize=300)
    return newWindow
