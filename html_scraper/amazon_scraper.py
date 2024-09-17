from datetime import datetime 
import requests
import bs4
import csv

USER_AGENT ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',    
}


def get_product_price(soup):
     main_price_span = soup.find('span', attrs={
        'class': 'a-price a-text-price a-size-medium apexPriceToPay'
    })
     price_spans = main_price_span.findAll()
     for span in price_spans : 
         price = span.text.strip().replace('$', '').replace(',', '')
         try:
            return float(price)
         except ValueError:
            print('error message')
            exit()
     
    
def get_page_html(url):
    res = requests.get(url = url, headers=REQUEST_HEADER)
    

def extract_product_info(url):
    product_info ={}
    print(f'scraping URL:{url}')
    html = get_page_html(url=url)
    soup  = bs4.BeautifulSoup(html,'lxml')   
    product_info['price'] = get_product_price(soup) 

if __name__ == "__main__":
    with open('amazon_products_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))