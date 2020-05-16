import tkinter as tk
from ..lib.loggingC import logging as l

class Window:
    def __init__(self, name = 'no name'):
        _window = _createWindow(name)
        _window.mainloop()

def _createWindow(name):
    l.debug('creating window')
    newWindow = tk.Tk()
    newWindow.title('PDF Merger')
    return newWindow
    

