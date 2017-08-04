import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

print(soup.h1)

index = 0
# for link in soup.find_all("a"):
#     print("<a href = '{}'>{}</a>".format(link.get("href"),link.text))
#     index += 1
#     if index == 20: break


# group_data = soup.find_all("div",{"class":"info"})
# for item in group_data:
#     print(item.text)