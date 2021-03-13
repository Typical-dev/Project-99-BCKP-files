import os
import shutil
import time

def main():
    deletedFolders = 0
    deletedFiles = 0
    path = "C:/Users/dhita/Desktop/WhiteHatjr"
    days = 30

    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root,folders,files in os.walk(path):
            if seconds >= getFileOrFolderAge(root):
                removeFolder(root)
                deletedFolders+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(root,folder)
                    if seconds > getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFolders+=1
                for file in files:
                    filePath = os.path.join(root,file)
                    if seconds > getFileOrFolderAge(filePath):
                        removeFolder(filePath)
                        deletedFiles+=1
    else:
        print("Path was not found")

def removeFolder(path):
    if not shutil.rmtree(path):
        print("Successfully deleted the folders")
    else:
        print("Unable to delete the folders")

def removeFiles(path):
    if not os.remove(path):
        print("Successfully deleted the files")
    else:
        print("Unable to deleted the files")

def getFileOrFolderAge(path):
    age = os.stat(path).st_ctime
    return age
