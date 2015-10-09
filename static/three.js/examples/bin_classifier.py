import vocabulary
import bernoulliNB

DClasses = ["positivos" , "negativos"] 

import os

dir = os.listdir("learn2/negativos/")

negativos = []
for file in dir:
    w = open("learn2/negativos/"+file).read()
    negativos.append(w)

dir = os.listdir("learn2/positivos/")
positivos = []
for file in dir:
    w = open("learn2/positivos/"+file).read()
    positivos.append(w)

nn_corpus = [sentence.split(' ') for sentence in positivos]
nnn_corpus = [sentence.split(' ') for sentence in negativos]
nn_corpus += nnn_corpus

classes = []
for i in range(50):
    classes.append(1)
for i in range(50):
    classes.append(0)

voca = vocabulary.Vocabulary("stopwords.txt")
docs = [voca.doc_to_ids(doc) for doc in nn_corpus]

NB = bernoulliNB.BernoulliNB(voca, docs , classes)

def gg():
    print ":B"

def classify(comment):
    comment = comment.split(' ')
    tst_bow = voca.doc_to_ids_no_add(comment)
    print tst_bow
    return NB.apply(classes, voca, tst_bow)



