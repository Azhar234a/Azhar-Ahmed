from bs4 import BeautifulSoup
import requests

url="http://www.bbc.com/arabic"
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

news_titles = soup.find_all('h3')
for title in news_titles[:5]:
    print(title.get_text())