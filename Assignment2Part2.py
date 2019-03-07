import Assignment2Part1
#from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import *
import re
import math
import nltk
import operator

def calculateWeight(terms,tupleOfPII):
    #This function calculates score from TF and IDF
    tupleWeight = ()
    queryScore = {}
    queryScore.clear()

    for eachTerm in terms:
        if eachTerm in tupleOfPII:
            requiredIndex = tupleOfPII.index(eachTerm)                  # Checking if word is present in document
        else :
            continue
        requiredDocuments = tupleOfPII[requiredIndex+2]                 # Getting data from positional inverted index

        j = 0
        while j < len(requiredDocuments):
            weightTF = 1 + math.log(float(requiredDocuments[j+1]),2)    #Calculating weight of TF

            DF = len(requiredDocuments)/3                               #Getting document frequency

            weightIDF = math.log((10.0/DF),2)                           #Calculating weight of IDF
            tupleWeight = tupleWeight + (requiredDocuments[j],requiredDocuments[j+1],weightTF,weightIDF)    #Merging weight of TF and IDF in tuple

            j+=3
#####################
    #print tupleWeight
    k = 0
    while k < len(tupleWeight):
        if tupleWeight[k] in queryScore:
            queryScore[tupleWeight[k]] = queryScore[tupleWeight[k]] + (tupleWeight[k+2]*tupleWeight[k+3])   #Calculating score of documents
        else:
            queryScore[tupleWeight[k]] = tupleWeight[k+2]*tupleWeight[k+3]
        k +=4

    return queryScore




def calculateScore(query,tupleOfPII):
    #This function preprocesses the query and call function to calculate TF-IDF weights#

    #st = LancasterStemmer()                                        #Using stemmer from  http://www.nltk.org/api/nltk.stem.html
    st = PorterStemmer()                                            #Using python stemmer porter
    terms = []
    #queryWord = re.split('[^a-zA-Z0-9()]+', query)
    queryWords = nltk.word_tokenize(query)                          #Tokenizing query

    i = 0
    while i<len(queryWords):

        if queryWords[i].isalpha():                                 #Preprocessing the query
            queryWords[i].lower()
            queryWords[i] = st.stem(queryWords[i])
            terms.append(queryWords[i])
        if queryWords[i].isdigit():
            if queryWords[i+1] == '(':                              #Checking if proximity operator is included
                pass
            else:
                terms.append(queryWords[i])
        i = i+1

    queryScore = calculateWeight(terms,tupleOfPII)                   #Calling function for calculating weights

    return queryScore


def calculateProximity(difference, word1, word2,tupleOfPII,answer):
    #This function checks for proximity window and return documents satifying proximity window for given query#
    #answer = []
    doc1ptr = 0
    doc2ptr = 0
    #match = 0
    difference = int(difference) +int(1)                             #Getting proximity window

    if word1 in tupleOfPII:
        pList1 = tupleOfPII[tupleOfPII.index(word1)+2]               #Getting list of documents for proximity word 1
    else:
        return 0

    if word2 in tupleOfPII:                                          #Getting list of documents for proximity word 2
        pList2 = tupleOfPII[tupleOfPII.index(word2)+2]
    else:
        return 0

    while doc1ptr < len(pList1) and doc2ptr < len(pList2):              #Traversing through positional posting list
        if int(pList1[doc1ptr]) < int(pList2[doc2ptr]):               #Check for document number
            doc1ptr += 3
            continue
        elif int(pList1[doc1ptr]) > int(pList2[doc2ptr]):              # Check for document number
            doc2ptr += 3
            continue
        elif int(pList1[doc1ptr]) == int(pList2[doc2ptr]):           # If document matches
            pos1 = pList1[doc1ptr+2]                                   # Get positions of matched document
            pos2 = pList2[doc2ptr+2]                                    # Get positions of matched document

            pos1 = pos1.replace('[','').replace(']','')
            pos2=pos2.replace('[','').replace(']','')

            pos1 = re.split(',',pos1)
            pos2 = re.split(',',pos2)

            pos1ptr = 0
            pos2ptr = 0

            while pos1ptr < len(pos1) and pos2ptr < len(pos2):              #Traversing through positions
                if int(pos2[pos2ptr]) - int(pos1[pos1ptr]) > 0 :            #Check for proximity window

                    if int(pos2[pos2ptr]) - int(pos1[pos1ptr]) <= difference :      #If proximity window matches
                        answer.append(pList1[doc1ptr])
                        #match = 1
                        break
                    else :
                        pos1ptr +=1

                else:                                                         #Increment the pointer if doesnot match
                    if int(pos2[pos2ptr]) <= int(pos1[pos1ptr]):
                        pos2ptr += 1
                    else:
                        pos1ptr += 1

        doc1ptr += 3
        doc2ptr += 3
    #if match == 0:
    #    print "No documents found!"
    #if match == 1:
    #    print "Match found!"

    return answer


def checkProximity(query,tupleOfPII,answer):
    #This function performs preprocessing on proximity query and calls function to check for proximity matching documents#

    #st = LancasterStemmer()                                        #Using stemmer from  http://www.nltk.org/api/nltk.stem.html
    st = PorterStemmer()                                            #Using python stemmer porter
    queryWords = nltk.word_tokenize(query)                          #Tokenizing words

    i = 0
    while i < len(queryWords):                                      #Preprocessing of proximity query
        if queryWords[i].isalpha():
            queryWords[i].lower()
            queryWords[i] = st.stem(queryWords[i])
        i = i + 1

    j = 0
    while j < len(queryWords):
        if queryWords[j] == "(":                                    #Checking for proximity window
            #answer = []
            difference = queryWords[j-1]                            #Getting proximity window

            word1 = queryWords[j+1]                                 #Getting proximity word1
            word2 = queryWords[j+2]                                 #Getting proximity word2
            answer = calculateProximity(difference,word1,word2,tupleOfPII,answer)  #Calling function for getting documents satisfying proximity
        j+=1
    return answer                                                   #Returning documents satifying proximity




def main():
    # This is main function which accepts user's choice and provide output accordingly#
    answer = []
    pInvertedIndex = Assignment2Part1.positionalInvertedIndexCreation()             #Calling function to create positional inverted index

    tupleOfPII = Assignment2Part1.printPositionalInvertedIndex(pInvertedIndex)      #Calling function to print and store positional inverted index

    choice = 'y'
    while choice == 'y':
        matchedProximities={}
        choice = raw_input("\n\n Do you want to enter query? (press 'y' if yes / any other key to come out!)")
        if choice == 'y':
            query = raw_input("\n\nKindly enter the query :")

            words = nltk.word_tokenize(query)                       #Tokenizing query
            answer = []
            ordered = {}
            if '(' in words:                                        #Checking for proximity window
                #answer = []
                answer = checkProximity(query,tupleOfPII,answer)   # Go for proximity function

            queryScore = calculateScore(query,tupleOfPII)           #Getting score of the query document wise
            #print queryScore


            print "\n \nBelow documents are retrieved : "
            if not answer:                                          #If proximity window is not there
                ordered = sorted(queryScore.items(), key=operator.itemgetter(1), reverse=True)
                for key, value in ordered:
                    print "Doc " + key + "   ==> Score  " + str(value)

            else :                                                  #If proximity window is there
                for doc in answer:
                    if doc in queryScore:
                        matchedProximities[doc] = queryScore[doc]   #Check for common documents
                        #print

                pordered = sorted(matchedProximities.items(), key=operator.itemgetter(1), reverse=True)
                #print matchedProximities
                for key, value in pordered:
                    print "Doc "+key + "   ==> Score  " + str(value)

        else :
            break



main()                                                                                           # Calling main function
