import re
url = 'https://www.artstation.com/'

except_url = ['https://www.artstation.com/', 'http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6.1/html5shiv.js', 'https://www.artstation.com/artwork.rss', 'https://www.artstation.com/artwork.rss?sorting=latest', 'http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,400,300,600,700,800', 'https://www.artstation.com/assets/application-d1d7943a77af9f663a59332ee32c083c.css', 'https://www.artstation.com/assets/application-22be454109c38274bd4b66633ea43c28.js', 'https://www.artstation.com/assets/community-0e69a583aa0b3cf14cdba16fb698841b.js', 'https://d31qbv1cthcecs.cloudfront.net/atrk.js', 'https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=jzg4k1a0Sn00Ua', 'http://magazine.artstation.com', 'http://support.artstation.com', 'http://eepurl.com/JF5iP', 'https://www.facebook.com/artstationhq', 'https://twitter.com/ArtStationHQ', 'http://www.ballistiq.com', 'http://www.ballistiq.com']

def except_cleaner(url, except_url):
    clean_url = []
    pattern = re.findall(r'htt.{0,10}\/\/.{0,5}\.([a-z|0-9]+)\.{0,1}.*', url)
    for i in except_url:
        if re.findall(pattern[0], i):

            clean_url.append(i)
    print(clean_url)

except_cleaner(url, except_url)