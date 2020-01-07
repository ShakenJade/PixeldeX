"""
07/01/2020
1er version de l'objet Tekusuchā signifiant litteralement texture.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image.
Dans sa version n*1 il est recommander de l'utiliser pour des images a tendances
statiques avant tout utilisation concernant des sprites nous recommendons une
etude plus approfondit sur les perdormances.
Cet objet fait parti de la branche gpu
"""
class Fph0701Tekusucha:
    def __init__(self,acc,sc,a):
        if type(sc) == int:
            self.acc , self.firstMetaDa = Fpx0401loadImages(acc,[sc,sc])
            if a == 0 or a == False or a == "none" and type(a) == int:
                self.acc = self.acc
                self.secMetaDa = ["succes"]
            elif type(a) == int:
                self.acc = pygame.transform.rotate(self.acc,a)
                self.secMetaDa = ["succes"]
            else:
                print("erreur non fatale")
                self.secMetaDa = ["fail","type de la variable de rotation invalide"]
        elif type(sc) == list:
            self.acc , self.firstMetaDa = Fpx0401loadImages(acc,sc)
            self.secMetaDa = ["none"]
        else:
            self.firstMetaDa = ["fail","erreur au niveau du type de valeurs pour la taille de l'image","ne mettez en type de valeur que des int et des list"]
            print("impossible de charger l'image")
            self.acc = "error"
            self.secMetaDa = ["none"]
        self.metaD = {"first":self.firstMetaDa,"seco":self.secMetaDa}
"""
12/11/2019
2e version de loadImages
deve : Mahli
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type gestion des ressources fichiers,
car n'affiche rien.
Pour l'instant ne prend en charge que les .png car possedent une opacitée , elle
traduit neanmoins tout arguments en str.
Elle a pour but d'avoir une meilleur gestion et traduction que celle des
librairies pygames.
notes:Dans de futures versions il est prevu de rajouter des options de post-traitements.
"""
def Fpx0401loadImages(acces,scale):
    try:
        img = pygame.image.load(str(acces+".png"))
        if scale[0] == 0 or scale[1] == 0:
            img = img
            metaD = ["succes"]
        else:
            img = pygame.transform.scale(img,(scale[0],scale[1]))
            metaD = ["succes",str(scale)]
    except pygame.error:
        img = "error"
        metaD = ["fail"]
        print("impossible de charger l'image png",str(acces))
    return img , metaD
