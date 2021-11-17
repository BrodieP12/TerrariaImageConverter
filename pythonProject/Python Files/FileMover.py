import os
import sys
import json
StatueIdentifier = ["Statue"]
ToolIdentifier = {"Pickaxe":["Pickaxe","Drill","Reaver Shark","Drill","Picksaw"],"Axes":["Axe","Sawtooth Shark","Waraxe","War axe","Chainsaw","Hamxe","Shroomite Digging Claw"],"Hammers":["Hammer","Hammush","Jackhammer"],"Wiring":["Wrench","Grand Design","Actuation Rod","Wire Cutter"],"Painting":["Paintbrush","Paint Roller","Paint Scraper"],"Hooks":["Grappling Hook","Ivy Whip","Skeletron Hand","Hook"],"Fishing Poles":["Fishing Poll","Fishing Rod","Rod","Fishing Hook","Chum Caster","Fleshcatcher","Fisher of Souls"],"Movement":["Ice Mirror","Magic Mirror","Cell Phone","Rod of Discord","Portal Gun","Umbrella","Tragic Umbrella","Magic Conch","Demon Conch","Snake Charmer's Flute"],"Block-Placing Wands":["Leaf Wand","Living Wood Wand","Rich Mahogany Leaf Wand","Living Mahogany Wand","Hive Wand","Bone Wand"],"Others":["Bucket","Sponge","Bug Net","Sickle","Staff of Regrowth","Clentaminator","Breathing Reed","Binoculars","Guide to Critter Comanionship","Gravedigger's Shovel","Ice Rod","Dirt Rod"]}
MusicBoxes = ["Music Box"]
#Summoning_ItemIdentifier = []
#BlockIdentifier = []
#WallIdentifier = []
#DyeIdentifier = []
#PaintIdentifier = []
#BannerIdentifier = []
#OreIdentifier = []
#BarIdentifier = []
#WoodIdentifier = []
#PotionsIdentifier = []
#AccesoriesIdentifier = []
#PlantsIdentifier = []
#ArmorIdentifier = []
#GemsIdentifier = []
#PaintingsIdentifier = []
#ChestsIdentifier = []
#FurnitureIdentifier = []
#OthersIdentifier = []
#Alphabetical_Order = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ImageFiles = []
dicts = []
dict = {}
for i in os.listdir("../Images Pixel Art/Items Pixel Art/"):
    files = []
    for j in os.listdir("Images Pixel Art/Items Pixel Art/{0}".format(i)):
        files.append(j)
        dict.update({i:files})
ToolsKeys = list(ToolIdentifier.keys())
ToolsValues = list(ToolIdentifier.values())
ItemsKeys = list(dict.keys())
ItemsValues = list(dict.values())
Files = []
def getFiles(name, index):
    for j in ItemsValues:
        for k in j:
            for test in ["armor"]:
                if test in k and k not in Files:
                    key = ItemsKeys[ItemsValues.index(j)]
                    Files.append("{0}/{1}".format(key,k))
    file = open("Images Pixel Art/{0}".format(name),"w")
    for i in Files:
        file.write(i+"\n")
    file.close()

getFiles("Armor",5)