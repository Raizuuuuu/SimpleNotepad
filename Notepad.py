from tkinter import Tk, Text, mainloop

class Notepad():
    def __init__(self, root):
        self.root = root        
        self.title = "Notepad"
        self.file_path = None
        T = Text(self.root)
        T.pack()

        
if __name__ == "__main__":
    root = Tk()
    notepad = Notepad(root)
    mainloop()
