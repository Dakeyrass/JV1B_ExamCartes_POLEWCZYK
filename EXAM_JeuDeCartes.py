def Swap(tableau,tableau1,n,t):
    stock1=tableau[n]
    tableau[n]=tableau1[t]
    tableau1[t]=stock1
    return tableau 
'''Test=[1,2,3]
Test1=[4,5,6]
print(Swap(Test,Test1,0,2))'''
#J'ai tenté une technique de permutation mais je n'ai pas su la mettre en oeuvre dans les classes. 

class Carte:
    def __init__(self,cout,nom,description):
        self.__coutmanaa=cout
        self.__name=nom
        self.__description=description
    def getCout(self):
        return self.__coutmanaa
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description
class Cristal(Carte):
    def __init__(self,cout,nom,description,valeur):
        Cristal.__init__(self,cout,nom,description)
        self.__valeur = valeur
    def PlayCristal(self,magejoueur):
        magejoueur.getMana -= self.__coutmanaa 
        magejoueur.getTotal += self.__valeur
class Creature(Carte):
    def __init__(self,cout,nom,description,pv,scoreatk):
        Creature.__init__(self,cout,nom,description)
        self.__vie=pv
        self.__scoreatk=scoreatk
    def atk(self,cible):
        cible.getTotal -= self.__coutmanaa
        cible.getPv -= self.__scoreatk
    def pvPerdu(self,dgt):
        self.__vie -= dgt
        #if (self.__vie<=0):
        #    Creature.append(defausse) => j'ai encore ce problème de variable qui appartient à une classe et qui donc ne peut être utilisée ailleurs. 
class Blast(Carte):
    def __init__(self,cout,nom,description,valeur):
        Blast.__init__(self,cout,nom,description)
        self.__valeur=valeur
    def PlayBlast(self,joueurennemi):
        joueurennemi.getPv -= self.__valeur

carteA=Carte(10,"Super Monstre","Elle ne fait rien, elle est simplement chère.")

class Mage:
    def __init__(self,nom,pv,main):
        self.__name=nom
        self.__pv=pv
        self.__total=100
        self.__actuel=100
        self.__main=main
        self.__defausse=[]
        self.__jeu=[1,2,3,4]
    def getName(self):
        return self.__name
    def getPv(self):
        return self.__pv
    def getMana(self):
        return self.__actuel
    def getMain(self):
        return self.__main
    def getDefausse(self):
        return self.__defausse
    def getZone(self):
        return self.__jeu
    def getTotal(self):
        return self.__total
    def PlayCard(self,cartechoisie):
        self.__jeu = cartechoisie #Ici je voulais ajouter la carte dans le tableau. 
        self.__actuel -= cartechoisie.getCout() 
        #Ici, le pb est que getCout est dans une autre classe, et je n'ai pas trouvé d'autres solutions pour récupérer la valeur. 
        #J'ai eu exactement le même problème à d'autres endroits. 
    #def recupMana(self):
    #def atk(self,ennemi,dgt):
    #    ennemi.getPv() -= dgt
    
mageA=Mage("Random",100,Carte(10,"Super Monstre","Elle ne fait rien, elle est simplement chère."))
print(mageA.PlayCard(carteA))
print(mageA.getZone())