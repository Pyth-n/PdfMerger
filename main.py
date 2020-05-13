import os
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox as mb
from loggingC import logging

labels = {}
filesDict = {}

# gets the path of opened files, stores in files[] global
def openFile():
    isTampered = False
    
    filepath = askopenfilenames(
            filetypes=[("PDF Files", "*.PDF"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    for path in filepath:
        if path in filesDict:
            logging.info(path + ' is already in dict!')
            continue
        filesDict[path] = os.path.basename(path)
        isTampered = True

    if isTampered:
        print('TAMPERED!')
        updateLabels()

# update the labels when pdfs are selected
def updateLabels():
    for x in labels:
        tmp = labels[x]
        logging.debug(f'deleting {labels[x]}')
        tmp.destroy()
    
    i = 1
    for x in filesDict:
        # log key and value
        logging.debug(f'key: {x}\tValue: {filesDict[x]}')
        label = tk.Label(master=labelFrame, text=f'{filesDict[x]}')
        label.grid(row=i, column=1)
        labels[x] = label
        i += 1

# configure window
window = tk.Tk()
window.title('PDF Merger')
window.rowconfigure([0,1,2], weight=1, minsize=100)
window.columnconfigure([0], weight=1, minsize=300)

openFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
openFrame.grid(row=0, column=0, sticky='')

# TODO: Label
text = tk.Label(master=openFrame,text="Open PDF files \N{RIGHTWARDS BLACK ARROW}")
text.grid(row=0, column=0, sticky='nsew')

# TODO: open file button
openButton = tk.Button(master=openFrame,text="Open", command=openFile)
openButton.grid(row=0, column=1, sticky='e')

labelFrame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
labelFrame.grid(row=1, column=0, sticky='n')

actionFrame = tk.Frame(master=window)
actionFrame.grid(row=2, column=0, sticky='')

mergeButton = tk.Button(master=actionFrame, text='Merge')
mergeButton.grid(row=0, column=0)

mergeLabel = tk.Label(master=actionFrame, text="2 or more PDFs \nrequired", fg="red")
mergeLabel.grid(row=1, column=0)

def show():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    mb.showinfo(title='welcome', message='success')

#window.after(500, show)
window.mainloop()


