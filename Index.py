from tkinter import *
from time import strftime
import os


class IndexBeaugess:
    def __init__(self, root):
        self.root = root
        self.root.title("Index Beaugess")
        self.root.geometry("1700x920")


        title = Label(self.root, text="Beaugess Gestion", font=("times new roman",45), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heu = strftime("%H:%M:%S")
            lbheure.config(text=heu)
            lbheure.after(1000,heure)


        lbheure = Label(self.root, text="HH:MM:SS", font=("times new roman",15,"bold"), bg="cyan", fg="black",)
        lbheure.place(x=0, y=15, width=120, height=45)
        heure()

        
if __name__ == "__main__":
    root = Tk()
    obj = IndexBeaugess(root)
    root.mainloop()