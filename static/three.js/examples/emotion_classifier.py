import vocabulary
import bernoulliNB

DClasses = ["alegria" , "enojo" , "miedo" , "tristeza"] 

import os

dir = os.listdir("learn_emotion/alegria/")

alegria = []
for file in dir:
    w = open("learn_emotion/alegria/"+file).read()
    alegria.append(w)

dir = os.listdir("learn_emotion/enojo/")

enojo = []
for file in dir:
    w = open("learn_emotion/enojo/"+file).read()
    enojo.append(w)

dir = os.listdir("learn_emotion/miedo/")
miedo = []
for file in dir:
    w = open("learn_emotion/miedo/"+file).read()
    miedo.append(w)

dir = os.listdir("learn_emotion/tristeza/")
tristeza = []
for file in dir:
    w = open("learn_emotion/tristeza/"+file).read()
    tristeza.append(w)


nn_corpus = [sentence.split(' ') for sentence in alegria]
nnn_corpus = [sentence.split(' ') for sentence in enojo]
miedo_corpus = [sentence.split(' ') for sentence in miedo]
tristeza_corpus = [sentence.split(' ') for sentence in tristeza]

nn_corpus = nn_corpus +  nnn_corpus + miedo_corpus + tristeza_corpus

classes = []

for k in range(4):
    for i in range(3):
        classes.append(k)

print classes


voca = vocabulary.Vocabulary("stopwords.txt")
docs = [voca.doc_to_ids(doc) for doc in nn_corpus]

print docs
NB = bernoulliNB.BernoulliNB(voca, docs , classes)

def classify(comment):
    comment = comment.split(' ')
    tst_bow = voca.doc_to_ids_no_add(comment)
    print tst_bow
    return NB.apply(classes, voca, tst_bow)



