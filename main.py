# import os, PyPDF2
# import tkinter as tk
# from tkinter.filedialog import askopenfilenames, asksaveasfilename
# from tkinter import messagebox as mb
# from pdfmerger.custom.loggingC import logging

# labels = {}
# filesDict = {}
# filesHeap = {}

# # gets the path of opened files, stores in files[] global
# def openFile():
#     isTampered = False
    
#     filepath = askopenfilenames(
#             filetypes=[("PDF Files", "*.PDF"), ("All Files", "*.*")]
#         )
#     if not filepath:
#         return
#     for path in filepath:
#         if path in filesDict:
#             logging.debug(path + ' is already in dict!')
#             continue
#         filesDict[path] = os.path.basename(path)
#         isTampered = True

#     if isTampered:
#         updateLabels()

# # saves file to user's chosen path. clears memory when done
# def saveFile(merger):
#     # obtains the path of where the user wants to save
#     filepath = asksaveasfilename(
#         filetypes = [("PDF Files", "*.pdf"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         logging.warning("File save cancelled")
#         return
#     # save file
#     with open(filepath, 'wb') as f:
#         merger.write(f)

#     # close the files
#     for x in filesHeap:
#         tmp = filesHeap[x]
#         tmp.close()
#     # clear the heap
#     filesHeap.clear()

#     mb.showinfo('Saved Successfully', f'File was saved at {filepath}')

# def merge():
#     # create a merger instance
#     merger = PyPDF2.PdfFileMerger()

#     # show warning if less than 2 items are selected
#     if len(filesDict) < 2:
#         logging.warning('Less than 2 files selected')
#         mb.showerror('Merge Error', 'Must merge 2 or more PDF files')
#         return

#     # add opened files to heap, can't close yet until its merged
#     for x in filesDict:
#         tmp = open(x, 'rb')
#         merger.append(tmp)
#         filesHeap[x] = tmp

#     saveFile(merger)
#     merger.close()
    

# # update the labels when pdfs are selected
# def updateLabels():
#     for x in labels:
#         tmp = labels[x]
#         logging.debug(f'deleting {labels[x]}')
#         tmp.destroy()
    
#     i = 1
#     for x in filesDict:
#         # log key and value
#         logging.debug(f'key: {x}\tValue: {filesDict[x]}')
#         label = tk.Label(master=labelFrame, text=f'{filesDict[x]}')
#         label.grid(row=i, column=1)
#         labels[x] = label
#         i += 1

# def show():
#     window.attributes('-topmost', 1)
#     window.attributes('-topmost', 0)
#     mb.showinfo(title='welcome', message='success')

# #window.after(500, show)
# window.mainloop()


