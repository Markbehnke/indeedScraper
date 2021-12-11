import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')


allFiles = os.listdir("./logs")
languages = ["python", "java", "c++", "sql", "html", "php"]


def stemming(desc, oldFile):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    with open(f"./processedLogs/{oldFile}.txt", 'a', encoding="utf-8") as file:
        desc = desc.split()
        for word in desc:
            if not word in stop_words:
                file.write(f"{ps.stem(word)} ")
        file.write("\n")
    file.close()


# Start Iterating through all the files in the folder
for individualFiles in allFiles:
    wordCounts = dict()
    with open("./logs\\" + individualFiles, 'r', encoding="utf-8") as file:
        data = file.read().lower()

        entryCount = data.count('scrapedjobid')

        # Split the data into each individual job posting
        for entry in data.split('scrapedjobid'):
            stemming(entry, individualFiles)
            # If entry is empty then decerement the total count by 1
            if len(entry) < 8:
                entryCount -= 1
            # Loop through every word in the languages array and check if it is in the job posting
            for word in languages:
                if word in entry:
                    if word in wordCounts:
                        wordCounts[word] += 1
                    else:
                        wordCounts[word] = 1

    print("Word counts in " + individualFiles)
    print(wordCounts)
    for word in wordCounts:
        wordCounts[word] = "{:.2f}".format(
            wordCounts[word]/entryCount*100) + "%"
    print("Word counts as a % of total files that have it")
    print(wordCounts)
    print('\n')
