# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

ew = 609.5 #Poids à vide (kg)

# les bras de levier :
blew = 0.34
blAV = 0.36
blAR = 1.19
blFuel = 1.12
blSupp = 1.61
blBagages = 1.9

# les limites :
maxCatN = 1000
maxCatU = 910
limFuel = 110
limSupp = 50
limBagages = 40

rhoFuel = 0.72  #densité du fuel (kg/L)

# les inputs :
kgAV = float(input("poids passagers AV (kg) : "))
kgAR = float(input("poids passagers AR (kg) : "))
LFuel = float(input("Litres de fuel dans le principal (L) (max:110 L): "))
if LFuel > limFuel :
    while LFuel > limFuel :
        LFuel = float(input("c'est trop, choisir une valeur valable : "))
kgFuel=LFuel*rhoFuel
LSupp = float(input("Litres de fuel dans le supp (L) (max:50 L) : "))
if LSupp > limSupp :
    while LSupp > limSupp :
        LSupp = float(input("c'est trop , choisir une valeur valable : "))
kgSupp=LSupp*rhoFuel
kgBagages = float(input("kg de bagages (kg) (max:40 Kg): "))
if kgBagages > limBagages :
    while kgBagages > limBagages :
        kgBagages = float(input("c'est trop , choisir une valeur valable : "))

# les calculs de moment (masse * bras de levier = moment) :
mew=ew*blew
mAV=kgAV*blAV
mAR=kgAR*blAR
mFuel=kgFuel*blFuel
mSupp=kgSupp*blSupp
mBagages=kgBagages*blBagages

Totalkg = ew+kgAV+kgAR+kgFuel+kgSupp+kgBagages
Totalm = mew+mAV+mAR+mFuel+mSupp+mBagages
zfw=ew+kgAV+kgAR+kgBagages
zfm=mew+mAV+mAR+mBagages

BLfinal = Totalm/Totalkg

#Checking
if Totalkg>maxCatN:
    print("La masse totale est de",Totalkg,"kg, c'est supérieur à la masse max :",maxCatN,"kg")
elif Totalkg>maxCatU:
    print("La masse totale est de",Totalkg,"kg, c'est supérieur à la masse max en catégorie Utilitaire :",maxCatU,"kg, mais inférieur à la catégorie Normale :",maxCatN,"kg")
else : 
    print("La masse totale est de",Totalkg,"kg")


#graph
x=Totalm
y=Totalkg
x2=zfm
y2=zfw

X=np.array([135,150,425,560])
Y=np.array([650,750,1000,1000])
X2=np.array([370,560])
Y2=np.array([650,1000])
X3=np.array([150,385,510])
Y3=np.array([750,910,910])

plt.title('Masse & centrage F-GOOF')
plt.scatter(x,y,color='red')
plt.scatter(x2,y2,color='orange',label='Zero fuel weight')
plt.arrow(x-7,y-5,x2-x+17,y2-y+10,color='orange',head_length = 10, head_width = 10, length_includes_head = True)
plt.plot(X,Y,color='blue',label='Cat N')
plt.plot(X2,Y2,color='blue')
plt.plot(X3,Y3,label='Cat U')
plt.xlabel('Moment (m/kg)')
plt.ylabel('Masse (kg)')
plt.grid()
plt.legend()
#plt.savefig('masseCentrageFGOOF.png') # si vous voulez sauvegarder le centrogamme enlevez le # devant plt.savefig
plt.show()
print("Moment total :",format(Totalm,'.3f'),"m/kg / Masse totale :",format(Totalkg,'.3f'),"kg / Centrage : ",format(BLfinal,'.3f'),'m')
