
import random
import time
import requests

while 1:
    url_generate=random.randint(1,4)
    if url_generate==1:
        url="https://www.studnadoucovani.cz/"
    elif url_generate==2:
        url="https://www.studnadoucovani.cz/about"
    elif url_generate==3:
        url="https://www.studnadoucovani.cz/payment"
    elif url_generate==4:
        url="https://www.studnadoucovani.cz/kontakt"
    response = requests.get(url)
    print("idk")    
    sleep_t=random.randint(5,60)
    time.sleep(sleep_t)


