import os
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox as mb
from loggingC import logging

files = []
labels = []
filesDict = {}

# gets the path of opened files, stores in files[] global
def openFile():
    filepath = askopenfilenames(
            filetypes=[("PDF Files", "*.PDF"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    for path in filepath:
        files.append(path)
        filesDict[path] = os.path.basename(path)

    makeLabels()

def makeLabels():
    print(files)

    for i in range(len(files)):
        logging.info(files[i])
        label = tk.Label()
    

# configure window
window = tk.Tk()
window.title('PDF Merger')
window.rowconfigure([0,1], weight=1, minsize=100)
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

label = tk.Label(master=labelFrame, text="test")
label.grid(row=0, column=0, sticky='')

def show():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    mb.showinfo(title='welcome', message='success')

#window.after(500, show)
window.mainloop()


