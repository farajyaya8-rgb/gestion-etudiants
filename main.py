# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    #On demande le nom et l'age de la personne______
#if __name__ == '__main__':

  #  nom = input('quel est votre nom ? ')
   # while not nom:
       # print("veuiller saisir un nom ")
       # nom = input('quel est votre nom ? ')

#age = input('quel est votre age ? ')
#while not age:
    #print("veuiller saisir un age ")
   # age = input('quel est votre age ? ')

#ville = input('quel est votre ville ? ')
#while not ville:
   # print("veuiller saisir une ville ")
   # ville = input('quel est votre ville ? ')


#filière = input('quel est votre filière ? ')
#while not filière :
   # print("veuiller saisir une filière ")
    #filière = input('quel est votre filière  ? ')

#objectif_professionnel  = input('quel est votre objectif professionnel ? ')
#while not objectif_professionnel:
   # print("veuiller saisir un objectif_professionnel ")
    #objectif_professionnel = input('quel est votre objectif professionnel ? ')

#print("bonjour " + nom + ", tu habites à " + ville + ".")
#print("Tu étudies " + filière + ".")
#print("ton objectif est de devenir " + objectif_professionnel + ".")

etudiants = []
choix = ""


def ajouter_etudiants():
    nom = input("Nom de l'etudiant : ")
    age = int(input("Age de l'etudiant : "))
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


while choix != "5":
    print("\n--- MENU ---")
    print("1. Ajouter")
    print("2. Afficher")
    print("3.Rechercher")
    print("4. Supprimer")
    print("5. Quitter")

    choix = input("Choisis une option : ")
    if choix == "1":
        ajouter_etudiants()
        ajouter_etudiants()
        print(etudiants)

    elif choix == "2":
        afficher_etudiants()


    elif choix == "3":
       rechercher_etudiants()

    elif choix == "4":
        supprimer_etudiants()

    elif choix == "5":
        print("tu as choisi Quitter")
    else:
        print("Choix invalide")







#age = 0
#while age == 0:
    #age_str = input("quel est votre age ? ")
    #nom = "toto"
    #age = "23"
   # try:
      # age = int(age_str)
    #except:
       # print("ERREUR: vous devez rentrer un nombre pour l'age")

   # else:
     # print("vous vous appelez " + nom + ", vous avez " + str(age) + "ans")  # Press F9 to toggle the breakpoint.
      #  print("l'an prochain vous aurez " + str(age+1) + "ans")


   # print(type(nom))
    #print(type(age))
   # 1.5-> float
    #vrai ou faux -> boolean

 # boucle while : "tant que" ...

#n = 0
#print("debut de la boucle")
#while n < 10:
  #  print("valeur de n: " + str(n))
  #  n = n + 1

#print("fin de la boucle")

#mot_de_passe = ""
#while not mot_de_passe == "toto" :
  #  mot_de_passe = input("Quel est votre mot de passe ? ")

#print("mot_de_passe correct, vous avez accès au compte")

# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

