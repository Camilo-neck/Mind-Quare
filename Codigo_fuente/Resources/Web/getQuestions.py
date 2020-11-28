from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://0emrne63slsngxkmx1652w-on.drv.tw/PreguntasMindQuare/PaginaWeb/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup)
print(type(soup))