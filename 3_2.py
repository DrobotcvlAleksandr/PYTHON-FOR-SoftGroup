import os
def list_folders(route): #функция, которая в качестве аргумента принимает путь к каталогу с файлами и выводит содержимое указанного каталога и всех вложенных подкаталогов
    for top, dirs, files in os.walk(route):
        for nm in files:
          print (os.path.join(top, nm))

list_folders("D:\торрент рождественский")
