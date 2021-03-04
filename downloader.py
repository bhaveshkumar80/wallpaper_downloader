import requests
from bs4 import BeautifulSoup
import shutil
import os

def download_wallpaper(celebrity_name):
    name = '-'.join(celebrity_name.split())
    URL = 'https://wallpapercave.com/{}-wallpapers'.format(name)
    html_page = requests.get(URL)
    soup = BeautifulSoup(html_page.content, 'html5lib')

    table = soup.find('div', attrs = {'id': 'albumwp'})
    images = table.findAll('img', attrs = {'class': 'wpimg'})

    url_base = "https://wallpapercave.com/"

    for i, img in enumerate(images):
        url_ext = img.attrs['src']
        full_url = url_base + url_ext

        r = requests.get(full_url, stream=True)
        if r.status_code == 200:
            if not os.path.exists(celebrity_name):
                os.mkdir(celebrity_name)
            filename = celebrity_name + '/' + celebrity_name + '_{}.jpg'.format(i)
            with open(filename, "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

while True:
    name = input('Enter keywords : ')
    try:
        download_wallpaper(name)
        break
    except:
        print("Please enter valid name or check spelling")
        
print('Wallpapers are downloaded!')
print("Thanks for using!")