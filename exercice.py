#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import *
import json
import os
import pickle
# TODO: Définissez vos fonction ici
def comparerDeuxFichiers(chemin1: str, chemin2: str):
    with open(chemin1, encoding="utf-8") as fichier1, open(chemin2, encoding="utf-8") as fichier2:
        #dataF1 = fichier1.readlines()
        #dataF2 = fichier2.readlines()
        #for elemF1, elemF2 in zip(dataF1, dataF2):
            #if elemF1 != elemF2:
               # return f"{elemF1}isn't the same as:\n{elemF2}"
        #return "The lines are identical."
        for count, line1 in enumerate(fichier1):
            line2 = fichier2.readline()
            if line1 != line2:
                return f"{line1} !=\n{line2}"
        return "The lines are identical."


def recopieEtTriple(chemin1: str, chemin2: str):
    with open(chemin1, encoding="utf-8") as f1, open(chemin2, "w",  encoding="utf-8") as f2:
        #for line in f1:
            #line = line.replace(" ", " "*3)
            #f2.write(line)
        f2.write(f1.read().replace(" ", " "*3))

def associeNotes(chemin1: str, chemin2: str):
    #with open(chemin1, encoding="utf-8") as f1, open(chemin2, "w",  encoding="utf-8") as f2:
        #for grade in f1:
            #for letter, grades in PERCENTAGE_TO_LETTER.items():
                #if grades[0] <= int(grade.strip()) < grades[1]: ####if int(grade.strip()) in range(grades[0], grades[1]):   Pas recommande dans un if statement
                    #f2.write(grade.strip() + " " + letter + "\n")

    with open(chemin1, encoding="utf-8") as f1:### on fait ca pour close le fichier des quil nest plus utilise vu quon le read et lassigne a une variable et non le modifier
        lines = f1.readlines()
    with open(chemin2, "w",  encoding="utf-8") as f2:
        for line in lines:
            for letter, grades in PERCENTAGE_TO_LETTER.items():
                if grades[0] <= int(line.strip()) < grades[1]: ### int(grade) fonctionnerait parce que python est smart mais pas tous les langages le ferait
                    f2.write(line.strip() + " " + letter + "\n")
                    break

def deleteRecipe(dictionnary: dict):
    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in dictionnary:
        del dictionnary[name]
        print("La recette est supprimee!")
    else:
        print("la recette n'existe pas!")
    return dictionnary

def creerLivresRecettes(chemin1: str = None):
    if os.path.exists(chemin1):
        with open(chemin1) as path:
            recipes = json.load(path)
    else:
        recipes = dict()

    while True:
        choice = input("Choisissez une option: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher \n e) Quitter le programme\n").strip()

        if choice == "a":
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes = add_recipes(recipes)
        elif choice == "c":
            recipes = deleteRecipe(recipes)
        elif choice == "d":
            print(recipes)
        elif choice == "e":
            break
        else:
            print("L'option choisie n'est pas valide.")

    with open(chemin1, 'w') as outfile:
        json.dump(recipes, outfile, indent=4)













if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(comparerDeuxFichiers("exemple.txt", "ex2.txt"))
    recopieEtTriple("exemple.txt", "exempleTriple.txt")
    associeNotes("notes.txt", "notesLettres.txt")
    creerLivresRecettes("./recettes.txt")
    #print(exercice5("./exemple.txt"))
    #exercice6("./notes.txt", "./notes_skip.txt")

    pass
