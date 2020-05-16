import os
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from . import labels, filesDict, filesHeap, parentInstance
from .label import Label
from ..lib.loggingC import logging

def setInstance(windowI, frame):
    '''
    imports window and frame instance from top-level script
    '''
    parentInstance.append(windowI)
    parentInstance.append(frame)

def openFile():
    isTampered = False
    
    filepath = askopenfilenames(
            filetypes=[("PDF Files", "*.PDF"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    for path in filepath:
        if path in filesDict:
            logging.debug(path + ' is already in dict!')
            continue
        filesDict[path] = os.path.basename(path)
        isTampered = True

    if isTampered:
        updateLabels()

def updateLabels():
    for x in labels:
        tmp = labels[x]
        tmp.getLabel().destroy()

    i = 1
    for file in filesDict:
        logging.info(filesDict[file])

        tmp = Label(parentInstance[1], filesDict[file])
        tmp.grid(i, 0)
        labels[file] = tmp
        i += i