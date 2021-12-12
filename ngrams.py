from nltk import ngrams
from nltk import tokenize
import os
import re

allFiles = os.listdir('./processedLogs')
gramDict = dict()
gramCounter = 0

for i in range(len(allFiles)):
    with open(f"./processedLogs/{allFiles[i]}", 'r', encoding='utf-8') as file:
        data = file.read()
        lines = data.splitlines()
        lastLine = lines[-1]
        entryCount = int(lastLine)
        data = tokenize.sent_tokenize(data)  
        for n in range(1, 7):
            print("writing " + str(n) + "gram for file " + allFiles[i])
            for line in lines:
                data = tokenize.sent_tokenize(line)  
                dupeArray = []
                for y in range(len(data)):
                    data[y] = re.sub(r'[^A-Za-z0-9 ]+', '', data[y])
                    ngram = ngrams(data[y].split(), n)

                    for gram in ngram:
                        if gram not in dupeArray:
                            dupeArray.append(gram)
                            if gram in gramDict:
                                gramDict[gram]+=1
                            else:
                                gramDict[gram]=1
            gramDict = sorted(gramDict.items(), key=lambda x: x[1], reverse=True)
            with open(f"./ngram data/{n}gram for {allFiles[i]}", "w", encoding='utf-8') as writeFile:
                for gram in gramDict:
                    if gramCounter < 100:
                        writeFile.write(str(gram))
                        writeFile.write(" " + str("{:.2f}".format(gram[1]/entryCount*100)) + "%")
                        writeFile.write('\n')
                        gramCounter+=1       

            gramDict = dict()
            gramCounter = 0
