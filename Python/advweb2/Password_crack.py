"""
Nicole Angelyn T. Lopez
SS151
Asia Pacific College
Note:
Cannot find password for dictionary_attack.zip in short_dict.txt
Add 'cse' word in short_dict.txt to open brute_force.zip using Dictionary Attack
"""
import zipfile
from itertools import product
import time
def open_dict_file():
    while True:
        try:
            dictFile=input("\nEnter dictionary file name: ")
            #If input ends with .txt
            if dictFile.endswith('.txt'):
                openDictFile=open(dictFile)
                return openDictFile
        except:
            pass
def open_zip_file():
    while True:
        try:
            fileToOpen = input("\nEnter zip file name: ")
            #If input ends with .zip
            if fileToOpen.endswith('.zip'):
                openZipFile = zipfile.ZipFile(fileToOpen)
                return openZipFile
        except:
            pass
def brute_force_attack(zip_file):
    x=time.sleep(1)
    print ("Cracking using Brute Force...")
    listChar=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              '1','2','3','4','5','6','7','8','9','0']
    joinListChar=''.join(listChar)
    maxLength=8
    for i in range(1,maxLength+1):
        for items in product(joinListChar,repeat=i):
            password = bytes(''.join(items), 'utf-8')
            try:
                zip_file.extractall(pwd=password)
                return password.decode('utf-8')
            except:
                pass
def dictionary_attack(zip_file,dict_file):
    print ("Cracking using Dictionary...")
    listWord = []
    for word in dict_file:
        stripWord=word.strip()
        listWord.append(stripWord)
    lenListWord = len(listWord)
    for i in range(0, lenListWord):
        password = bytes(listWord[i],'utf-8')
        try:
            zip_file.extractall(pwd=password)
            dict_file.close()
            return password.decode('utf-8')
        except:
            pass
def main():
    law = "R.A 8792"
    prison = "six (6) months to three (3) years"
    print("Cracking zip files.\nWarning cracking passwords is illegal due to law %s"
          "\nand has a prison term of %s"
          "\n" % (law, prison))
    while True:
        crack=input("What type of cracking ('brute force','dictionary', 'both', 'q'): ")
        if crack=="brute force".lower():
            print("\nBrute Force Cracking")
            fileToCrack=open_zip_file()
            startTime=time.process_time()
            password=brute_force_attack(fileToCrack)
            endTime=time.process_time()
            print("Brute force password is %s" % (password))
            print("Elapsed time (sec): %s" % (endTime - startTime))
        elif crack=="dictionary".lower():
            print("\nDictionary Cracking")
            dictToOpen=open_dict_file()
            fileToCrack=open_zip_file()
            startTime = time.process_time()
            password = dictionary_attack(fileToCrack,dictToOpen)
            endTime = time.process_time()
            print("Dictionary password is %s" % (password))
            print("Elapsed time (sec): %s" % (endTime - startTime))
        elif crack=="both".lower():
            print("\nBoth Brute Force and Dictionary attack.")
            dictToOpen=open_dict_file()
            fileToCrack=open_zip_file()
            startTime = time.process_time()
            passDict=dictionary_attack(fileToCrack,dictToOpen)
            endTime = time.process_time()
            if passDict is not None:
                print ("Dictionary password is %s" % (passDict))
            else:
                print ("No password found.")
                print("Dictionary Elapsed time (sec): %s" % (endTime - startTime))
                startTime = time.process_time()
                passBrute=brute_force_attack(fileToCrack)
                endTime = time.process_time()
                print("Brute force password is %s" % (passBrute))
                print("Brute Force elapsed time (sec): %s" % (endTime - startTime))
        elif crack=="q".lower():
            exit()
main()