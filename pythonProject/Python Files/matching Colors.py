import os
import sys


Blocks = open("../Text Files/TerrariaBlockOrder")
Colors = open("../Text Files/RGB Values.txt")
Mixed = open("../Text Files/TerrariaBlockColors.txt", "w")
BlockList = Blocks.readlines()
ColorsList = Colors.readlines()
for i in range(len(BlockList)):
    newLine = BlockList[i].strip("\n") + "|" + ColorsList[i].strip("\n")
    Mixed.write(newLine)
    Mixed.write("\n")