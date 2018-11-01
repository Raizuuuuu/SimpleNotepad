from tkinter import Tk

class Notepad():
    def __init__(self, root):
        self.root = root        
        self.TITLE = "Notepad"
        self.file_path = None

        
if __name__ == "__main__":
    root = Tk()
    notepad = Notepad(root)
