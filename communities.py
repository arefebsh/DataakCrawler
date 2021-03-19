import requests
from bs4 import BeautifulSoup
import re
from query import Query
from sub_communities import sub_community


def community(url, cookie):
    response = requests.get(url, cookie)
    soup = BeautifulSoup(response, 'html.parser')

    # tables name
    community_data = []
    for table in soup.findAll("table"):
        titles_thead = table.find('thead')
        title = titles_thead.text.strip()

        communities = re.findall(re.compile(
            r'<td class=\"trow[1-2]\">\s*<strong><a href=\"forumdisplay\.php\?fid=[0-9]{1,}\">(.*)</a></strong>')
            , str(table))

        sub_communities = re.findall(re.compile(r'<a href=\"forumdisplay\.php\?fid=[0-9]{1,}" title=\"\">([^</a>]*)')
                                     , str(table))
        query = Query(table)
        query.tables()

        for com in communities:
            u = re.findall(f"<a href=\"(.*)\">{com}</a>", str(table))
            community_url = url + u[0]
            community_data.append((com, community_url))
            query = Query(community_data)
            c_id = query.community()

            if re.findall(f'<div class="smalltext">', str(table)):
                sub_community_url = (url + re.findall(f"<a href=\"([^<]*)\" title=\"\">{sub}</a>", str(table))[0]
                                     for sub in sub_communities)

                for url_sub in sub_community_url:
                    sub_community(url_sub, cookie)

    return "communities and title tables"
