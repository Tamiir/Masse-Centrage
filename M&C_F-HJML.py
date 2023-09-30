# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:47:21 2021
@author: Paul
"""

#F-HJML

import matplotlib.pyplot as plt
import numpy as np

ew = 725.7  #Poids à vide (kg)

# les bras de levier :
blew = 1.038
blAV = 0.864
blAR = 1.854
blFuel = 1.227
#blSupp = 1.61
blBagages = 2.413
blBagages2 = 3.124

# les limites :
maxCatN = 1111
maxCatU = 953
limFuel = 212
#limSupp = 1
limBagages1 = 54
limBagages2 = 22.7
limbagages = 54

rhoFuel = 0.72  #densité du fuel (kg/L)

# les inputs :
kgAV = float(input("poids passagers AV (kg) : "))
kgAR = float(input("poids passagers AR (kg) : "))
LFuel = float(input("Litres de fuel (L) (max:212 L): "))
if LFuel > limFuel :
    while LFuel > limFuel :
        LFuel = float(input("c'est trop, choisir une valeur valable (max:212 L) : "))
kgFuel=LFuel*rhoFuel

kgBagages = float(input("kg de bagages zones 1(kg) (max:54 Kg): "))
kgBagages2 = float(input("kg de bagages zones 2(kg) (max:22.7 Kg attention le total doit etre inférieur à 54Kg): "))
if kgBagages > limBagages1 :
    while kgBagages > limBagages1 :
        kgBagages = float(input("c'est trop , choisir une valeur valable : "))
if kgBagages2 > limBagages2 :
    while kgBagages2 > limBagages2 :
        kgBagages2 = float(input("c'est trop , choisir une valeur valable : "))
if kgBagages+kgBagages2 > limbagages :
    while kgBagages+kgBagages2 > limbagages :
        kgBagages = float(input("kg de bagages zones 1(kg) : "))
        kgBagages2 = float(input("kg de bagages zones 2(kg) : "))
    
    
# les calculs de moments (masse * bras de levier = moment):
mew=ew*blew
mAV=kgAV*blAV
mAR=kgAR*blAR
mFuel=kgFuel*blFuel
#mSupp=kgSupp*blSupp
mBagages=kgBagages*blBagages
mBagages2=kgBagages2*blBagages2


Totalkg = ew+kgAV+kgAR+kgFuel+kgBagages+kgBagages2
Totalm = mew+mAV+mAR+mFuel+mBagages+mBagages2
zfw=ew+kgAV+kgAR+kgBagages+kgBagages2
zfm=mew+mAV+mAR+mBagages+mBagages2

BLfinal = Totalm/Totalkg

#Checking
if Totalkg>maxCatN:
    print("La masse totale est de",Totalkg,"kg, c'est supérieur à la masse max :",maxCatN,"kg")
elif Totalkg>maxCatU:
    print("La masse totale est de",Totalkg,"kg, c'est supérieur à la masse max en catégorie Utilitaire :",maxCatU,"kg, mais inférieur à la catégorie Normale :",maxCatN,"kg")
else : 
    print("La masse totale est de",Totalkg,"kg")


#tracés/centrogrammes

x=Totalm
y=Totalkg
x2=zfm
y2=zfw

X=np.array([635,780,1125,1325])
Y=np.array([715,885,1111,1111])
X2=np.array([850,1325])
Y2=np.array([715,1111])
X3=np.array([739,980])
Y3=np.array([715,945])
X4=np.array([880,980])
Y4=np.array([945,945])

plt.title('Masse & centrage F-HJML')
plt.scatter(x,y,color='red')
plt.scatter(x2,y2,color='orange',label='Zero fuel weight')
plt.arrow(x-7,y-5,x2-x+17,y2-y+10,color='orange',head_length = 10, head_width = 10, length_includes_head = True)
plt.plot(X,Y,color='blue',label='Cat N')
plt.plot(X2,Y2,color='blue')
plt.plot(X3,Y3,label='Cat U',color='steelblue')
plt.plot(X4,Y4,color='steelblue')
plt.xlabel('Moment (m/kg)')
plt.ylabel('Masse (kg)')
plt.grid()
plt.legend()
#plt.savefig('masseCentrageFHJML.png') #pour sauvegarder le graphique enlevez le # devant plt.savefig
plt.show()
print("Moment total :",format(Totalm,'.3f'),"m/kg / Masse totale :",format(Totalkg,'.3f'),"kg / Centrage : ",format(BLfinal,'.3f'),'m')
