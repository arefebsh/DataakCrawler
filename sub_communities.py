import requests
from bs4 import BeautifulSoup
import re
from query import Query

def sub_community(url, cookie):
    response = requests.get(url, cookie)
    soup = BeautifulSoup(response, 'html.parser')
    sub_communities_data = []
    community_title = re.findall(re.compile(r'<span class=\"active\">(.*)</span>'), response)

    for table in soup.find("table").findAll("tr"):
        sub_community_title = re.findall(re.compile(
            r'<td class=\"trow[1-2]\">\s*<strong><a href=\"forumdisplay\.php\?fid=[0-9]{1,}\">(.*)</a></strong>')
            , str(table))

        # Author
        sub_community_author = re.findall(re.compile(
            r'<br/>\s*توسط\s*<a href=\"https://forum\.dataak\.com/member\.php\?action=profile&amp;uid=[1-9]'
            r'{1,}\">(.*)</a></span>'), str(table))

        author_url = [re.findall(f"<a href=\"(.*)\">{i}</a>", str(table)) for i in sub_community_author]

        # Post
        post_text = re.findall(re.compile(
            r'<a href=\"showthread\.php\?tid=[1-9]&amp;action=lastpost\" title=\"(.*)\"><strong>'),
            str(table))

        post_url = (re.findall(f"<<a href=\"(.*)\" title=\"{p}\"><strong>", str(table)) for p in post_text)

        query = Query(author_url)
        query.user()
        sub_communities_data.append((community_title, sub_community_title, url, post_url))
        query = Query(sub_communities_data)
        query.sub_community()

    return "sub_communities"

