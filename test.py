if __name__ != '__main__':
    raise Exception('Not importable!')

from pdfmerger.gui.window import Window
from pdfmerger.gui.frame import Frame
from pdfmerger.gui.label import Label
from pdfmerger.gui.button import Button

a = Window('PDF Merger')
f = Frame(a.getWindow(), 'raised', 1)
f.grid(0, 0, 's')

l = Label(f.getFrame(), \
    'Open PDF files \N{RIGHTWARDS BLACK ARROW}')
l.grid(0,0)

b = Button(f.getFrame(), 'Open')
b.grid(0, 1)

a.mainloop()