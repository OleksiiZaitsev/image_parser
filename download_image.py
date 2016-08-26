import requests
import re
import random
import os
import image_garbage_collector


path = r'images/'
url = 'https://www.artstation.com/'
except_url = []


# DATA PREPARATION IN LIST BY URL
def data(url):
    page = requests.get(url='{}'.format(url))
    encoding = page.encoding  # GET PAGE CODE
    if encoding == None:
        encoding = 'UTF-8'
        data = r'{}'.format(page.text.encode(encoding=encoding))
        print(data)
        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN
    else:
        data = r'{}'.format(page.text.encode(encoding=encoding))
        return data.split('"')  # SPLIT DATA BY THE '"' AND RETURN

# SAVE IMAGE BY URL AND DEF NAME()
def save(url, name, path = 'images/'):
    # try:
    image = requests.get(url)
    if not os.path.exists(path):
        os.mkdir(path)

    if image.content.__sizeof__() > 10000:
        with open('{}{}'.format(path, name), "wb") as imgfile:
            imgfile.write(image.content)

    image_garbage_collector.garbage_collector()

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

# SEARCH THE TEXT
def search(data):
    for i in data:
        if re.match('.{0,25}\/{2}.{1,50}:*\/{0,50}', i):
            image = re.findall('.png.*|.jpg.*|.ico.*|.JPG.*', i)
            print(image)
            if image:
                save(i, name(i))
            # elif re.findall('rss', i):
            #     except_url.insert(0, "{}".format(i))

            elif re.match('\/\/.+', i):
                except_url.append("{}{}".format('http:', i))

            else:
                except_url.append("{}".format(i))
    return except_url

search(data(url))
print(except_url)
while True:
    for i in except_url:
        try:
            search(data(i))

            print(except_url)
        except:
            print('ups')