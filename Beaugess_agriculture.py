#les librairies
import tkinter 
from tkinter import *
from tkinter import Tk,ttk
from cProfile import label
from subprocess import call
from tkinter import messagebox
#import mysql.connector


def Seconnecter():
    nom = txtuser.get()
    mdp = txtpassword.get()
    if(nom == "" and mdp == ""):
        messagebox.showerror("", "Veuillez remplir les champs")
        txtpassword.delete("0", "end")
        txtuser.delete("0", "end")
    elif(nom == "admin" and mdp == "admin"):
        messagebox.showinfo("", "Bienvenue")
        txtuser.delete("0", "end")
        txtpassword.delete("0", "end")
        root.destroy()
        call(["python","Beaugess_agriculture2.py"])
    else:
        messagebox.showwarning("", "Erreur de Connexion")
        txtpassword.delete("0", "end")
        txtuser.delete("0", "end")




root = Tk()
root.title("Authentification") 
root.geometry("1260x800+450+120")
root.resizable(False,False)
root.configure(background="black")

#Ajout du titre
title = Label(root, borderwidth=3, relief= SUNKEN, text="Authentification", font=("times new roman",45), bg="gray",fg="white")
title.pack(side=TOP, fill=X)

#creation d'un Mainframe
Mainframe = Frame(root, bd=2, relief=GROOVE, bg="gray")
Mainframe.place(x=230,y=230,width=800,height=400)

#Label
nomuser = Label(Mainframe, text="Nom d'utilisateur", font=("Times new roman",25,"bold"), bg="gray", fg="white")
nomuser.grid(row=0, column=0, sticky=W, padx=90, pady=90)

password = Label(Mainframe, text="Mot de passe", font=("Times new roman",25,"bold"), bg="gray", fg="white")
password.grid(row=1, column=0, sticky=W, padx=90, pady=0)

#input
txtuser = Entry(Mainframe, bd=4, font=("Times new roman",20))
txtuser.grid(row=0,column=1, sticky=W, padx=50, pady=0)

txtpassword = Entry(Mainframe,show="*", bd=4, font=("Times new roman",20))
txtpassword.grid(row=1,column=1, sticky=W, padx=50, pady=0)

#Connection
btnconnect = Button(Mainframe, text="Connexion", font=("Times new roman",15), bg="gray", fg="white", cursor="hand2", command=Seconnecter)
btnconnect.place(x=300, y=300,width=200,height=50)








root.mainloop()