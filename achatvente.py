from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

def Achats():

    root.destroy()
    call(["python","Achats.py"])


#fonction ventes
def Ventes():
        root.destroy()
        call(["python", "Ventes.py"])


#ma fenetre
root = Tk()

root.title("beaugess gestion")
root.geometry("600x200+400+200")
root.resizable(False,False)
root.configure(background="blue")

#ajouter un titre

lbltitre = Label(root,borderwidth=3,relief=SUNKEN,text = "beaugess gestion",font=("times new roman",25),background="green",foreground="white")
lbltitre.place(x=0,y=0,width=600)


#bouton achats
btnenregistrer = Button(root,text= "ACHATS",font =("times new roman",24),bg="yellow",fg="white",command=Achats)
btnenregistrer.place(x=100,y=100,width=200)
#bouton vente
btnenregistrer = Button(root,text= "VENTES",font =("times new roman",24),bg="yellow",fg="white",command=Ventes)
btnenregistrer.place(x=300,y=100,width=200)



#exécution
root.mainloop()