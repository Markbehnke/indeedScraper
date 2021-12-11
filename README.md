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


<h2>To Run The Data Collection and Processed text</h2>

<ul>
  <li>Open languageCounter.py</li>
  <li>Run the program. The program will scrape all the .txt files in /logs folder, it will process them by converting it to lowercase, stem all the words, and remove all the stop words</li>
  <li>The processed text files can be found in the processedLogs folders</li>
  
</ul>

  


