import os
import sys
import TerrariaColorMatcher as TCM
#print(os.listdir("Images/"))
Images = []
for i in os.listdir("Images/"):
    Images.append(i)
Enemies = []
Weapons = []
for i in os.listdir("Blocks"):
    Enemies.append(i)
#for i in os.listdir("Images/Weapons/"):
#    Weapons.append(i)
#print(Enemies Pixel Art)
#print(Weapons)


class Files:
    def __init__(self, startFile):
        self.files = []
        self.child_files = []
        self.dict = {}
        for i in os.listdir(startFile):
            self.files.append(i)
        for i in range(len(self.files)):
            self.child_files.append([])
            for j in os.listdir(startFile + self.files[i]):
                self.child_files[i].append(j)
            self.dict.update({self.files[i]: self.child_files[i]})
        self.keys = self.dict.keys()
        self.values = self.dict.values()

def update(string):
    letter = 1
    while letter <= len(string):
        new_string = string[0:letter]
        sys.stdout.write("\r")
        sys.stdout.write("{0}".format(new_string))
        sys.stdout.flush()
        letter += 1
fileName = "Summons"

#print(ItemsFilesValues)
#print(EnemyFilesKeys)
#print(WeaponsFilesKeys)
#print(EnemyFilesValues)
#print(WeaponsFilesValues)
failed = 0
#TCM.createAll("Buffs/Activated Furniture/Ammo Box.png","Images Pixel Art/Buffs/Activated Furniture/Ammo Box Pixel Art", "")
def convertFiles(file):
    try:
        os.mkdir("Images Pixel Art/{0}".format(file))
    except:
        pass
    for i in range(len(ItemsFilesKeys)):
        try:
            os.mkdir("Images Pixel Art/{1}/{0}".format(ItemsFilesKeys[i],file))
        except:
            pass
        for j in range(len(ItemsFilesValues[i])):
            name = ItemsFilesValues[i][j].split(".png")[0]
            if ".png.png" in ItemsFilesValues[i][j]:
                try:
                    os.mkdir("Images Pixel Art/{2}/{0}/{1} Pixel Art".format(ItemsFilesKeys[i], name, file))
                except:
                    pass
            else:
                try:
                    os.mkdir("Images Pixel Art/{2}/{0}/{1} Pixel Art".format(ItemsFilesKeys[i], name, file))
                except:
                    pass
            TCM.createAll("{2}/{0}/{1}".format(ItemsFilesKeys[i], ItemsFilesValues[i][j], file),"Images Pixel Art/{2}/{0}/{1} Pixel Art".format(ItemsFilesKeys[i], name, file), "")
            cP = "\033[1;32;40m Image Name: {0}, File: {1}".format(name, ItemsFilesKeys[i])
            update(cP)
#files = ["Accesories","Critters","Dyes"]
#for i in files:
ItemFiles = Files("Accesories/")
# WeaponFiles = Files("Images/Weapons/")
ItemsFilesKeys = list(ItemFiles.keys)
ItemsFilesValues = list(ItemFiles.values)
#print(ItemsFilesKeys)
#print(ItemsFilesValues)
for i in range(len(ItemsFilesKeys)):
    for j in ItemsFilesValues[i]:
        if ".png.png" in j:
            j2 = j.split(".png.png")
            j2 = j2[0]
            j2 = j2 + ".png"
        else:
            j2 = j
        print(f"Accesories/{ItemsFilesKeys[i]}/{j2}")