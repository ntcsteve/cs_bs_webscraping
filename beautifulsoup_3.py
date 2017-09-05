import requests
from bs4 import BeautifulSoup
import pandas

base_url = "https://www.domain.com.au/sale/west-ryde-nsw-2114/"
next_page = "https://www.domain.com.au/sale/west-ryde-nsw-2114/?page=2"

# create a list called records - we will use it for pandas
records = []

for page in range(1, 3):

    new_url = base_url + "?page=" + str(page)
    r = requests.get(new_url)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")
    all_details = soup.find_all("div", {"class": "listing-result__left"})

    for item in all_details:

        # create a dictionary called listings - we will export it to records
        listings = {}

        try:
            listings["1.Price"] = item.find("p", {"class": "listing-result__price"}).text.strip()
            listings["2.Address"] = item.find("div", {"class": "listing-result__address-line-1"}).text.replace(",", "").strip()
            listings["3.Suburbs"] = item.find("span", {"itemprop": "addressLocality"}).text.strip()
            listings["4.State"] = item.find("span", {"itemprop": "addressRegion"}).text.strip()
            listings["5.Code"] = item.find("span", {"itemprop": "postalCode"}).text.strip()
            listings["6.Beds"] = item.find_all("span", {"class": "property-feature__feature"})[0].text.strip()
            listings["7.Baths"] = item.find_all("span", {"class": "property-feature__feature"})[1].text.strip()
            listings["8.Parking"] = item.find_all("span", {"class": "property-feature__feature"})[2].text.strip()

            # Try to remove the #
            # listings["9.Features"] = item.find("div", {"class": "property-features is-regular listing-result__features"}).text.strip()

        except:
            pass

        # exporting the dictionary (listings) into the list (records)
        records.append(listings)
        print("Before Pandas ...")
        print(listings)

# using pandas for data analysis and manipulation
df = pandas.DataFrame(records)
print("After Pandas ...")
print(df)

# Code to export in csv format
# df.to_csv("domain.csv")
