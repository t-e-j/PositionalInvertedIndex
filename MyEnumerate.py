import nltk
from nltk.stem.lancaster import LancasterStemmer
from collections import defaultdict
import itertools as it

l1 = ["eat", "sleep", "repeat"]

l = "I am tejasvi, i tej"
file_content = open("/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/HW1 documents.txt").read()


with open("/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/HW1 documents.txt", "r") as input:
    input_ = input.read().split('<DOC ')

#print input_[0]
#print input_[1]
#print input_[2]

Doc = input_[2][:1]
#print "This is my document ID"
#print Doc
words=nltk.word_tokenize(file_content)
# creating enumerate objects
obj1 = enumerate(words)
#obj2 = enumerate(s1)

#print "Return type:", type(obj1)
#print list(enumerate(words))

# changing start index to 2 from 0
#print list(enumerate(s1, 2))


#def find_index(l,elem) :
    #return [[i]+[t for t,k in enumerate(j) if k==elem] for i,j in enumerate(l)]
    #print [[i]+[t for t,k in enumerate(j) if k==elem] for i,j in enumerate(l)]

#find_index(l,"i")



mylist = [('1', 1), ('i', 1), ('real', 1), ('lov', 1), ('my', 1), ('nex', 1), ('12', 2), ('thi', 2), ('gre', 2), ('tablet', 2), ('doe', 2), ('everyth', 2), ('i', 2), ('could', 2), ('want', 2), ('it', 2), ('to', 2), ('3', 3), ('i', 3), ('am', 3), ('tejasv', 3), ('10', 4), ('i', 4), ('am', 4), ('bels', 4)]
#mylist = [(1,'tejasvi'),(1,"belsare"), (3,"I"),(4, "I"),(5,"tejasvi")]
#mylist = "do NOT fall for this crappy super slow tablet.. I tried hard , very hard for two weeks to CONVINCE myself that I'm too picky , that I'm asking too much ... I tried to justify its flaws .. In vein .. I ended up hating that piece of disaster so much, to the point I HAD TO THROW IT IN THE GARBAGE CAN.. instead of returning it.. I thought to give it as a present to a child but soon I realized that no child deserves to get so frustrated by its slugginess and hardware ugliness"


dict=defaultdict(list)
for key,value in mylist:
    dict[key].append(value)

#for key in dict:
  #  print key ,dict[key]


text = 'I really love my Nexus!'
text = text.split(' ')
#print text

myarray =[]

myarray.insert()

print myarray
text1 = ['tejasvi','belsare','sfsu','my']
myarray.append(text1)
print myarray



tokens = [['tejasvi','belsare','sfsu','california','california'],['san','francisco','ca'],['tejasvi'],['california','san'],['tejasvi']]

d = defaultdict(lambda:[])
for docID, sub_l in enumerate(myarray):
        for t in set(sub_l):
            d[t].append([docID] + [ind for ind, ele in enumerate(sub_l) if ele == t])
print d



/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/HW1 documents copy.txt
/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/HW1 documents.txt
a-zA-Z0-9
0(touch screen) fix repair
1(great tablet) 2(tablet fast)

4.64 + 2.32

nexus like love happy
asus repair
0(touch screen) fix repair
1(great tablet) 2(tablet fast)
tablet
