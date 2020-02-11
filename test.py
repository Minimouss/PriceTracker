import requests
import pandas as pd
from bs4 import BeautifulSoup

locURL = "D:\\01_EasyTrack\\"
filename = "Inventaire.ods"

webURL = "https://www.amazon.fr/IZOKEE-Connecteur-Femelle-Connecteurs-Terminals/dp/B01MY8FLMV/"
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

doc = ezodf.opendoc(locURL + filename)
pd.read_excel(doc, engine="odf")


# page = requests.get(URL, headers=header)
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
# price = soup.select_one("span[id=price_inside_buybox]").text.strip()
# converted_price = float(price[0:2] + str(".") + price[3:5])
#
# print(price, type(price))
# print(converted_price, type(converted_price))
