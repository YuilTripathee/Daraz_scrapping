# Introduction
It is a scrapping project. It uses Python sript to scrape data from one of the page in daraz.com (i.e. DSLR section) and renders the result in a text file (output.txt).

# How it works?
1. Run the script.
2. Get the information from output and get your product.

# Libraries applied
```python
import requests
from bs4 import BeautifulSoup as soup
```

# Output structure
The script returns a CSV (Comma Separted Value) format that is used universally. This file can be opened from Microsoft Excel.
![Output Screenshot](docs/scr1.png)