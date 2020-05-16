if __name__ != '__main__':
    raise Exception('Not importable!')

from pdfmerger.gui.window import Window
from pdfmerger.gui.frame import Frame
from pdfmerger.gui.label import Label
from pdfmerger.gui.button import Button

# main window
a = Window('PDF Merger')

# open file frame
f = Frame(a.getWindow(), 'raised', 3)
f.grid(0, 0, 's')

l = Label(f.getFrame(), \
    'Open PDF files \N{RIGHTWARDS BLACK ARROW}')
l.grid(0,0)

b = Button(f.getFrame(), 'Open')
b.grid(0, 1)


# list of files frame
labelFrame = Frame(a.getWindow(), 'raised', 1)
labelFrame.grid(1, 0, 'n')

# merge button frame
actionFrame = Frame(a.getWindow(), 'raised', 0)
actionFrame.grid(2, 0, 's')

mergeButton = Button(actionFrame.getFrame(), \
    'Merge')

mergeButton.grid(0, 0)

l3 = Label(actionFrame.getFrame(), \
    '2+ PDFs required', 'red')
l3.grid(1, 0)

# main window loop
a.mainloop()