from grid import SudokuGrid
import sys

if __name__=="__main__":
    jouer = True
    tour=0

#+ Ce script devra accepter un argument de la ligne de commande donnant le nom du fichier et le numéro de ligne
#à partir desquels initialiser la grille.
#+ Si cet argument n'est pas donné, le script demandera à l'utilisateur de saisir manuellement une grille.
#+ Il alternera ensuite les étapes suivantes:
#	1. Affichage de l'état actuel de la grille;
#	2. Saisie utilisateur de la position et de la valeur à écrire;
#	3. Vérification de la validité de la saisie;
#	4. Inscription dans la grille de la valeur donnée à la position donnée si valide.

    if (sys.argv ==3):
        fichier= sys.argv[1]
        ligne= sys.argv[2]
        sudoku = SudokuGrid.from_file(fichier,ligne)

    else:
        sudoku= SudokuGrid.from_stdin()

    while jouer:
        tour+=1
        if tour ==1:
            print("Le jeu va commencer, voici la grille actuelle : \n")
        else :
            print(" Voici la nouvelle grille")
        print(sudoku)
        a=int(input("Choix de la ligne :"))
        b=int(input("Choix de la colonne :"))
        c=int(input("Choix de la valeur :"))

        #Gestion des fautes
        verif= False
        while verif==False:
            if a>10 and b>10 :
                print("La grille a des colonnes et des lignes numérotés de 0 à 9, il faut recommencer")
                a = input("Choix de la ligne :")
                b = input("Choix de la colonne :")
            if (a,b) not in sudoku.get_empty_pos():
                print("La case est occupée trouvez en une autre")
                a = input("Choix de la ligne :")
                b = input("Choix de la colonne :")
            if a<10 and b<10 and (a,b) in sudoku.get_empty_pos():
                verif=True

        try :
            sudoku.write(int(a),int(b),int(c))
        except :
            print("La valeur doit être un chiffre de 0 à 9 ! et pas autre chose !!")
            c = input("Choix de la valeur :")
            sudoku.write(int(a),int(b),int(c))

        if len(sudoku.get_empty_pos())==0:
            jouer=False






