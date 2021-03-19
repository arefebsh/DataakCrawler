from login import Login_Dataak
from communities import community
from create_table import Create_Table

url = "https://forum.dataak.com/"
login = Login_Dataak("crawling", "32145713", url)
cookie = login.login()
re = Create_Table()
re.query_create()
community(url, cookie)
