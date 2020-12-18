# ScrapBookin
### Projet 2 - OCR
Ce projet permet de scraper des informations d'un site d'exercice : http://books.toscrape.com/<br/>
Les informations scrapés sont : 
* L'url de la page : product_page_url
* L'ID de l'article : universal_product_code
* Le titre : title
* Le prix TTC : price_including_tax
* Le prix HTC :price_excluding_tax
* La quantité d'article disponible : number_available
* La description du produit : product_description
* La catégorie : category
* L'évalution : review_rating
* L'url de l'image : image_url

# Axes d'amélioration
- [ ] Vérification de données existantes dans les fichiers .csv
- [ ] Edition du chemin pour écrire les données.
- [ ] Lecteur : en fonction de l'UPC, donne le prix du livre.
- [ ] Fonction de mise à jour, qui n'efface pas les données déjà extraites.

## Installation
Avant de pouvoir utiliser ce programme, vous devrez procédez à quelques installations.
### 1. Clonage
Veuillez cloner le projet sur votre ordinateur. Pour cela, je vous invite à utiliser Git Bash.<br/>
Tapez : `git clone https://github.com/Emericdefay/ScrapBookin.git` dans un dossier.<br/>
### 2. Environnement virtuel
Montez votre environnement virtuel à la racine du projet. Personnelement j'utilise virtualenv.<br/>
Tapez : `virtualenv env` à la racine du projet depuis un terminal.<br/>
Ensuite pour l'activer, tapez : `source env/scripts/activate`.
### 3. Librairies
Des librairies sont necessaires à l'utilisation du programme, il s'agit de bs4 et de requests. <br/>
Tapez : `pip install -r requirements.txt`.

## Usage
Vous êtes maintenant prêt à utiliser le scraper.<br/>
Pour se faire, restez sur votre terminal.<br/>
Tapez : `python -u ScrapBookin.py`.<br/>
Le -u permet de suivre l'avancement du programme.

## Structure et informations.
Ce programme créé et structure les données dans deux dossiers distincts :
- Le dossier datas : Contient les fichiers .csv, représentants chacune des catégories du site.
- Le dossier pictures : Contient les dossiers d'images au format .jpg pour chacune des catégorie du site.
Attention : Si vous utilisez le programme plus d'une fois, les fichiers .csv seront corrumpus. Veuillez à copier les données et à les isoler du dossier ScrapBookin.


