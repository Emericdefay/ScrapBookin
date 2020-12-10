#-------------------------------------------------------------------------------
# Name:        ScrapBookin
# Purpose:     Un .csv pour les gouverner tous.
#
# Author:      Defay Emeric
#
# Created:     10/12/2020
#-------------------------------------------------------------------------------

# Libraires :
# Requests me permet de capturer les informations d'une page web
import requests
# BeautifulSoup de bs4 met permet de parser les élements d'un code source d'une page web
from bs4 import BeautifulSoup


def scrapOne(url):

    # HTML de la page web
    response = requests.get(url)

    # Si code 200 : donne le code html de la page url
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup.findAll('meta'))


    # Get Datas :
    product_page_url = url
    cellules = soup.findAll('td')
    desc = (soup.findAll('meta'))[-3]
    category = soup.findAll("ul", {"class": "breadcrumb"})
    category = str(category).split('\n')[-4].split('>')[1][:-3]
    picture = soup.find('img')
    picture = 'http://books.toscrape.com' + str(picture).split('src="../..')[1][:-3]



    # Write Datas :
    universal_product_code = str(cellules[0])[4:-5]
    title = (str(soup.title).split("\n")[1]).replace(" | Books to Scrape - Sandbox", "").replace('    ','')
    price_including_tax = str(cellules[2])[6:-5]
    price_excluding_tax = str(cellules[3])[6:-5]
    number_available = str(cellules[5]).split("(")[1].replace(" available)</td>", "")
    product_description = "trop long"#str(desc).split('\n')[1]
    category = category
    review_rating = str(cellules[6])[4:-5]
    image_url = picture
    datas = ', '.join(list(map(str, (universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, picture))))
    print(datas)

if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/out-of-print-city-lights-spotlight-no-14_536/index.html"
    scrapOne(url)