import tkinter
from cProfile import label
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
# import mysql



def Retour():
    root.destroy()
    call("python","Vente.py" )

def Ajouter():
    matricule = txtnumero.get()
    client = txtclient.get()
    telephone = txttelephone.get()
    produit = comboproduits.get()
    prix_achat = txtprix.get()
    quantite_achte = txtquantité.get()

    # maBase = mysql .connect(host="localhost", user="root", password="1234", database="vente")
    # meConnect = maBase.cursor()


    try:
        sql = "INSERT INTO tb_achat(code,client,telephone,produit,prix,quantité) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (matricule,fournisseur,telephone,produit,prix_achat,quantite_achte)
        meConnect.execute(sql,val)
        maBase.commit()
        dernierMatricule = meConnect.lastrowid
        messagebox.showinfo("informations","vente ajouter")
        root.destroy()
        call(["python","Vente.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def Modifier():
    matricule = txtnumero.get()
    client = txtclient.get()
    telephone = txttelephone.get()
    produit = comboproduits.get()
    prix_achat = txtprix.get()
    quantite_achte = txtquantité.get()

    maBase = mysql .connect(host="localhost", user="root", password="1234", database="vente")
    meConnect = maBase.cursor()


    try:
        sql = "update tb_achat set client=%s,telephone=%s,produits=%s,prix=%s,quantité=%s where code= %s"
        val(client,telephone,produit,prix_achat,quantite_achte,matricule)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information","vente modifier")
        root.destroy()
        call(["python","Vente.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def Supprimer():
    matricule = txtnumero.get()

    maBase = mysql .connect(host="localhost", user="root", password="1234", database="vente")
    meConnect = maBase.cursor()

    try:
        sql = "select from tb_vente where code=%s"
        val = (matricule)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information","vente supprimer")
        root.destroy()
        call(["python","Vente.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()








#fenetre
root = Tk()

root.title("MENUE VENTE")
root.geometry("1350x700+0+0")
root.resizable(False,False)
root.configure(background="blue")


#ajouter un titre
lbltitre = Label(root,borderwidth=3,relief=SUNKEN,text = "beaugess gestion",font=("times new roman",25),background="green",foreground="white")
lbltitre.place(x=0,y=0,width=1350,height=100)


#details

#matricule
lblnumero = Label(root,text="MARICULE",font=("times new roman",15),bg="green",fg="white")
lblnumero.place(x=70,y=150,width=150)
txtnumero = Entry(root,bd=4,font=("times new roman",25))
txtnumero.place(x=250,y=150,width=150)

#CLIENTS
lblnumero = Label(root,text="CLIENT",font=("times new roman",15),bg="green",fg="white")
lblnumero.place(x=50,y=200,width=200)
txtnumero = Entry(root,bd=3,font=("times new roman",25))
txtnumero.place(x=250,y=200,width=300)

#télephone
lblnumero = Label(root,text="TELEPHONE",font=("times new roman",15),bg="green",fg="white")
lblnumero.place(x=70,y=250,width=150)
txtnumero = Entry(root,bd=3,font=("times new roman",25))
txtnumero.place(x=250,y=250,width=300)


#Ventes
lblproduits = Label(root,text="PRODUITS",font=("times new roman",15),bg="green",fg="white")
lblproduits.place(x=550,y=150,width=150)

comboproduits = ttk.Combobox(root,font=("times new roman",15))
comboproduits["values"] = ["autres"]
comboproduits.place(x=700,y=150,width=150)

#prix
lblprix = Label(root,text="PRIX",font=("times new roman",15),bg="green",fg="white")
lblprix.place(x=550,y=200,width=150)
txtprix = Entry(root,bd=3,font=("times new roman",25))
txtprix.place(x=700,y=200,width=150)

#quantité
lblquantité = Label(root,text="QUANTITE",font=("times new roman",15),bg="green",fg="white")
lblquantité.place(x=550,y=250,width=150)
txtquantité = Entry(root,bd=3,font=("times new roman",25))
txtquantité.place(x=700,y=200,width=150)


#enrégistrer
btnenregistrer = Button(root,text= "ENREGISTRER",font =("times new roman",15),bg="yellow",fg="white",command=Ajouter)
btnenregistrer.place(x=1000,y=140,width=200)

#modifier
btnenregistrer = Button(root,text= "MODIFIER",font =("times new roman",15),bg="yellow",fg="white",command=Modifier)
btnenregistrer.place(x=1000,y=190,width=200)

#suprimer
btnsupprimer = Button(root,text= "SUPPRIMER",font =("times new roman",24),bg="yellow",fg="white",command=Supprimer)
btnsupprimer.place(x=1000,y=240,width=200)

#retour
btnretour = Button(root,text= "RETOUR",font =("times new roman",24),bg="red",fg="white",command=Retour)
btnretour.place(x=1240,y=240,width=100)


#table
table = ttk.Treeview(root,columns= (1,2,3,4,5,6),height=10,show="headings")
table.place(x=0,y = 290,width=1350,height=700)

#entete
table.heading(1 , text="CODE VENTE")
table.heading(2 , text="CLIENT")
table.heading(3 , text="TELEPHONE")
table.heading(4 , text="PRODUITS")
table.heading(5 , text="PRIX")
table.heading(6 , text="QUANTITE")

#définir les dimention des colonnes
table.column(1,width=50)
table.column(2,width=150)
table.column(3,width=150)
table.column(4,width=100)
table.column(5,width=50)
table.column(6,width=50)


#afficher les informations de la table
# maBase = mysql .connect(host="localhost",user="root",password="",database="vente")
# meConnect = maBase.cursor()
# meConnect.execute("select * from tb_vente")
# for row in meConnect:
#     table.insert('',END, values=row)
# maBase.close()





#exécution
root.mainloop()

