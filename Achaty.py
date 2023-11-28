#Les librairies importés
import tkinter 
from tkinter import *
from tkinter import Tk,ttk
from cProfile import label
from subprocess import call
from tkinter import messagebox
#import mysql.connector

def Retour():
    root.destroy()
    call(["python", "Python/Acceuil.py"])

#creation de fenetre
root = Tk()
root.title("Gestion Achats") 
root.geometry("1260x800+450+120")
root.resizable(False,False)
root.configure(background="white")

#Ajout du titre
title = Label(root, borderwidth=3, relief= SUNKEN, text="GESTION DES ACHATS", font=("times new roman",45), bg="black",fg="white")
title.pack(side=TOP, fill=X)

#detail des achats
##espace Fournisseur
labelFournisseur = LabelFrame(root, text="Fournisseurs", font=("times new roman",15), bg="white")
labelFournisseur.place(x=10,y=100, width=400,height=170)

#matricule
lblmatricule = Label(labelFournisseur, text="Matricule", font=("times new roman",15,"bold"), bg="white")
lblmatricule.grid(row=0, column=0, sticky=W, padx=5,pady=2)
txtmatricule = Entry(labelFournisseur,bd=4,font=("times new roman",15))
txtmatricule.grid(row=0, column=1, sticky=W, padx=5,pady=2)

#FOURNISSEUR(Nom)
lblfournisseur = Label(labelFournisseur,text="Fournisseur",font=("times new roman",15,"bold"), bg="white")
lblfournisseur.grid(row=1, column=0, sticky=W, padx=5,pady=2)
txtfournisseur = Entry(labelFournisseur,bd=3,font=("times new roman",15))
txtfournisseur.grid(row=1, column=1, sticky=W, padx=5,pady=2)

#télephone
lblnumero = Label(labelFournisseur,text="Telephone",font=("times new roman",15,"bold"), bg="white")
lblnumero.grid(row=2, column=0, sticky=W, padx=5,pady=2)
txtnumero = Entry(labelFournisseur,bd=3,font=("times new roman",15))
txtnumero.grid(row=2, column=1, sticky=W, padx=5,pady=2)

#email
lblemail = Label(labelFournisseur, text="Mail", font=("times new roman",15,"bold"), bg="white")
lblemail.grid(row=3, column=0, sticky=W, padx=5, pady=2)
txtemail = Entry(labelFournisseur, bd=3,font=("times new roman",15))
txtemail.grid(row=3, column=1, sticky=W, padx=5, pady=2)

##espace Produits
#les labels
labelproduit = LabelFrame(root, text="Produits", font=("times new roman",15), bg="white")
labelproduit.place(x=430,y=100, width=800,height=170)

lblcategory = Label(labelproduit, text="Selectionner une categorie", font=("times new roman",15,"bold"), bg="white")
lblcategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

lblproduit = Label(labelproduit, text="Produits", font=("times new roman",15,"bold"), bg="white")
lblproduit.grid(row=1, column=0, sticky=W, padx=5, pady=2)

lblprix = Label(labelproduit, text="Prix", font=("times new roman",15,"bold"), bg="white")
lblprix.grid(row=2, column=0, sticky=W, padx=5, pady=2)

lblqtt = Label(labelproduit, text="Quantité", font=("times new roman",15,"bold"), bg="white")
lblqtt.grid(row=3, column=0, sticky=W, padx=5, pady=2)

lbltaxe = Label(labelproduit, text="Taxe", font=("times new roman",15,"bold"), bg="white")
lbltaxe.grid(row=0, column=2, sticky=W, padx=5, pady=2)

#les Entry
txtcategory = Entry(labelproduit, bd=3, font=("times new roman",15))
txtcategory.grid(row=0, column=1, sticky=W, padx=5,pady=2)

txtproduit = Entry(labelproduit, bd=3, font=("times new roman",15))
txtproduit.grid(row=1, column=1, sticky=W, padx=5,pady=2)

txtprix = Entry(labelproduit, bd=3, font=("times new roman",15))
txtprix.grid(row=2, column=1, sticky=W, padx=5,pady=2)

txtqtt = Entry(labelproduit, bd=3, font=("times new roman",15))
txtqtt.grid(row=3, column=1, sticky=W, padx=5,pady=2)

txttaxe = Entry(labelproduit, bd=3, font=("times new roman",15))
txttaxe.grid(row=0, column=3, sticky=W, padx=5,pady=2)


##Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=("times new roman",15), bg="black",fg="white", cursor="hand2")#, command=Ajouter)
btnenregistrer.place(x=400, y=300, width=100, height=30)

##Modifier
btnmodifier = Button(root, text="Modifier", font=("times new roman",15), bg="black",fg="white", cursor="hand2")#, command=Modifier)
btnmodifier.place(x=510, y=300, width=100, height=30)

##Supprimer
btnSupprimer = Button(root, text="Supprimer", font=("times new roman",15), bg="black",fg="white", cursor="hand2")#, command=Supprimer)
btnSupprimer.place(x=620, y=300, width=100, height=30)

##Retour
btnRetour = Button(root, text="Retour", font=("times new roman",15), bg="black",fg="white", cursor="hand2", command=Retour)
btnRetour.place(x=730, y=300, width=100, height=30)

##table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
table.place(x=10, y=350, width=1230, height=430)

#Entete
table.heading(1, text="CODE ACHAT")
table.heading(2, text="FOURNISSEUR")
table.heading(3, text="TELEPHONE")
table.heading(4, text="PRODUIT")
table.heading(5, text="PRIX")
table.heading(6, text="QUANTITE")

#dimensions de colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=50)

#afficher les infos de la table
# mabase = mysql.connector.connect(host=localhost, user=root, password="", database=achat)
# meConnect = mabase.cursor()
# meConnect.execute("select * from tb_achat")
# for row in meConnect:
#     table.insert('', END, value=row)
# mabase.close()
#execution
root.mainloop()