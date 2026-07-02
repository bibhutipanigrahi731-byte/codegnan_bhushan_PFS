#day-28
'''
'''
import pandas ad pd
import matplotlib.pyplot as plt
import requests
import re
from bs4 import beautifulsoup
url = "http://books.toscrape.com/"
try:
    response = response.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()
except requests.exceptions.requestexception as e:
    print("error fatching data:", e)
    exit()
soup = beautifulsoup(respone.text,"html.parser")
books = soup.find_all(name."articele",class_= "product_pod")
book_name = []
book_price = []
for book in books:
    
    











                      
