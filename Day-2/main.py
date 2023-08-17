""""Day#2"""
import turtle


def demander_choix_dessin():
    reponse_str = input("""
    """)


def demander_taille_escalier():
    taille_escalier_int = 0
    while taille_escalier_int == 0:
        taille_escalier_str = input("Veuillez entrer la taille d'escalier : ")
        try:
            taille_escalier_int = int(taille_escalier_str)
        except ValueError:
            print("ERREUR : Vous devrez entrer un nombre pour la taille ")
    return taille_escalier_int


def demander_nombre_escalier():
    nombre_escalier_int = 0
    while nombre_escalier_int == 0:
        nombre_escalier_str = input("Veuillez entrer le nombre d'escalier : ")
        try:
            nombre_escalier_int = int(nombre_escalier_str)
        except ValueError:
            print("ERREUR : Vous devrez entrer un nombre  ")
    return nombre_escalier_int


def dessiner_escalier(taille, nombre):
    for i in range(0, nombre_escalier):
        t.forward(taille_escalier)
        t.left(90)
        t.forward(taille_escalier)
        t.right(90)
    t.forward(taille_escalier)


def dessiner_carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


taille_escalier = demander_taille_escalier()
nombre_escalier = demander_nombre_escalier()
t = turtle.Turtle()
dessiner_escalier(taille_escalier, nombre_escalier)
turtle.done()