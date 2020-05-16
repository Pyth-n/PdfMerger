# import os, PyPDF2
# import tkinter as tk
# from tkinter.filedialog import askopenfilenames, asksaveasfilename
# from tkinter import messagebox as mb
# from pdfmerger.custom.loggingC import logging

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

# def show():
#     window.attributes('-topmost', 1)
#     window.attributes('-topmost', 0)
#     mb.showinfo(title='welcome', message='success')

# #window.after(500, show)
# window.mainloop()


