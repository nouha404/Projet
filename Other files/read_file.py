
chemin = r'C:\Users\Mugiwara no nouha\Desktop\learn\lire_un_fichier\document\document.txt'

with open(chemin, 'r') as file:
    contenue = file.read()
                #file.readlines           Pour recuperer le contenue du fichier a l'interieur d'une liste
                #file..read().splitline   Pour recuperer le contenue du fichier a l'interieur d'une liste sans les \n
    # contenue = repr(file.read())        Pour enlever les retours a la ligne
    print(contenue)
    
    
# #Pour ecrire a l'interieur du fichier
# with open(chemin, 'w') as file:
#     file.write("\nC'est reel")
#     print(contenue)
# # with open(chemin, 'a') as file: a comme append pour ne pas ecraser ce qui etait a l'interieur 
 
