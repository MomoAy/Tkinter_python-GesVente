#Les librairies importés
from subprocess import call
from tkinter import Tk,ttk
from tkinter import *
from tkinter import messagebox


def Retour():
    root.destroy()

def Achat():
    root.destroy()
    call(["python", "Python/Achaty.py"])

def Vente():
    root.destroy()
    call(["python", "Python/Gestion.py"])

#creation de fenetre
root = Tk()
root.title("BEAUGESS GESTION")
root.geometry("1080x800+450+120")
root.resizable(False,False)
root.configure(background="#808080")

#Ajout du titre
title = Label(root, borderwidth=3, relief= SUNKEN, text="BEAUGESS GESTION", font=("times new roman",45), bg="black",fg="white")
title.pack(side=TOP, fill=X)

#creation d'un Mainframe
Mainframe = Frame(root, bd=2, relief=GROOVE, bg="white")
Mainframe.place(x=10,y=100,width=1020,height=600)

#creation du frame des bouttons
btnframe = Frame(Mainframe, bd=2, relief=GROOVE, bg="black")
btnframe.place(x=10,y=20,width=1000,height=560)


#creation de boutton
btnVente = Button(btnframe, text="Gestion ventes", font=("times new roman",15), fg="black",bg="white",width=30,cursor="hand2", command=Vente)
btnVente.grid(row=0,column=0,sticky=W,padx=330,pady=40)

btnFournisseur = Button(btnframe, text="Gestion Fournisseurs", font=("times new roman",15), fg="black",bg="white",width=30,cursor="hand2", command=Achat)
btnFournisseur.grid(row=1,column=0,sticky=W,padx=330,pady=35)

btnProduits = Button(btnframe, text="Gestion Produits", font=("times new roman",15), fg="black",bg="white",width=30,cursor="hand2")
btnProduits.grid(row=2,column=0,sticky=W,padx=330,pady=35)

btnGerant = Button(btnframe, text="Espace Gerant", font=("times new roman",15), fg="black",bg="white",width=30,cursor="hand2")
btnGerant.grid(row=3,column=0,sticky=W,padx=330,pady=35)

btnquit = Button(btnframe, text="Quitter", font=("times new roman",15), fg="black",bg="white",width=30,cursor="hand2", command=Retour)
btnquit.grid(row=3,column=0,sticky=W,padx=330,pady=35)

#Execution 
root.mainloop() 