import re


def except_cleaner(url, except_url):
    clean_url = []

    if re.findall(r'www', url):
        pattern = re.findall(r'htt.{0,10}\/\/.{0,5}\.([a-z|0-9]+)\.{0,1}.*', url)
    else:
        pattern = re.findall(r'htt.{0,5}\/\/\.{0,1}([a-z|0-9]+)\.{0,1}', url)

    for i in except_url:
        if re.findall(pattern[0], i):

            clean_url.append(i)

    return set(clean_url)

