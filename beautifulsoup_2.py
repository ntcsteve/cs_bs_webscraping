import requests
from bs4 import BeautifulSoup

base_url = "https://www.domain.com.au/sale/west-ryde-nsw-2114/"
next_page = "https://www.domain.com.au/sale/west-ryde-nsw-2114/?page=2"

for page in range(1, 3):

    new_url = base_url + "?page=" + str(page)
    r = requests.get(new_url)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    # we are only interested with the listing result
    all_details = soup.find_all("div", {"class": "listing-result__left"})

    # extracting all the right data in all_details
    for item in all_details:

        try:
            price = item.find("p", {"class": "listing-result__price"}).text.strip()
            address1 = item.find("div", {"class": "listing-result__address-line-1"}).text.replace(",", "").strip()
            address2 = item.find("span", {"itemprop": "addressLocality"}).text.strip()

        except:
            pass

        print(price)
        print(address1)
        print(address2)
