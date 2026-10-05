# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



etudiants = []
choix = ""


def ajouter_etudiants():
    nom = input("Nom de l'etudiant : ").strip()
    while nom == "":
        print("Nom invalide")
        nom = input("Nom de l'etudiant : ").strip()
    age = int(input("Age de l'etudiant : "))
    while age <= 0:
        print("age invalide ! ")
        age = int(input("Age de l'etudiant : "))

    note = int(input("Note de l'etudiant : "))
    while note < 0 or note > 20:
        print("Note de l'etudiant invalide")
        note = int(input("Note de l'etudiant : "))
    etudiant ={
        "nom": nom,
        "age": age,
        "note": note
    }

    etudiants.append(etudiant)
    print("Etudiant ajouté !")

def afficher_etudiants():
    print("\nListe des étudiants :")

    for etudiant in etudiants:
        print("Nom :", etudiant["nom"])
        print("Age :", etudiant["age"])
        print("Note :", etudiant["note"])

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
                nouvel_age = int(input("Nouveau age :"))
                etudiant["age"] = nouvel_age

            elif choix == "note":
                nouvel_note = int(input("Nouvelle note :"))
                etudiant["note"] = nouvel_note
                while nouvel_note < 0 or nouvel_note > 20:
                    print("Note de l'etudiant invalide")
                    nouvel_note = int(input("Note de l'etudiant : "))


while choix != "6":
    print("\n--- MENU ---")
    print("1. Ajouter")
    print("2. Afficher")
    print("3.Rechercher")
    print("4.modifier")
    print("5. Supprimer")
    print("6. Quitter")

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
        print("Au revoir")
    else:
        print("Choix invalide")







#age = 0

# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

