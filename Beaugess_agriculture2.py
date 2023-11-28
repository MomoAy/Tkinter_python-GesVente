#Les librairies importés
import tkinter 
from tkinter import *
from tkinter import Tk,ttk
from cProfile import label
from subprocess import call
from tkinter import messagebox
#import mysql.connector





root = Tk()
root.title("Authentification") 
root.geometry("1260x800+450+120")
root.resizable(False,False)
root.configure(background="gray")

#Ajout du titre
title = Label(root, borderwidth=3, relief= SUNKEN, text="Enregistrement des Informations", font=("times new roman",45), bg="black",fg="white")
title.pack(side=TOP, fill=X)

#Main frame
mainFrame = Frame(root, bd=4, relief=GROOVE, bg="white")
mainFrame.pack(side=TOP, fill=BOTH, expand=True)

#Label
nom = Label(mainFrame, text="Nom", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)

prenom = Label(mainFrame, text="Prenom", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)

age = Label(mainFrame, text="Age", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)

datenais = Label(mainFrame, text="Date de Naissance", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)

sexe = Label(mainFrame, text="Sexe", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)

Profession = Label(mainFrame, text="Nom", font=("times new roman", 15,"bold"), bg="gray", fg="black")
nom.grid(row=0, column=0, sticky=W, padx=5,pady=2)











root.mainloop()