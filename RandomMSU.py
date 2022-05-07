from datetime import datetime
import os
import shutil
import random

now = datetime.now()
name = now.strftime("%d_%m_%Y_%H_%M")
os.mkdir(name)
racine=os.path.abspath(name)
#print(racine)
nbDir = 0
x=1

path='./'
resultat = os.scandir(path)

for entry in resultat :
	if entry.is_dir():
		nbDir = nbDir+1

f=open("./"+name+'\\'+name+'.msu',"w+")
f.close()		
nbDir=nbDir-1 #on retire le dossier créé
#print("Il y a "+str(nbDir)+" dossiers !")
liste=[1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,40,41,42,43,44,45,46,47,48,49,5,50,51,52,53,54,55,56,57,58,59,6,7,8,9]

while x<60: #on loop 59 fois pour les 59 fichiers du MSU
	rand = random.randint(1,nbDir) #on choisit dans quel dossier on va prendre le x-ième fime
	#print("Je choisis le dossier "+str(rand))
	#print("Je suis l'itération "+str(x))
	cpt = 1 #le compteur qu'on compare au rand
	resultat = os.scandir(path)
	for entry in resultat :
		if entry.is_dir() and entry.name!=str(name) :
			if cpt == rand : #dans ce if si on est dans le dossier dont on doit copier une chanson
				cpt = cpt+1
				#print (entry.name + " Itération "+ str(x)) #pour vérifier quel dossier est choisi à chaque itération
				recurs = os.scandir(path+entry.name)
				j=1
				for file in recurs :
					if j == x : #ici on a choisit le fichier qu'on veut copier
						print (file.name)
						shutil.copyfile(os.path.abspath(file),racine+'\\'+name+'-'+str(liste[x-1])+".pcm")
						j = j+1
					else :
						j = j+1


			else : 
				cpt = cpt+1 #dans ce else pour incrémenter le cpt
	x = x+1

	





















