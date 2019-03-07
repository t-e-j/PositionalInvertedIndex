
import sys
import re
#from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import *

from collections import defaultdict

def filtering(eachDocument):
    # This function is used for case normalization , stemming and stopwords removal #

    #st = LancasterStemmer()                             #Using stemmer from  http://www.nltk.org/api/nltk.stem.html
    st = PorterStemmer()                                   #Using python porter stemmer
    stopWords = ['the', 'is', 'at', 'of', 'on', 'and', 'a']     #Stop words list
    mylist = []
    #words = nltk.word_tokenize(eachDocument)               # Not considering words like Google" as " is attached with the word.
    words = re.split('[^a-zA-Z0-9]+',eachDocument)

    for word in words:

        if word.isalpha():
            word = word.lower()                     # Convert to lower case and append
            rootword = st.stem(word)                # Getting root word of the word
            if rootword in stopWords:               # Creating list of root words with document number
                continue
            else :
                mylist.append(rootword)

        elif word.isdigit():                       # Adding numbers in list with document number
            mylist.append(word)

    modifiedDoc = " ".join(mylist)

    return modifiedDoc


def positionalInvertedIndexCreation():
    #This function is used for creation of positional inverted index on the basis of given dataset path#

    givenPath = raw_input("\nKindly provide path of the document set (including name) :")  # Getting file name and path from user

    try:
        file_content = open(givenPath).read()                                       # Read document from given path
        pass
    except IOError:                                                                 # Validation for given file name and path
        print "Unable to open file. Kindly check path and filename again.  "
        sys.exit()

    with open(givenPath,"r") as document:
        content = document.read().split('<DOC ')

    documentArray=[]
    i = 1
    while i in range(len(content)) :

        docArray = content[i].split(">")
        docID = docArray[0]                                 # Getting Document ID
        myDocument = docArray[1].split("</DOC")
        eachDocument = str(myDocument[0])                   # Getting complete document corresponding to collected document ID

        preprocessedDoc = filtering(eachDocument)           # Preprocessing of documents
        sentence = preprocessedDoc.split()

        documentArray.append(sentence)
        i = i+1

    dic = defaultdict(lambda: [])
    for docNumber, word in enumerate(documentArray):        # Getting positions of the terms
        for term in set(word):
            dic[term].append([docNumber] + [index for index, element in enumerate(word) if element == term])

    return dic


def printPositionalInvertedIndex(pInvertedIndex):
    #This function is used for printing created inverted index#
    saveFinalEntry = ()

    print ("\nPlease find below inverted index for given document :\n")
    for array in pInvertedIndex:                                                       # Printing Inverted Index
        totalCount = len(pInvertedIndex[array])                                        # Getting DF

        size = len(array)-1
        docs = pInvertedIndex[array]
        size = 0
        entry = ""
        saveEntry = ()

        for everyEntry in docs:                                                 # This loop stores Positinal Inverted Index in proper format
            everyEntry[0]=everyEntry[0]+1
            count = len(everyEntry)-1
            everyEntry.insert(1,count)
            size = size + everyEntry[1]
            singleTupleEntry =  "{" + str(everyEntry[0]) + "," + str(everyEntry[1]) + ":" + str(everyEntry[2:]) + "}"
            saveTupleEntry = str(everyEntry[0]) , str(everyEntry[1]) , str(everyEntry[2:])
            entry += singleTupleEntry
            saveEntry += saveTupleEntry
        finalEntry = "[" + array + ":" + str(totalCount) + "] \t -> \t" + entry
        saveFinalEntry = saveFinalEntry + (array, totalCount , saveEntry)
        print finalEntry
    return saveFinalEntry


#################
#def main():

#    pInvertedIndex = positionalInvertedIndexCreation()
#    tupleOfPII = printPositionalInvertedIndex(pInvertedIndex)


#main()                                                                          # Calling main function
