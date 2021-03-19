import requests
from bs4 import BeautifulSoup
from headers import headers


class Login_Dataak:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    def login(self):
        with requests.Session() as session:
            response = session.get(self.url, verify=False, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            my_post_key = soup.find('input', attrs={'name': 'my_post_key', 'type': 'hidden'})
            cookie = response.cookies.get_dict()
            login_data = {"url": f"{self.url}/index.php",
                          'username': f"{self.username}",
                          'password': f"{self.password}",
                          "my_post_key": my_post_key,
                          "action": "do_login"
                          }

            r_post = session.post(f"{self.url}" + "/member.php", data=login_data, verify=False, cookies=cookie, headers=headers)
            return r_post.cookies.get_dict()
