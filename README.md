# stylehaat_crawler
Crawler for https://www.stylehaat.com/.  
Python Version: 3.7  

Exports data into JSON file using following command: 
"scrapy crawl stylehaat_product -o items.json"  

For CSV file 
"scrapy crawl stylehaat_product -o items.csv"  

Following data is scrapped  
1. Product category 
2. Product Name 
3. Product New Price 
4. Product Image 
5. Product Description 

Install dependency using following command: 
"pip install requirements.txt"
