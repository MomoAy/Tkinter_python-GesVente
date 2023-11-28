from tkinter import * 
from tkinter  import messagebox,ttk
import random
from time import strftime
from subprocess import call


class Beaugess:
    def __init__(self, root):
        self.root = root
        self.root.title('BEAUGESS')
        self.root.geometry("1920x1040+0+0")

        title = Label(self.root, text="Beaugess Gestion", font=("times new roman",45), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heu = strftime("%H:%M:%S")
            lbheure.config(text=heu)
            lbheure.after(1000,heure)


        lbheure = Label(self.root, text="HH:MM:SS", font=("times new roman",15,"bold"), bg="cyan", fg="black",)
        lbheure.place(x=0, y=15, width=120, height=45)

        heure()
        #nos variables
        self.c_nom = StringVar()
        self.c_phone = StringVar()

        self.n_facture = StringVar()
        z = random.randint(1000,999999)
        self.n_facture.set(z)

        self.c_prenom = StringVar()
        self.rech_fact = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalbrute = StringVar()
        self.taxe = StringVar()
        self.taxe_temp = IntVar()
        self.totalnet = StringVar()

        #Liste de Categories
        self.list_categorie = ["Selection",'ALIMENTAIRES','VESTIMENTAIRES','ELECTRONIQUE']
        
        self.alim = ['Selection','Riz AK 50Kg','Riz AICHA 5Kg','Riz THAÏ 50Kg','HUILE NIOTO 5l','HUILE AICHA 10l','Lait Bridel 1l','Fromage 500mg','33 EXPORTS']
        self.price_riz_ak = 5000
        self.price_riz_aicha = 7500
        self.price_riz_thaï = 9500
        self.price_huile_nioto = 12500
        self.price_huile_aicha = 15000
        self.price_lait_bridel = 18000
        self.price_fromage = 25000
        self.price_33export = 25000

        self.vest = ['Selection',"T-shirt polo","T-shirt Gucci","T-shirt NIKE","Jogging Nike", "Pantalon kaki"]
        self.price_tpolo = 3000
        self.price_tgucci = 5000
        self.price_tnike = 5000
        self.price_jogging_nike = 25000
        self.price_pantalon_kaki = 2000

        self.elec = ['selection',"TV LG","Hp probook450","Home TV","Machine à laver"]
        self.price_tvlg = 3000000
        self.price_home_tv = 5000000
        self.price_probook450 = 500000
        self.price_machine_laver = 300000


        Main_frame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        Main_frame.place(x=10, y=100, width=1890, height=920)

        #client
        client_frame = LabelFrame(Main_frame, text="Client", font=("times new roman", 15), bg="white")
        client_frame.place(x=10, y=5, width=450, height=150)

        self.lbcontact = Label(client_frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        self.lbcontact.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbnom = Label(client_frame, text="Nom Client", font=("times new roman", 15, "bold"), bg="white")
        self.lbnom.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbprenom = Label(client_frame, text="Prenom Client", font=("times new roman", 15, "bold"), bg="white")
        self.lbprenom.grid(row=2, column=0, sticky=W, padx=5, pady=2)



        self.txtcontact = ttk.Entry(client_frame, textvariable=self.c_phone, font=("times new roman", 15))
        self.txtcontact.grid(row=0, column=1, sticky=W,padx=5, pady=2)

        self.txtnom = ttk.Entry(client_frame, textvariable=self.c_nom, font=("times new roman", 15))
        self.txtnom.grid(row=1, column=1, sticky=W,padx=5, pady=2)

        self.txtprenom = ttk.Entry(client_frame, textvariable=self.c_prenom, font=("times new roman", 15))
        self.txtprenom.grid(row=2, column=1, sticky=W,padx=5, pady=2)

        #produits
        produit_frame = LabelFrame(Main_frame, text="Produits", font=("times new roman",15,), bg="white")
        produit_frame.place(x=500, y=5, width=700,height=150)

        self.lbcategorie = Label(produit_frame, text="Selectionner une Catégorie", font=("times new roman",15,"bold"), bg="white")
        self.lbcategorie.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbnomproduit = Label(produit_frame, text="Nom du produit", font=("times new roman",15,"bold"), bg="white")
        self.lbnomproduit.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbprix = Label(produit_frame, text="Prix", font=("times new roman",15,"bold"), bg="white")
        self.lbprix.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.lbqtte = Label(produit_frame, text="Quantité", font=("times new roman",15,"bold"), bg="white")
        self.lbqtte.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.lbtaxe = Label(produit_frame, text="taxe", font=("times new roman",15,"bold"), bg="white")
        self.lbtaxe.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.txt_categorie = ttk.Combobox(produit_frame, font=("times new roman", 10),values=self.list_categorie, width=24, state="readonly")
        self.txt_categorie.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_categorie.current(0)
        self.txt_categorie.bind("<<ComboboxSelected>>", self.fonctionproduit)

        self.txt_nomproduit = ttk.Combobox(produit_frame, font=("times new roman", 10),textvariable=self.produit, width=24, state="readonly")
        self.txt_nomproduit.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_nomproduit.bind("<<ComboboxSelected>>", self.fonctionprix)


        self.txt_prix = ttk.Combobox(produit_frame, font=("times new roman", 10),textvariable=self.prix, width=24, state="readonly")
        self.txt_prix.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        self.txt_qtte = ttk.Entry(produit_frame, font=("times new roman", 10),textvariable=self.qte, width=24)
        self.txt_qtte.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        self.txt_taxe = ttk.Entry(produit_frame, font=("times new roman", 10), textvariable=self.taxe_temp, width=24)
        self.txt_taxe.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #recherche
        rech_frame = Frame(Main_frame, bd=2, bg="white")
        rech_frame.place(x=1250, y=10, width=600, height=70)

        self.l_recherche = Label(rech_frame, text="N Facture", font=("times new roman", 20, "bold"), bg='white')
        self.l_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_recherche = ttk.Entry(rech_frame, textvariable=self.rech_fact, font=("times new roman", 20), width=15)
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_recherche = Button(rech_frame, text="Rechercher", height=2, font=("times new  Roman", 12, "bold"), bg="yellow", width=11, cursor="hand2")
        self.btn_recherche.grid(row=0, column=2)

        #espace facture
        fact_label = LabelFrame(Main_frame, text="Facture", font=("times new Roman",15,"bold"), bg="white")
        fact_label.place(x=1220, y=80, width=650, height=650)


        scroll_y = Scrollbar(fact_label, orient=VERTICAL)
        self.textarea = Text(fact_label, font=("times new Roman",15, "bold"), bg="white" , fg="blue")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        #footer
        enbas_frame = LabelFrame(Main_frame, text="Boutton", font=("times new Roman",15), bg="white")
        enbas_frame.place(x=0, y=730, width=1880,height=180)

        self.l_totalbrute = Label(enbas_frame, text="Total Brute", font=("times new Roman",23,"bold"), bg="white")
        self.l_totalbrute.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.l_taxe = Label(enbas_frame, text="Taxe", font=("times new Roman",23,"bold"), bg="white")
        self.l_taxe.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.l_totalnet = Label(enbas_frame, text="Total net", font=("times new Roman",23,"bold"), bg="white")
        self.l_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_totalbrute = ttk.Entry(enbas_frame, textvariable=self.totalbrute, font=('times new Roman',23), width=15,state="readonly")
        self.txt_totalbrute.grid(row=0, column=1,sticky=W,padx=5,pady=2)

        self.txt_taxe = ttk.Entry(enbas_frame, textvariable=self.taxe, font=('times new Roman',23), width=15,state="readonly")
        self.txt_taxe.grid(row=1, column=1,sticky=W,padx=5,pady=2)

        self.txt_totalnet = ttk.Entry(enbas_frame, textvariable=self.totalnet, font=('times new Roman',23), width=15,state="readonly")
        self.txt_totalnet.grid(row=2, column=1,sticky=W,padx=5,pady=2)

        #bouton
        btn_frame = Frame(enbas_frame, bd=2, bg="white")
        btn_frame.place(x=450, y=0)

        
        self.ajoutPanier = Button(btn_frame, text="Ajouter",command=self.ajouter, height=2, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.ajoutPanier.grid(row=0, column=0)

        self.sauvegarde = Button(btn_frame, text="Sauvegarder la Facture", height=2,command=self.sauvegarder, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.sauvegarde.grid(row=0, column=2)

        self.generer = Button(btn_frame, text="Générer",command=self.generefact, height=2, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.generer.grid(row=0, column=1)
        
        self.imprime = Button(btn_frame, text="Imprimer", height=2, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.imprime.grid(row=0, column=3)

        self.reni = Button(btn_frame, text="Réniialiser", height=2, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.reni.grid(row=0, column=4)

        self.quit = Button(btn_frame, text="Quitter", command=self.Retour, height=2, font=("times new Roman", 19, "bold"), bg="blue", width=15, cursor="hand2")
        self.quit.grid(row=0, column=5)
        self.Bienvenue()
        self.l=[]

    ##Fontions
    def Bienvenue(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END,"\t\tBIENVENUE CHEZ BEAUGESS")
        self.textarea.insert(END,f"\n\nNuméro de Facture : {self.n_facture.get()}")
        self.textarea.insert(END,f"\n\nNom du Client : {self.c_nom.get()}")
        self.textarea.insert(END,f"\n\nPrenom du Client : {self.c_prenom.get()}")
        self.textarea.insert(END,f"\n\nNuméro du Client : {self.c_phone.get()}")

        self.textarea.insert(END,f"\n**************************************************************")

        self.textarea.insert(END,f"\nProduits\t\tQTE\t\tPrix")
        
        self.textarea.insert(END,f"\n**************************************************************")

    def Retour(self):
        self.root.destroy()
        call(["python", "Python/Acceuil.py"])

    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n
        self.l.append(self.m)
        if self.produit.get() =="":
            messagebox.showerror("Erreur","selectioner un produit")
        else:
                self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{self.m}")
                self.totalbrute.set(str("Rs.%.2f"%(sum(self.l))))
                self.taxe.set(str("Rs.%.2f"%((((sum(self.l)))*self.taxe_temp.get())/100)))
                self.totalnet.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l)))*self.taxe_temp.get())/100)))))

    def generefact(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur","Ajouter d'abord un produit")
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            #self.Bienvenue()
            text = self.textarea.insert(END, text)
        #self.textarea.insert(END,f"\n**************************************************************")
        self.textarea.insert(END,f"\nTotal Brute : \t\t\t{self.totalbrute.get()}")
        self.textarea.insert(END,f"\nTaxe : \t\t\t{self.taxe.get()}")
        self.textarea.insert(END,f"\nTotal net : \t\t\t{self.totalnet.get()}")

    def sauvegarder(self):
        op = messagebox.askyesno("Sauvegarder","Voulez vous sauvegarder la facture ?")
        if op == "True":
            self.donneFacture = self.textarea.get(1.0,END)
            f1 = open("C:/Users/AYEVA/Desktop/Facture"+str(self.n_facture.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("sauvegarder", f"la facture numéro{self.n_facture.get()}a été enregistré avec succes")
            f1.close()
    def fonctionproduit(self, even=""):
        if self.txt_categorie.get() =="ALIMENTAIRES":
            self.txt_nomproduit.config(values = self.alim)
            self.txt_nomproduit.current(0)

        if self.txt_categorie.get() =="VESTIMENTAIRES":
            self.txt_nomproduit.config(values = self.vest)
            self.txt_nomproduit.current(0)

        if self.txt_categorie.get() =="ELECTRONIQUE":
            self.txt_nomproduit.config(values = self.elec)
            self.txt_nomproduit.current(0)

    def fonctionprix(self, even=""):
        if self.txt_nomproduit.get()=="Riz AK 50Kg":
            self.txt_prix.config(values = self.price_riz_ak)
            self.txt_prix.current(0)
            self.qte.set(1)
            
        if self.txt_nomproduit.get()=="Riz AICHA 5Kg":
            self.txt_prix.config(values = self.price_riz_aicha)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="Riz THAÏ 50Kg":
            self.txt_prix.config(values = self.price_riz_thaï)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="HUILE NIOTO 5l":
            self.txt_prix.config(values = self.price_huile_nioto)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="T-shirt polo":
            self.txt_prix.config(values = self.price_tpolo)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="T-shirt Gucci":
            self.txt_prix.config(values = self.price_tgucci)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="T-shirt NIKE":
            self.txt_prix.config(values = self.price_tnike)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="TV LG":
            self.txt_prix.config(values = self.price_tvlg)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="Home TV":
            self.txt_prix.config(values = self.price_home_tv)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="Machine à laver":
            self.txt_prix.config(values = self.price_machine_laver)
            self.txt_prix.current(0)
            self.qte.set(1)

        













if __name__ == "__main__":
    root = Tk()
    obj = Beaugess(root)
    root.mainloop()