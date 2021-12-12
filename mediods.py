from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
import os
from nltk import tokenize
import re
from collections import Counter


class main:

    def text_to_v(text):
        WORD = re.compile(r"\w+")
        words = WORD.findall(text)
        return Counter(words)

    def cosine_sim(v1, v2):
        inter = set(v1.keys()) & set(v2.keys())
        numer = sum([v1[x] * v2[x] for x in inter])

        sum1 = sum([v1[x] ** 2 for x in list(v1.keys())])
        sum2 = sum([v2[x] ** 2 for x in list(v2.keys())])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return round(float(numer) / denominator, 6)

    def calcDF(text):
        DF = dict()
        words = text.split()
        # Find term frequency of each word and assign it to that word
        for word in words:
            if word in DF:
                DF[word] += 1
            else:
                DF[word] = 1
        return DF

    def calcTF(vect):
        length = len(vect)
        for word in vect:
            vect[word] = round(vect[word] / length, 4)
        return vect

    results = []
    hello = ""
    allFiles = os.listdir("./processedLogs")
    results = []
    unigram = []
    i = 0
    for file in allFiles:
        with open(f"./processedLogs/{file}", 'r', encoding="utf-8") as file:
            temp = file.read()
        for word in temp:
            hello += word
        results.append(hello)

   # Create a vector with each articles DF score in it
    dfVector = dict()
    for i in range(len(results)):
        dfVector[i] = calcDF(results[i])

    # calculate the TF score of each document.
    tfVector = dict()
    for i in range(len(dfVector)):
        tfVector[i] = calcTF(dfVector[i])

    idfVector = dict()

    TfidfVectorizer = TfidfVectorizer(use_idf=True)
    tfIdf = TfidfVectorizer.fit_transform(results)
    df = pd.DataFrame(tfIdf[0].T.todense(
    ), index=TfidfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    # print the top 25 TF-IDF values
    print("Top 25 TF-IDF values: ")
    print(df.head(25))
    print(len(results))
    # Create nxn matrix:
    matrix = np.zeros((len(allFiles), len(allFiles)))

    # Calculate cosine sum matrix:
    for i in range(len(matrix)):
        doc1 = text_to_v(results[i])
        for k in range(len(matrix)):
            doc2 = text_to_v(results[k])
            matrix[i][k] = cosine_sim(doc1, doc2)
    print("COSINE simularity matrix:\n")

    # Print cosine matrix:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end="")
            print(" , ", end="")
        print(" : \n")

    labels = allFiles
    Z = linkage(matrix, 'single')
    fig = plt.figure(figsize=(25, 10))
    dn = dendrogram(Z, labels=labels)
    plt.show()
