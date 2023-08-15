""""DAY#1"""


def demander_nom():  # demander nom
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom ? ")
    return nom_str


def demander_age(nom_personne):  # demander âge
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne+" quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR : Vous devrez rentrer un nombre pour l'âge ")
    return age_int


def demander_taille(nom_personne):
    taille_float = 0
    while taille_float == 0:
        taille_str = input(nom_personne + " quel est votre taille ? ")
        try:
            taille_float = float(taille_str)
        except ValueError:
            print("ERREUR : Vous devrez rentrer un nombre pour la taille ")
        else:
            if taille_float > 2.5:
                print("Veuillez rentrer une taille réel en mètre")
                taille_float = 0
    return taille_float


def afficher_resultats(nom_personne, age_personne, taille_personne):
    print()
    print("Vous vous appelez " + nom_personne + " vous avez " + str(age_personne) + " ans")
    print("L'an prochain vous aurez " + str(age_personne + 1) + " ans")

    if age_personne == 17:
        print("Vous êtes presque majeur")
    elif age_personne == 18:
        print("Tout juste majeur : Félicitation")
    elif age_personne == 1 or age_personne == 2:
        print("Vous êtes bébé")
    elif 12 <= age_personne < 18:
        print("Vous êtes adolescent")
    elif age_personne > 60:
        print("Vous êtes sénior")
    elif age_personne < 10:
        print("Vous êtes enfant")
    elif age_personne > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher taille
    print("Votre taille : "+str(taille_personne)+" m")
# ------------------------------------------------------------------------------------------------


nom = demander_nom()
age = demander_age(nom)
taille = demander_taille(nom)
afficher_resultats(nom, age, taille)
