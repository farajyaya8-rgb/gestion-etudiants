# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json

etudiants = []
choix = ""

def sauvegarder_etudiants():
    with open("etudiants.json", "w") as fichier:
        json.dump(etudiants, fichier, indent=4)
def charger_etudiants():
    global etudiants

    with open("etudiants.json", "r") as fichier:
        etudiants = json.load(fichier)
def ajouter_etudiants():
    nom = input("Nom de l'etudiant : ").strip()
    while nom == "":
        print("Nom invalide")
        nom = input("Nom de l'etudiant : ").strip()

    while True:
        try:
            age = int(input("Age de l'etudiant : "))
            if age<=0:
               print("age invalide ! ")
            else:
                break
        except ValueError:
            print("Tu dois entrer un nombre !")




    while True:
        try:
            note = int(input("Note de l'etudiant : "))
            if note < 0 or note > 20:
                print("Note invalide ! ")
            else:
                break
        except ValueError:
            print("Tu dois entrer un nombre !")


    etudiant ={
        "nom": nom,
        "age": age,
        "note": note
    }

    etudiants.append(etudiant)
    sauvegarder_etudiants()
    print("Etudiant ajouté !")

def afficher_etudiants():
    print("\nListe des étudiants :")

    for i, etudiant in enumerate(etudiants, start=1):
        print(f"\n{i}.{etudiant['nom']}")
        print(f" Age: {etudiant['age']}")
        print(f" Note: {etudiant['note']}")

def rechercher_etudiants():

     rechercher = input("Quel étudiant veux-tu rechercher ? ")
     trouve = False

     for etudiant in etudiants:
        if etudiant["nom"] == rechercher:
            print("Etudiant trouvé !")
            print("Nom :", etudiant["nom"])
            print("Age :", etudiant["age"])
            print("Note :", etudiant["note"])
            trouve = True
     if trouve == False:
        print("Etudiant introuvable !")

def etudiant_existe(nom) :
    if nom in etudiants:
        return True
    else:
        return False

def supprimer_etudiants():
    nom_etudiant = input("Quel etudiant veux-tu supprimer ? : ")
    trouve = False

    for etudiant in etudiants:
      if etudiant["nom"] == nom_etudiant:
        etudiants.remove(etudiant)
        sauvegarder_etudiants()
        print("Etudiant supprimé !")
        trouve = True
    if trouve == False:
        print("Etudiant introuvable !")

def modifier_etudiants():
    nom = input("Quel etudiant veux-tu modifier ? : ")
    for etudiant in etudiants:
        if etudiant["nom"] == nom:
            choix = input("Que veux-tu modifier ? (nom/age/note) :")
            if choix == "nom":
                nouveau_nom = input("Nouveau nom :")
                etudiant["nom"] = nouveau_nom
            elif choix == "age":
                while True:
                    try:
                        nouvel_age = int(input("Nouveau age :"))

                        if nouvel_age <= 0:
                            print("Age invalide ! ")
                        else:
                            etudiant["age"] = nouvel_age
                            print("Age modifier avec succès !")
                            break
                    except ValueError:
                        print("Tu dois entrer un age valide !")


            elif choix == "note":
                while True:
                    try:
                      nouvel_note = int(input("Nouvelle note :"))

                      if nouvel_note < 0 or nouvel_note > 20:
                         print("Note de l'etudiant invalide")
                      else:
                        etudiant["note"] = nouvel_note
                        print("Note modifier avec succès !")
                        break
                    except ValueError:
                        print("Tu dois entrer une note valide !")

            sauvegarder_etudiants()

def statistique():
    if len(etudiants) == 0:
        print("Erreur : La liste est vide !")
        return
    nombre = len(etudiants)
    print("nombre total d'etdiants : ", nombre)

    somme = 0
    for etudiant in etudiants:
        somme = somme + etudiant["note"]

    moyenne = somme / len(etudiants)
    print("moyenne des notes : ", moyenne)

    meilleure_etudiant = ""
    meilleure_note = 0
    for etudiant in etudiants:
       if etudiant["note"] > meilleure_note:
           meilleure_note = etudiant["note"]
           meilleure_etudiant = etudiant["nom"]

    print("meilleure note : ", meilleure_note)
    print("meilleure etudiant : ", meilleure_etudiant)
    admis = 0
    for etudiant in etudiants:
        if etudiant["note"] >= 10:
            admis = admis + 1
            print("Nombre d'etudiants admis : ", admis)

    ajournes = 0
    for etudiant in etudiants:
        if etudiant["note"] < 10:
            ajournes = ajournes + 1
            print("Nombre d'etudiants ajourne : ", ajournes)

charger_etudiants()

while choix != "7":
    print("\n--- MENU ---")
    print("1. Ajouter")
    print("2. Afficher")
    print("3.Rechercher")
    print("4.modifier")
    print("5. Supprimer")
    print("6. statistique")
    print("7. Quitter")

    choix = input("Choisis une option : ")
    if choix == "1":
        ajouter_etudiants()
        print(etudiants)

    elif choix == "2":
        afficher_etudiants()


    elif choix == "3":
       rechercher_etudiants()

    elif choix == "4":
        modifier_etudiants()

    elif choix == "5":
        supprimer_etudiants()

    elif choix == "6":
        statistique()

    elif choix == "7":
        print("Au revoir")
    else:
        print("Choix invalide")







#age = 0

# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

