import requests
from bs4 import BeautifulSoup

# find out the main url
base_url = "https://www.domain.com.au/sale/west-ryde-nsw-2114/"

# find out the next url - it's an example for us to crawl through the site
next_page = "https://www.domain.com.au/sale/west-ryde-nsw-2114/?page=2"

# crawling the website with a for loop
for page in range(1, 3):

    # url to loop and crawl
    new_url = base_url + "?page=" + str(page)

    # create a requests object with the new url
    r = requests.get(new_url)

    # we want the content of the requests object created previously
    c = r.content

    # using BeautifulSoup with html parser
    soup = BeautifulSoup(c, "html.parser")

    # using prettify to display our results
    print(soup.prettify())
