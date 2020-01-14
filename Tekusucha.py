"""
07/01/2020
1e version de l'objet Tekusuchā signifiant litteralement texture.
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
                self.secMetaDa = ["none"]
            elif type(a) == int and a != 0:
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
08/01/2020
1e version de l'objet Tekusuchā signifiant litteralement texture.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image.
Dans sa version n*2 il est recommander de l'utiliser pour des images a tendances
statiques avant tout utilisation concernant des sprites nous recommendons une
etude plus approfondit sur les perdormances.
Cet objet fait parti de la branche gpu
NB: il y a un bug avec la rotation de pygame nous esperons 
"""
class Fph0801Tekusucha:
    def __init__(self,acc,sc,a):
        if type(sc) == int:
            self.acc , self.firstMetaDa = Fpx0401loadImages(acc,[sc,sc])
            if a == 0 or a == False or a == "none" and type(a) == int:
                self.acc = self.acc
                self.secMetaDa = ["none"]
            elif type(a) == int and a != 0:
                self.acc = pygame.transform.rotate(self.acc,a)
                self.secMetaDa = ["succes"]
            else:
                print("erreur non fatale")
                self.secMetaDa = ["fail","type de la variable de rotation invalide"]
        elif type(sc) == list:
            self.acc , self.firstMetaDa = Fpx0401loadImages(acc,sc)
            if a == 0 or a == False or a == "none" and type(a) == int:
                self.acc = self.acc
                self.secMetaDa = ["none"]
            elif type(a) == int and a != 0:
                self.acc = pygame.transform.rotate(self.acc,a)
                self.secMetaDa = ["succes"]
            else:
                print("erreur non fatale")
                self.secMetaDa = ["fail","type de la variable de rotation invalide"]
        else:
            self.firstMetaDa = ["fail","erreur au niveau du type de valeurs pour la taille de l'image","ne mettez en type de valeur que des int et des list"]
            print("impossible de charger l'image")
            self.acc = "error"
            self.secMetaDa = ["none"]
        self.metaD = {"first":self.firstMetaDa,"seco":self.secMetaDa}
"""
14/01/2020
3e version de l'objet Tekusuchā signifiant litteralement texture.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image.
Il a ete tester avec des sprit et fonctionne relativement bien.
Cet objet fait parti de la branche gpu.
"""
class Fph1401Tekusucha:
    def __init__(self,acc,sc,a,x,y):
        if type(sc) == list:
            self.acc , self.firstMetaD = Fpx1400loadImages(acc,sc,a)
            self.acc = pygame.transform.scale(self.acc,(sc[0],sc[1]))
            self.acc = pygame.transform.flip(self.acc,x,y)
            if x == True or y = True:
                self.secMetaD = ["flip","succes"]
            else:
                self.secMetaD = ["flip","none"]
        elif type(sc) == int:
            self.acc, self.firstMetaD = Fpx1400loadImages(acc,sc,a)
            self.acc = pygame.transform.flip(self.acc,x,y)
            if x == True or y = True:
                self.secMetaD = ["flip","succes"]
            else:
                self.secMetaD = ["flip","none"]
        self.MetaD = {"fisrt":self.firstMetaD,"sec":self.firstMetaD}
"""
14/01/2020
1e version de l'objet TekusuchāSprite signifiant litteralement texture de sprite.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image plus avancé contenant des sprite et serra prochainement conbiner a la branche principal.
Cet objet fait parti de la branche gpu.
"""
class Fph1401TekusuchaSprite(pygame.sprite.Sprite):
    Class_Object_Index = 0
    def __init__(self,name,x,y,reso,spri):
        super(Fph1401TekusuchaSprite, self).__init__()
        self.images = []
        if len(self.images) == 0 and incr => spri:
            self.images.append(pygame.image.load(str(name)+str(self.incr)+".png"))
            self.incr =+ 1
 
        self.index = 0
  
        self.image = self.images[self.index]
        
        self.rect = pygame.Rect(x, y, reso[0], reso[1])

        self.incr = 0
        Fph1401TekusuchaSprite.Class_Object_Index =+ 1
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            
            self.index = 0
        
        self.image = self.images[self.index]
    def postInistailization(self):
        if len(self.images) == 0 and incr => spri:
            self.images.append(pygame.image.load(str(name)+str(self.incr)+".png"))
            self.incr =+ 1
        
        
        
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
        img = pygame.image.load(str(str(acces)+".png"))
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
"""
14/01/2019
2e version de loadImages
deve : Mahli, Eva
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type gestion des ressources fichiers,
car n'affiche rien.
Pour l'instant ne prend en charge que les .png car possedent une opacitée , elle
traduit neanmoins tout arguments en str.
Elle a pour but d'avoir une meilleur gestion et traduction que celle des
librairies pygames.
"""
def Fpx1400loadImages(acces,scale,rotate):
    try:
        img = pygame.image.load(str(str(acces)+".png"))
        if scale == 0 or scale == False or scale == "none":
            img = pygame.transform.rotozoom(img, rotate, 1)
            if rotate =! 0:
                metaD = ["scale","none","rotate","succes"]
            else:
                metaD = ["scale","none","rotate","none"]
        else:
            img = pygame.transform.rotozoom(img, rotate, scale)
            if rotate =! 0:
                metaD = ["scale","succes","rotate","succes"]
            else:
                metaD = ["scale","succes","rotate","none"]
    except pygame.error:
        img = "error"
        metaD = ["fail"]
        print("impossible de charger l'image png",str(acces))
    return img , metaD
