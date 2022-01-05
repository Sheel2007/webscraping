import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?q=python%20developer&l=Arlington%2C%20VA&vjk=1c4581176f018594'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

labels = soup.find_all("h2")
pres = soup.find_all("pre")
salary = soup.find_all("div", {"class": "attribute_snippet"})

for i in range(len(labels)):
    print(labels[i].text)
    print(pres[i].text)
    try:
        print(salary[i].text, '\n')
    except:
        print('Salary not listed', '\n')

