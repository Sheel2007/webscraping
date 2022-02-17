import subprocess
import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl

try:
    p = subprocess.run('rm profile_img.jpg', capture_output=True)
    a = subprocess.run('rm -rf repo_url', capture_output=True)
except:
    pass

ssl._create_default_https_context = ssl._create_unverified_context


def get_image(soup):
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    urllib.request.urlretrieve(profile_image, "profile_image.jpg")

def get_repos(soup):
    repos = soup.find_all("span", {"class": "repo"})
    print('Here are the repositories this user has: ')
    for repo in repos:
        print(repo.text)

def get_url(url, repo):
    return url + '/' + repo

def clone(repo_url):
    try:
        subprocess.Popen(['git', 'clone', str(repo_url), 'repo_url'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    except:
        print('invalid repo link')

while True:
    github_user = input('Input Github User: ')
    if github_user == 'quit':
        break
    url = 'https://github.com/' + github_user

    r =  requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    get_image(soup)
    get_repos(soup)
    repo = input('Which repo would you like to download? ')
    repo_url = get_url(url, repo)
    clone(repo_url)