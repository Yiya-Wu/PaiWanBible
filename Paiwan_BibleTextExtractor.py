import requests
from bs4 import BeautifulSoup

file_path = "/Users/yiyawu/Documents/yiya/00.txt"

with open(file_path, 'r') as file:
    html_contents = file.read()
    print(html_contents)
    
soup = BeautifulSoup(html_contents, "html.parser")

links = soup.find_all("a", class_="some-class")

for link in links:
    print(link.get("href"))