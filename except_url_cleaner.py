import re


def except_cleaner(except_url, url):
    clean_url = set()
    for i in except_url:

        pattern = re.findall(r'(^ht.{0,25}\/{2}.{1,50}:?\/{0,10}.{0,150}) *', i)

        if pattern:
            clean_url.add(i)

    cleaned_url = list(clean_url)
    for i in cleaned_url:
        if i == url:
            cleaned_url.remove(i)

        elif re.findall('(rss)', i):
            rss = i
            cleaned_url.remove(i)
            cleaned_url.insert(0,rss)

    return cleaned_url
