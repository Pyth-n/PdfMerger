import os, logging
import tkinter as tk

# configure window
window = tk.Tk()
window.title('PDF Merger')
window.rowconfigure(0, weight=1, minsize=300)
window.columnconfigure([0, 1], weight=1, minsize=300)

# TODO: Label
text = tk.Label(master=window,text="Open PDF files:")
text.grid(row=0, column=0, sticky='e')

# TODO: open file button
openButton = tk.Button(master=window,text="Open")
openButton.grid(row=0, column=1, sticky='w')

window.mainloop()
