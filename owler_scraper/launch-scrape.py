import requests
from bs4 import BeautifulSoup

url = "https://temple.campuslabs.com/engage/organizations"
#download the URL and extract the content to the variable html 
response = requests.get(url, cookies={'__test': '2501c0bc9fd535a3dc831e57dc8b1eb0'})
html = response.content
print(html)
#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parser')
#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div",attrs={'id':'org-search-results'})
#print(main_table)
#Now we go into main_table and get every a element in it which has a class "title" 
links = main_table.find_all("a", attrs={'style': 'display: block; text-decoration: none; margin-bottom: 20px;'})

#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted 
extracted_records = []
for link in links:
    url = link['href']
    title = link.find("div", attrs={'style':'font-size: 18px; font-weight: 600; color: rgb(73, 73, 73); padding-left: 5px; text-overflow: ellipsis; margin-top: 5px; overflow: initial; height: initial;'}).text
    record = {
        'title':title,
        'url':url
        }
    extracted_records.append(record)
print(extracted_records)