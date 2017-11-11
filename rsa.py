"""
Fichier:	 python 3
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
"""
import rsa_fonct

# nomfichier = input('\nEntrez nom des fichier : \n')
nomfichier = "fichier"
rsa_fonct.gencle(nomfichier, taille=1024)
rsa_fonct.chiffre(nomfichier)
rsa_fonct.dechiffre(nomfichier)
