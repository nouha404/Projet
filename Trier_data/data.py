from pathlib import Path

CHEMIN = Path(__file__).resolve()
prenom_txt = CHEMIN.parent / 'prenom.txt'
prenom_final = CHEMIN.parent / 'prenom_final.txt'

#ouvrir prenom_txt et transformer en array
array_prenom = prenom_txt.read_text().split(', ')
array_prenom.sort()
del array_prenom[0] 

#recuperer les prenom dans un nouveau liste
new_array = []
for i in array_prenom:
    new_array.append(i)
new_array.sort()

#netoyage des prenoms
clean_prenom = ', '.join(new_array)
cleans = clean_prenom.replace('.', ',')

#nouveau tableau avec les prenom
final_array = []
final_array.append(cleans)

for i in final_array:
    a = i.split(', ')
    cleans = '\n'.join(a)

#remettre en array
last_array = cleans.split()
end_array = []

#compter le nombre de prenom
som = 0
for i in last_array:
    som += 1
    number_of_prenom = f'{som}. {i}'
    end_array.append(number_of_prenom)

#recuprer les donner de end_array
data_end_array = '\n'.join(end_array)

# Mettre les nouvelles donnees dans le document final 
if not Path.exists(prenom_final):
    prenom_final.touch()
prenom_final.write_text(data_end_array)
#Je comprends pas pk il mets Jade en premiere position or j'ai trier la liste
 