import tkinter as tk
from ..lib.loggingC import logging as l

class Button:
    def __init__(self, master, text, command=''):
        l.debug('new Button instance')
        self._master = master
        self._text = str(text)
        self._command = command

        self._button = tk.Button(master=self._master,\
            text = self._text, command = self._command)

    def getButton(self):
        return self._button

    def grid(self, row, column, sticky = ''):
        self._row = row
        self._column = column
        self._sticky = sticky

        self.getButton().grid(row = self._row, column = self._column, \
            sticky = self._sticky)
