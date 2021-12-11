import os


allFiles = os.listdir("indeedScraper\\logs")
languages = ["python", "java", "c++", "sql", "html", "php" ]

# Start Iterating through all the files in the folder
for i in range(len(allFiles)):
    wordCounts = dict()
    with open("indeedScraper\logs\\" + allFiles[i], 'r', encoding="utf-8") as file:
            data = file.read().lower()
            entryCount = data.count('scrapedjobid')
            
            #Split the data into each individual job posting
            for entry in data.split('scrapedjobid'):
                # If entry is empty then decerement the total count by 1
                if len(entry) < 8:
                    entryCount-=1
                #Loop through every word in the languages array and check if it is in the job posting
                for word in languages:
                    if word in entry:
                        if word in wordCounts:
                            wordCounts[word]+=1 
                        else:
                            wordCounts[word]=1

    print("Word counts in " + allFiles[i])                   
    print(wordCounts)
    for word in wordCounts:
        wordCounts[word] = "{:.2f}".format(wordCounts[word]/entryCount*100) + "%"
    print("Word counts as a % of total files that have it")
    print(wordCounts)    
    print('\n')
