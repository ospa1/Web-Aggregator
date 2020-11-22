import re

import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    """ Homepage """

    urls = ["https://yahoo.com",
            "https://bbc.com",
            "https://businessinsider.com",
            "https://time.com",
            "https://nbcchicago.com"]

    links = []
    for url in urls:
        website = url[8:-4]
        # todo function is too slow, use threading
        url_links = get_links(url)
        links += [(website, url_links)]
        print(website)
    context = {'links': links}
    return render(request, 'web_aggregators/index.html', context)


# todo return only 5 links
# retrieves a list of links from a url
def get_links(url):

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    tags = soup.findAll("a")
    links = []
    num = 0
    for tag in tags:
        link = tag.get("href")
        title = tag.text[:70]

        if 'http' not in link:
            link = url + link
            links.append((link, title))
            num += 1
        if num >= 5:
            break
    return links
