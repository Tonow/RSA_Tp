"""
Fichier:	 python 3
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
"""
import random
import sys
import hashlib
import trait_entier
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
    print("Generation de la cle")
    # Géneration de nombre premier
    p_quintuplet = number.getStrongPrime(taille)
    q_quintuplet = number.getStrongPrime(taille)

    phi_n = (p_quintuplet - 1) * (q_quintuplet - 1)

    a_quintuplet = number.getStrongPrime(taille)

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


def chiffre(nom="fichier_test"):
    """
    Chiffre le message sur l'entrée standard.

    chiffre le message sur l'entrée standard pour le destinataire de
    clé [nom].pub et sort le message chiffré sur la sortie standard
    """
    mot = input('\nEntrez le mot ou la phrase à chiffrer : \n')
    print("\n\n")
    #mot = "coucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmerscoucousouventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmers"
    #mot = "coucou"
    taille_du_mot = len(mot)

    i = 0
    txt_chiffre = ""
    with open(nom + '.pub', 'r') as fichierread:
        lines = fichierread.readlines()
        n_quintuplet = int(lines[1])
        b_quintuplet = int(lines[3])
        taille_cle = int(lines[5])
    # print("n: " + str(n_quintuplet) + " b: " + str(b_quintuplet))
    # print("taille_du_mot : " + str(taille_du_mot))
    while i * taille_cle < taille_du_mot:
        j = 0
        ascii_mot = b""
        while j < taille_cle:
            # print("posi : " + str(((i * taille_cle) + j))) # debug
            ascii_lettre = (mot[(i * taille_cle) + j]).encode()
            # print(str(type(ascii_lettre)) + " ascii_lettre : " +
            #       str(ascii_lettre) +
            #       str(int.from_bytes(ascii_lettre, sys.byteorder)))
            ascii_mot += ascii_lettre
            j = j + 1
            if ((i * taille_cle) + j) == taille_du_mot:
                break

        print(str(type(ascii_mot)) + " ascii_mot = " + str(ascii_mot) +
              str(int.from_bytes(ascii_mot, sys.byteorder)))
        lettre_crypt = 0
        lettre_crypt = trait_entier.modexp(int.from_bytes(ascii_mot, sys.byteorder),
                                           b_quintuplet, n_quintuplet)
        print(str(type(lettre_crypt)) + " lettre crypt = " + str(lettre_crypt))

        # Si le code ASCII est supérieur à n
        # if int.from_bytes(ascii_mot, sys.byteorder) > n_quintuplet:
        #     print("Les nombres p et q sont trop petits veuillez recommencer." +
        #           "\nascii_mot :\n" +
        #           str(int.from_bytes(ascii_mot, sys.byteorder)) +
        #           "\nn_quintuplet :\n" + str(n_quintuplet)
        #          )
        #     sys.exit(0)

        if lettre_crypt > n_quintuplet:
            print("Erreur de calcul")
            break
            sys.exit(0)

        print("\n \n Block " + str(i) + " : " + str(lettre_crypt))
        txt_chiffre += str(lettre_crypt) + "\n"
        i = i + 1
    print("\n \n text chiffre : " + txt_chiffre)
    with open(nom + '.chiffre', 'w') as file:
        file.write(txt_chiffre)

def dechiffre(nom = "kla"):
    """
    déchiffre le message sur l'entrée standard pour le
    récipendiaire [nom] et sort le message clair sur la sortie standard.
    On note que le programme va rechercher la clé privée dans le
    fichier [nom].priv de l'utilisateur.
    """
    print("Dechiffre")
    with open(nom + '.pub', 'r') as fichierread:
        lines = fichierread.readlines()
        n_quintuplet = int(lines[1])
    with open(nom + '.priv', 'r') as fichierread:
        lines = fichierread.readlines()
        a_quintuplet = int(lines[5])

    with open(nom + '.chiffre', 'r') as fichierread:
        for line in fichierread:
            print("int line : " + str(line))
            # print("a_quintuplet : " + str(a_quintuplet) + " n_quintuplet : " + str(n_quintuplet))
            lettre_decrypt = trait_entier.modexp(int(line), a_quintuplet, n_quintuplet)
            print(str(type(lettre_decrypt)) + "lettre decrypt = " + str(lettre_decrypt))
            print(type(lettre_decrypt))
            bytes_crypt = trait_entier.long_to_bytes(lettre_decrypt)
            print(bytes_crypt)
            str_decript = bytes_crypt.decode("utf-8", "ignore")
            decripte = str_decript[::-1]
            print(str(type(decripte)) + str(decripte))

def signe(nom):
    """
    signe le message sur l'entrée standard par l'émetteur [nom]
    et sort la signature sur la sortie standard. On note que le
    programme va rechercher la clé dans le fichier [nom].priv de l'utilisateur
    """
    with open(nom + '.priv', 'r') as fichierread:
        lines = fichierread.readlines()
        a_quintuplet = int(lines[5])
    signature = hashlib.md5(nom).hexdigest()
    lettre_decrypt = trait_entier.modexp(int(signature), a_quintuplet, n_quintuplet)
    print(signature)
    with open(nom + '.signature', 'w') as file:
        file.write(signature)


def verifie(nom, fichier_signature):
    """
    vérifie que le fichier-signature est bien la signature du
    message donné sur l'entrée standard pour l'émetteur [nom].
     Le programme accèdera au fichier [nom].pub seulement.
    """
