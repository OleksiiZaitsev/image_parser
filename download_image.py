import requests
import re
import random
import os
import image_garbage_collector
import except_url_cleaner

path = r'images/'
image_size = 150000
url = 'http://photochki.com/'

except_url = []


# DATA PREPARATION IN LIST BY URL
def data(url):
    page = requests.get(url='{}'.format(url))
    encoding = page.encoding  # GET PAGE CODE
    if encoding == None:
        encoding = 'UTF-8'
        data = r'{}'.format(page.text.encode(encoding=encoding))

        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN
    else:
        data = r'{}'.format(page.text.encode(encoding=encoding))
        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN

# SAVE IMAGE BY URL AND DEF NAME()
def save(url, name, path = 'images/'):

    image = requests.get(url)
    if not os.path.exists(path):
        os.mkdir(path)

    if image.content.__sizeof__() > image_size:
        with open('{}{}'.format(path, name), "wb") as imgfile:
            imgfile.write(image.content)

    # CLEAN FILES FROM THE DICT WITH SAME SIZE
    image_garbage_collector.garbage_collector(path)


# NAME IMAGE BY URL
def name(url):
    split_name = re.split('\/|\-|\?', url)
    search_name = re.findall('(\w+.jpg|\w.png)', '{}'.format(split_name))
    if len(search_name) > 0:
        return str(random.randint(0,500)) + '_' + search_name[0]
    else:
        if re.findall('jpg', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.jpg'
        elif re.findall('png', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.png'
        elif re.findall('ico', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.ico'
        elif re.findall('gif', '{}'.format(split_name)):
            return str(random.randint(0,500)) + '_' + '.gif'


# SEARCH THE TEXT
def search(data):
    for i in except_url_cleaner.except_cleaner(data, url):
        print(i)
        pattern = 'src\=|.{0,10}(h.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}(.png|.jpg|.ico|.JPG|.gif)) *'
        image = re.findall('.png.*|.jpg.*|.ico.*|.JPG.*|.gif.*', i)

        purified = re.search(pattern, i)

        if purified and image:
            #print(purified.group(1))
            if purified.group(1) != None:
                save(purified.group(1), name(purified.group(1)))

        elif re.match('\/\/.+', i):
            except_url.append("{}{}".format('http:', i))

        elif re.match('https|http.+', i):
            except_url.append("{}".format(i))



search(data(url))

while True:
    for i in except_url:
        print(i)
        try:
            print('=========================',except_url)
            search(data(i))
        except:
            print('This site can’t be reached')
