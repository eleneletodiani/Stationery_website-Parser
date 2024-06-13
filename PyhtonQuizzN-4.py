import time
from random import randint
import requests
from bs4 import BeautifulSoup
import csv
file = open('products.csv', 'w', encoding= 'UTF-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['Title', 'Price'])
ind = 1

while ind < 5:
   url = f'https://biblusi.ge/products?category=348&page={ind}'
   response = requests.get(url)
   print(response)
   html = response.text
   soup = BeautifulSoup(html, 'html.parser')
   phone_section = soup.find('div', class_="books w-100 w-md-90 mx-auto NUXT")
   print(phone_section)


   all_books = phone_section.find_all('div', class_= "mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6")

   for book in all_books:
      book_div = book.find('div', {"class": "__product-card"}) #class_='bg-white __product-card d-flex flex-column justify-content-between p8rem')
      p_title = book_div.acronym.text
      p_price = book_div.find('div', class_='text-primary font-weight-700').text
      write_obj.writerow([p_title, p_price])
      print(p_title)
      print(p_price)
   ind += 1
   time.sleep(randint(15,20))




