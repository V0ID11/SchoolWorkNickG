import sqlite3
import numpy as np

# from matplotlib import pyplot as plt

# import re

#from nltk.corpus import stopwords


import gensim
from gensim import corpora
from gensim import models
from gensim.models import KeyedVectors
from gensim import similarities
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, strip_numeric,\
                    strip_non_alphanum, strip_multiple_whitespaces, strip_short
import re
# import keras

# from keras.layers import Dense, Activation, Input, Dropout

# from keras.models import Model

recipes = sqlite3.connect('RecipeSuggestor.db')



SQLQuery = "SELECT ingredients FROM Recipes"
x = recipes.execute(SQLQuery)

values = []
for i in x:
    processed = i[0]
    processed = processed.replace(processed[0], "")
    processed = processed.replace(processed[-1],"")
    processed = processed.replace("'","")
    y =processed.split(",")
    values.append(y)


dictionary = corpora.Dictionary(values)



model = models.Word2Vec(values)



similar_words = {search_term: [item for item in model.wv.most_similar([search_term], topn=5)]
                  for search_term in ['chicken breasts']}

print(similar_words)

word_vectors = model.wv
word_vectors.save("word2vec.wordvectors")

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')

# recipeVector = []
# for a in values:
#     vector = []
#     for z in a
#         vector.append(wv[a])
#     recipeVector.append(vector)
# print(recipeVector)


