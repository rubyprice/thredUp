from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.thredup.com/handbags?department_tags=handbags&search_tags=women-handbags'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
grid_item = page_soup.findAll("div",{"class":"uiUj-TxKXzmIOHZu6poxM grid-item"})

filename = "products.csv"
f = open(filename, "w")

headers = "product, sale, retail\n"
f.write(headers)


for item in grid_item:
	brand = item.img["alt"]
	sale_price = item.b.text
	
	sale = item.find("span",{"class":"_2EmC22frwH7zVD84OnujZa"})
	
	retail_price = str(sale.text)


	print("brand: " + brand)
	print("sale price: " + sale_price)
	print("retail price: " + retail_price)

	f.write(brand + "," + sale_price + "," + retail_price + "," +  "\n")

f.close()
