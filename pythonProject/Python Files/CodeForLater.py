import os
EnemyFilesKeys = 0
EnemyFilesValues = 0
WeaponsFilesKeys = 0
WeaponsFilesValues = 0

for i in EnemyFilesKeys:
    os.mkdir("Images Pixel Art/Enemies Pixel Art/" + i + " Pixel Art")
for i in range(len(EnemyFilesValues)):
    for j in range(len(EnemyFilesValues[i])):
        os.mkdir("Images Pixel Art/Enemies Pixel Art/" + EnemyFilesKeys[i] + " Pixel Art/" + EnemyFilesValues[i][j] + " Pixel Art")

for i in WeaponsFilesKeys:
    os.mkdir("Images Pixel Art/Weapons Pixel Art/" + i + " Pixel Art")
for i in range(len(WeaponsFilesValues)):
    for j in range(len(WeaponsFilesValues[i])):
        os.mkdir("Images Pixel Art/Weapons Pixel Art/" + WeaponsFilesKeys[i] + " Pixel Art/" + WeaponsFilesValues[i][j] + " Pixel Art")