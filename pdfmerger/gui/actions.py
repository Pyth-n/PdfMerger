import os, PyPDF2
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from . import labels, filesDict, filesHeap, parentInstance
from .label import Label
from ..lib.loggingC import logging

merger = None

def setInstance(instances):
    '''
    imports window and frame instance from top-level script
    '''
    global parentInstance
    parentInstance = instances

def openFile():
    isTampered = False
    
    filepath = askopenfilenames(
            filetypes=[("PDF Files", "*.PDF"), ("All Files", "*.*")]
        )
    _elevateWindow()
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

def clear():
    '''
    clears the labels, file heap, and the pdf merger from memory
    '''
    global merger
    _closeFiles()
    _destroyLabels()

    if merger:
        merger.close()

def merge():
    global merger

    merger = PyPDF2.PdfFileMerger()
    _heapFiles(merger)
    _closeFiles() or _destroyLabels() if _savePdf(merger) else None
    merger.close()

def _updateLabels():
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
    _elevateWindow()
    if not filepath:
        return False

    with open(filepath, 'wb') as f:
        merger.write(f)

    return True

def _closeFiles():
    '''
        Closes the files allocated on heap
    '''
    for x in filesHeap:
        logging.debug(f'closing {filesHeap[x]}')
        filesHeap[x].close()

    filesHeap.clear()
    filesDict.clear()

def _destroyLabels():
    '''
    Destroys the labels that show the files open
    '''
    for x in labels:
        logging.debug(f'destroying {labels[x]}')
        labels[x].destroy()

    labels.clear()

def _elevateWindow():
    parentInstance[0].focus_force()
