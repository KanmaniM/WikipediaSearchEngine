import sys
import time
import os
wordInEachFileThreshold = 100000





def split(absPathOfMergeFile,folderLocationOfIndex):
    global wordInEachFileThreshold
    index = 0
    count = 0
    file1 = absPathOfMergeFile
    secIndFile = folderLocationOfIndex + "secondaryIndex.txt"
    
    fp1=open(file1,'r') 
    sf =open(secIndFile,'w')
    
    lineFile1 = fp1.readline().strip('\n')
    
    while( lineFile1 ):


        if(count == 0):
            indexFileName = folderLocationOfIndex + "index_" + str(index) + ".txt"
            wordFile1 = lineFile1.split(":")[0]
            sf.write(wordFile1 + '\n')
            fp2 = open(indexFileName, 'w')
        
        fp2.write(lineFile1 + '\n')
        
        count += 1
        
        if(count == wordInEachFileThreshold):
            count = 0
            index += 1
            fp2.close()
        lineFile1 = fp1.readline().strip('\n')
    
    fp1.close()
    fp2.close()
    sf.close()
    os.remove(absPathOfMergeFile)




def mergeTwoFiles(file1 , file2 , folderLocationOfIndex):
    print("merge:",file1," ",file2)
    if file1 == file2:
        return
    fp1 = open(file1, 'r')
    fp2 = open(file2, 'r')
    tempFile = folderLocationOfIndex + "temporary.txt" 
    fp3 = open(tempFile, 'w')
    lineFile1 = fp1.readline().strip('\n')
    lineFile2 = fp2.readline().strip('\n')
    while (lineFile1 and lineFile2):
        wordFile1 = lineFile1.split(":")[0]
        wordFile2 = lineFile2.split(":")[0]
        if wordFile2 < wordFile1:
            fp3.write(lineFile2 + '\n')
            lineFile2 = fp2.readline().strip('\n')
        elif wordFile1 < wordFile2:
            fp3.write(lineFile1 + '\n')
            lineFile1 = fp1.readline().strip('\n')
        else:
            list1 = lineFile1.strip().split(":")[1]
            list2 = lineFile2.strip().split(':')[1]
            fp3.write(wordFile1 + ':' + list1 + list2 + '\n')
            lineFile1 = fp1.readline().strip('\n')
            lineFile2 = fp2.readline().strip('\n')
    while lineFile1:
        fp3.write(lineFile1 + '\n')
        lineFile1 = fp1.readline().strip('\n')
    while lineFile2:
        fp3.write(lineFile2 + '\n')
        lineFile2 = fp2.readline().strip('\n')
    os.remove(file1)
    os.remove(file2)
    os.rename(tempFile, file1)



def mergeFiles(folderLocationOfIndex):
    listOfIndexFiles = []
    for filename in os.listdir(folderLocationOfIndex):
        fileLocation = folderLocationOfIndex + filename
        listOfIndexFiles.append(fileLocation)
    listOfIndexFiles.sort()

    while(len(listOfIndexFiles)>1):
        file1 = listOfIndexFiles[0]
        file2 = listOfIndexFiles[1]
        mergeTwoFiles(file1 , file2 , folderLocationOfIndex)
        listOfIndexFiles.remove(listOfIndexFiles[1])
    split(listOfIndexFiles[0],folderLocationOfIndex)
        

startTime = time.time()
# mergeFiles(sys.argv[1])
# os.mkdir("merge")

import pickle
file = sys.argv[1]


titleFile = open(file, 'rb')
tf = pickle.load(titleFile) 
count = 0
for keys in tf: 
    print(keys, '=>', tf[keys])
    count += 1
    if(count == 35):
        break 
titleFile.close() 


word = sys.argv[2]
wordFile = open(word, 'rb')
wf = pickle.load(wordFile) 
count = 0
for keys in wf: 
    print(keys, '=>', wf[keys][0] , "$$$$$$4", wf[keys][1] )
    count += 1
    if(count == 35):
        break 
wordFile.close() 



print("Total time : " + str(time.time() - startTime))

  
