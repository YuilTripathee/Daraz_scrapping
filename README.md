# Introduction
It is a scrapping project. It uses Python sript to scrape data from one of the page in daraz.com (i.e. DSLR section) and renders the result in a text file (output.txt).

# Skill sets implemented
1. Scraping data from unstructed resources (like webpages)
2. Object oriented concept
3. JSON and data structure
4. Sorting and searching algorithm
5. Indexing objects in array

# How to run?
1. Run the script `main.py`.
2. Get the information from output and get your product.

# Libraries used
```python
import requests
import urllib
import urllib.parse
import json
import time
from bs4 import BeautifulSoup as soup
```

# Output format
The script returns a CSV (Comma Separted Value) format that is used universally. This file can be opened from Microsoft Excel.
![Output Screenshot](docs/scr1.png)
![Output Screenshot](docs/scr2.png)
