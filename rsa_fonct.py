"""
Fichier:	 python 3
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
"""
import random
from Crypto.Util import number


# borne-inf = 10**9
# borne-sup = 10**26
# nbr-longueur = 300


def gencle(nom="fichier", taille=10):
    """
    Genere des cle.

    génère une paire de clé pour des blocs de taille [t] et les sauve dans
    les fichiers [nom].pub et [nom].priv

    TODO implementer la taille de la cle dans les fichier !!

    n est le produit de deux nombre premiers p et q
    a est l'inverse de b modulo le produit (p-1)(q-1).
    n, b, est la partie publique de la clé
    p, q, a est la partie privée de la clé
    """
    # Géneration de nombre premier
    p_quintuplet = number.getPrime(taille)
    q_quintuplet = number.getPrime(taille)

    phi_n = (p_quintuplet - 1) * (q_quintuplet - 1)

    a_quintuplet = random.randint(10**taille - 1, 10**taille + 1)

    n_quintuplet = p_quintuplet * q_quintuplet

    b_quintuplet = number.inverse(a_quintuplet, phi_n)
    print("n: " + str(n_quintuplet) + " b: " + str(b_quintuplet))
    print("p: " + str(p_quintuplet) +
          " q: " + str(q_quintuplet) +
          " a: " + str(a_quintuplet))

    with open(nom + '.pub', 'w') as file:
        file.write("n:\n" + str(n_quintuplet) + "\n" +
                   "b:\n" + str(b_quintuplet) + "\n" +
                   "t:\n" + str(taille))

    with open(nom + '.priv', 'w') as file:
        file.write("p:\n" + str(p_quintuplet) + "\n" +
                   "q:\n" + str(q_quintuplet) + "\n" +
                   "a:\n" + str(a_quintuplet) + "\n" +
                   "t:\n" + str(taille))


def pgcd(a, b):
    """
    Calcule le pgcd de a par b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def chiffre(nom="fichier_test"):
    """
    Chiffre le message sur l'entrée standard.

    chiffre le message sur l'entrée standard pour le destinataire de
    clé [nom].pub et sort le message chiffré sur la sortie standard
    """
    mot = input('\nEntrez le mot ou la phrase à chiffrer : ')
    taille_du_mot = len(mot)
    i = 0
    txt_chiffre = ""
    with open('fichier.pub', 'r') as fichierread:
        lines = fichierread.readlines()
        n_quintuplet = lines[1]
        b_quintuplet = lines[3]
        taille_cle = lines[5]
    print("n: " + str(n_quintuplet) + " b: " + str(b_quintuplet))
    while i < taille_du_mot:
        j = 0
        while j < taille_cle:
            ascii_mot = ord(mot[(i * taille_cle) + j])
            j = j + 1

        lettre_crypt = pow(ascii_mot, int(b_quintuplet)) % int(n_quintuplet)

        # Si le code ASCII est supérieur à n
        if ascii_mot > int(n_quintuplet):
            print("Les nombres p et q sont trop petits veuillez recommencer.")

        # if lettre_crypt > phi_n:
        #     print("Erreur de calcul")

        print("\n Block " + str(i) + " : " + str(lettre_crypt))
        txt_chiffre += str(lettre_crypt)
        i = i + 1
    print(txt_chiffre)

def dechiffre(nom):
    """
    déchiffre le message sur l'entrée standard pour le
    récipendiaire [nom] et sort le message clair sur la sortie standard.
    On note que le programme va rechercher la clé privée dans le
    fichier [nom].priv de l'utilisateur.
    """


def signe(nom):
    """
    signe le message sur l'entrée standard par l'émetteur [nom]
    et sort la signature sur la sortie standard. On note que le
    programme va rechercher la clé dans le fichier [nom].priv de l'utilisateur
    """


def verifie(nom, fichier_signature):
    """
    vérifie que le fichier-signature est bien la signature du
    message donné sur l'entrée standard pour l'émetteur [nom].
     Le programme accèdera au fichier [nom].pub seulement.
    """
