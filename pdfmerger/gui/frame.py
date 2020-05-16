import tkinter as tk
from ..lib.loggingC import logging as l

reliefList = {
        'raised': tk.RAISED
}

class Frame:
    def __init__(self, master, relief = tk.FLAT, borderwidth=0):
        l.debug('created new frame instance')
        self._master = master
        self._relief = reliefList[relief]
        self._borderwidth = borderwidth

        self._frame = tk.Frame(master=self._master,\
             relief=self._relief, borderwidth=self._borderwidth)

    def getFrame(self):
        return self._frame

    def grid(self, row, column, sticky = ''):
        l.debug('creating grid')
        self._row = row
        self._column = column
        self._sticky = sticky
        self.getFrame().grid(row=self._row, column=self._column, sticky=self._sticky)
        # text = tk.Label(master=self.getFrame(),text="Open PDF files \N{RIGHTWARDS BLACK ARROW}")
        # text.grid(row=0, column=0, sticky='nsew')