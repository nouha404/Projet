
chaineZ = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaineZ.split(", ")
chaine_liste.sort() #ou sort()
chaine_en_ordre = ", ".join(chaine_liste)

print(chaine_en_ordre)
