if __name__ != '__main__':
    raise Exception('Not importable!')

from pdfmerger.gui.window import Window
from pdfmerger.gui.frame import Frame
from pdfmerger.gui.label import Label
from pdfmerger.gui.button import Button
from pdfmerger.gui.actions import openFile, setInstance, merge

# main window
a = Window('PDF Merger')

# open file frame
f = Frame(a.getWindow(), 'raised', 3)
f.grid(0, 0, 's')

l = Label(f.getFrame(), \
    'Open PDF files \N{RIGHTWARDS BLACK ARROW}')
l.grid(0,0)

b = Button(f.getFrame(), 'Open', openFile)
b.grid(0, 1)


# list of files frame
labelFrame = Frame(a.getWindow(), 'raised', 1)
labelFrame.grid(1, 0, 'n')

# merge button frame
actionFrame = Frame(a.getWindow(), 'raised')
actionFrame.grid(2, 0, 's')

mergeButton = Button(actionFrame.getFrame(),"Merge\n \N{HEAVY CHECK MARK}", merge)
mergeButton.grid(0, 0, 'w', [20,30], [20, 10])

clearButton = Button(actionFrame.getFrame(), \
    'Clear\n \N{ERASE TO THE LEFT}')
clearButton.grid(0, 1, 'e',  [20,30], [20, 10])

# label frame under actionFrame
labelFrame2 = Frame(a.getWindow(), 'raised', 1)
labelFrame2.grid(3, 0, 's')

l3 = Label(labelFrame2.getFrame(), \
    '2+ PDFs required', 'red')
l3.grid(1, 0, 'e')

# pass these instances to the gui package
setInstance(a.getWindow(), labelFrame.getFrame())

#a.getWindow().grid_columnconfigure(2, weight = 1, minsize = 100)

# main window loop
a.mainloop()