import os, PyPDF2
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
        _updateLabels()

def merge():
    merger = PyPDF2.PdfFileMerger()
    _heapFiles(merger)
    _closeFiles(merger) if _savePdf(merger) else None
    merger.close()

def _updateLabels():
    for x in labels:
        tmp = labels[x]
        tmp.getLabel().destroy()

    for index, file in enumerate(filesDict, start = 1):
        logging.info(filesDict[file])

        # the master of this label should be labelFrame
        tmp = Label(parentInstance[1], filesDict[file])
        tmp.grid(index, 0)
        labels[file] = tmp.getLabel()

def _heapFiles(merger):
    '''
        opens files and add it to the heap (doesn't close)
        files are also appended on the merger object
    '''
    for x in filesDict:
        tmp = open(x, 'rb')
        filesHeap[x] = tmp
        logging.debug(f'heaped {filesHeap[x]}')
        merger.append(tmp)

def _savePdf(merger):
    filepath = asksaveasfilename(
        filetypes = [("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if not filepath:
        return False

    with open(filepath, 'wb') as f:
        merger.write(f)

    return True

def _closeFiles(merger):
    '''
        Closes the files allocated on heap
    '''
    for x in filesHeap:
        logging.debug(f'closing {filesHeap[x]}')
        filesHeap[x].close()

    filesHeap.clear()

def _destroyLabels():
    '''
    Destroys the labels that show the files open
    '''
    for x in labels:
        logging.debug(f'destroying {labels[x]}')
        labels[x].destroy()

    labels.clear()