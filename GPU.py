from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
my_url = 'https://www.newegg.com/Viedo-Cards-Video-Devices/Category/Id-38?Tpk=graphics%20card'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})


filename = "products.csv"
f = open(filename, "w")

headers = 'brand, product_name, shipping\n'
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand:" + brand)
    print("product_name:" + product_name)
    print("shipping:" + shipping)
    print("\n")
    f.write(brand + ", " + product_name + ", " + shipping + "\n")

f.close()
