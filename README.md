# Indeed.com Job Scraper

<h2>To install Beautiful Soup</h2>
- To install Beautiful Soup, the library we used to scrape the website run


```python
pip install bs4
```

<h2>To install Requests</h2>


```python
pip install requests
```


<h2>To install KMedoids</h2>


```python
pip install scikit-learn-extra
```

<h2>Report and Presentation</h2>
Both the report and video presentation can be found in "COSC 329 - Job Scraper.pdf"


<h2>How To Run The Job Scraper</h2>

For our purposes, we used VScode to create the scraper. These instructions will be assuming you use VSCode or an IDE of your choice to run the scraper.

<ul>
  <li>Open
  main.py
  </li>
  <li>Change the jobTitle variable to the string or job title you want to search for on Indeed.ca</li>
  <li>On line 34, change the Open function parameter to the file you want the scraped job postings to be stored in</li>
  <li>Run the program. The program will print which page number it is on, and which job URL it is currently scraping</li>

</ul>


<h2>How To Run The Data Collection and Processed text</h2>

<ul>
  <li>Open languageCounter.py</li>
  <li>Run the program. The program will scrape all the .txt files in /logs folder, it will process them by converting it to lowercase, stem all the words, and remove all the stop words</li>
  <li>The processed text files can be found in the processedLogs folders</li>
  
</ul>

 <h2>File Structure</h2>
 <ul>
  <li>logs folder contains all the raw, scraped job searches from Indeed.ca</li>
  <li>node_modules folder contains all the stopwords from the english NLTK library</li>
  <li>processedLogs folder contains all the text files that are stemmed and stopwords removed</li>
  <li>languageCounter.py is the stemming and data processing algorithm. See above for more info</li>
  <li>main.py is the scraping file. See above for more info.
 </ul>
  
  
<h2>Project Status</h2>
Jobs scraped: Estimated ~21,202

<h2>Project Steps</h2>
Week 8 - Setup GitHub repo and read Beautiful Soup documentation
  -Completed

Week 9 - Begin basic implementation of web scraper
  -Completed

Week 10 - Continue implementation of the web scraper
  -Completed

Week 11 - Begin implementation of the data analyzer and stemming algorithm
  -Completed

Week 12 - Finalize program
  -Need to scrape more job postings

Week 13 - Submit presentation video
  -Submitted
Week 14 - Submit project deliverables.
  -Submitted
  
  
  [Tap here](https://tsn.ca)
  
>>> ... multiple lines of code


## ... multiple lines of code


``` ... multiple lines of code 

multiple lines of code

multiple lines of code```


` ... multiple lines of code
... multiple lines of code
... multiple lines of code`


> ... multiple lines of code
