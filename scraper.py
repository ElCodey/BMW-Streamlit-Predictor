import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def request(link):
    return requests.get(link)

def soup(request):
    return bs(request.content, "html.parser")

def aa_scraper_details(soup):
    car_details = []
    price = []
    specs = []
    counter = 2
    
    try:
        for i in range(3000):
            link = "https://www.theaa.com/used-cars/displaycars?keywordsearch=bmw&sortby=closest&page={}&pricefrom=0&priceto=1000000&mymakeid=105".format(counter)
            requests = request(link)
            soups = soup(requests)
    
            for i in soups.find_all("span", {"class": "make-model-text"}):
                car_details.append(i.get_text())

            for i in soups.find_all("div", {"class": "vl-price"}):
                price.append(i.get_text().strip().rstrip("\n"))

            for i in soups.find_all("ul", {"class": "vl-specs"}):
                specs.append(i.get_text().strip())
            
            counter += 1
    except:
        pass
    
    df = pd.DataFrame(
    {'car': car_details,
     'price': price,
     'specs': specs
    })
    
    return df