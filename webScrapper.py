# -------------------------- GitHub Website Web-scrapper using python---------------------#


import requests
from bs4 import BeautifulSoup as Bs

github_userName = input('Enter github user name: ')
url = 'http://github.com/' + github_userName
r = requests.get(url)


def repository_number():
    soup = Bs(r.content, 'html.parser')
    no_of_repositories = soup.find('span', {'class': 'Counter'})['title']
    return no_of_repositories


def user_name():
    re = requests.get(url).text
    soup = Bs(re, "lxml")
    for txt in soup.findAll("span", {'class': 'p-name vcard-fullname d-block overflow-hidden'}):
        return txt.text


def repository_names():
    re = requests.get('https://github.com/' + github_userName + '?tab=repositories').text.rstrip()
    soup = Bs(re, "lxml")
    names = []
    for txt in soup.findAll("h3", {'class': 'wb-break-all'}, 'a'):
        names.append(txt.text.replace("\n", '').strip())
        # print(txt.text, end='')
    return names


def location():
    re = requests.get(url).text
    soup = Bs(re, "lxml")
    for txt in soup.findAll("span", {'class': 'p-label'}):
        return txt.text.strip()
        # print(txt.text, end='')


def display_picture_url():
    re = requests.get(url)
    soup = Bs(r.content, 'html.parser')
    display_pic = soup.find('img', {'alt': 'Avatar'})['src']
    return display_pic


def get_intro():
    re = requests.get(url).text
    soup = Bs(re, "lxml")
    for txt in soup.findAll("div", {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'}):
        return txt.text.strip()
        # print(txt.text, end='')


def get_follower_number():
    re = requests.get(url).text
    soup = Bs(re, "lxml")
    for txt in soup.findAll("span", {'class': 'text-bold color-text-primary'}):
        return txt.text.strip()


print('Name of a user: ', user_name())
print('Intro of a user: ', get_intro())
print('Link for display picture: ', display_picture_url())
print('Location: ', location())
print('Followers count: ', get_follower_number())
print('No. of repositories: ', repository_number())
print('Names of repositories: ', repository_names())


