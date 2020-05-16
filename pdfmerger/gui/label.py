import tkinter as tk
from ..lib.loggingC import logging as l

class Label:
    def __init__(self, master, text):
        self._master = master
        self._text = text

        self._label = tk.Label(master=self._master,text=self._text)
    
    def getLabel(self):
        return self._label

    def grid(self, row, column, sticky=''):
        self._row = row
        self._column = column
        self._sticky = sticky
        self.getLabel().grid(row = self._row, column = self._column, sticky = self._sticky)
