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
# librairies pour trouver le chemin d'accès
import os
import sys


### Définitions :
#
# Gestion de dossiers/fichiers.
def pathtofolder():
    return os.path.dirname(sys.argv[0])

def createdatafolder(name):
    os.mkdir(pathtofolder() + '\\' + name)
    pass

def datafolderexist(name):
    return os.path.exists(pathtofolder() + '\\' + name)

def checkfolderdata(folder = 'datas'):
    if datafolderexist(folder):
        return True
    else:
        createdatafolder(folder)
        checkfolderdata(folder)

def datafileexist(filename):
    return os.path.exists(pathtofolder() + '\\datas\\' + filename + '.csv')


# Gestion du csv
def createcsv(filename):
    path = pathtofolder()
    filename = path+'\\datas\\'+ filename
    with open(filename+'.csv', 'w') as csv:
        csv.write("universal_product_code; title; price_including_tax; price_excluding_tax; number_available; product_description; category; review_rating; image_url")
        csv.write("\n")
    pass

def addcsv(data, filename):
    filename = pathtofolder() + '\\datas\\' + filename
    with open(filename + '.csv', 'a') as csv:
        csv.write(data)
        csv.write('\n')
    pass



# Scrapeur
def scrapOne(url):

    # HTML de la page web
    response = requests.get(url)

    # Si code 200 : donne le code html de la page url
    # Parser lxml à install
    soup = BeautifulSoup(response.text, 'lxml')

    # Get Datas :
    product_page_url = url
    cellules = soup.findAll('td')
    desc = (soup.findAll('meta'))[-3]

    stars = soup.find('p', {'class': "star-rating"})
    stars = str(stars).split('\n')[0]

    if 'One' in stars:
        review_rating = 1
    if 'Two' in stars:
        review_rating = 2
    if 'Three' in stars:
        review_rating = 3
    if 'Four' in stars:
        review_rating = 4
    if 'Five' in stars:
        review_rating = 5

    category = soup.findAll("ul", {"class": "breadcrumb"})
    category = str(category).split('\n')[-4].split('>')[1][:-3]

    picture = soup.find('img')
    picture = 'http://books.toscrape.com' + str(picture).split('src="../..')[1][:-3]

    # Write Datas :
    universal_product_code = cellules[0].text
    title = (str(soup.title).split("\n")[1]).replace(" | Books to Scrape - Sandbox", "").replace('    ','')
    price_including_tax = cellules[2].text[2:]
    price_excluding_tax = cellules[3].text[2:]
    number_available = str(cellules[5]).split("(")[1].replace(" available)</td>", "")
    product_description = 'trop long'#str(desc).split('\n')[1]
    category = category
    review_rating = review_rating
    image_url = picture
    datas = '; '.join(list(map(str, (universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url))))
    #print(datas)

    return datas, category

def scraplinksbooks(urlcat):
    response = requests.get(urlcat)

    soup = BeautifulSoup(response.text, 'lxml')

    links = []

    articles = soup.findAll('article', {'class': "product_pod"})

    urlroot = 'http://books.toscrape.com/catalogue'

    for article in articles:
        link = str(article.find('h3').a).split(" title")[0][17:-1]

        links.append(urlroot+link)

    return links

def detectPages(urlcat):
    urlcat = urlcat.replace('index.html', '')
    linkpages = ['index.html']

    response = requests.get(urlcat+linkpages[0])

    soup = BeautifulSoup(response.text, 'lxml')

    next = None

    nextpage = soup.find('li', {'class':'next'})
    if nextpage != None:
        next = (str(nextpage.a).split('">')[0][9:])

    while next != None :
        linkpages.append(next)

        response = requests.get(urlcat + next)
        soup = BeautifulSoup(response.text, 'lxml')

        nextpage = soup.find('li', {'class':'next'})

        if nextpage != None:
            next = (str(nextpage.a).split('">')[0][9:])
        else:
            next = None

    return linkpages

def scrapcat(urlcat):

    linkscat = detectPages(urlcat)

    urlcat = urlcat.replace('index.html', '')

    linksbooks = []

    for i in range(len(linkscat)):
        linksbooks += scraplinksbooks(urlcat+linkscat[i])


    #print(linksbooks)

    return linksbooks

def managecsv(url):
    datas = scrapOne(url)
    checkfolderdata()
    if not datafileexist(datas[1]):
        createcsv(datas[1])
        managecsv(url)
    else:
        addcsv(datas[0], datas[1])


# Fonction motrice

def main(urlcat):
    linkscat = scrapcat(urlcat)
    compteur = 1
    for link in linkscat:
        print(str(compteur) + " " +link)
        compteur += 1
        managecsv(link)
    print("done")


# Action Debbugage
if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    main(url)