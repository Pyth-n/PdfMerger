if __name__ != '__main__':
    raise Exception('Not importable!')

from pdfmerger.gui.window import Window
from pdfmerger.gui.frame import Frame

a = Window('PDF Merger')
f = Frame(a.getWindow(), 'raised', 1)
f.grid(0, 0)

a.mainloop()