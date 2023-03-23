from urlextract import URLExtract
from requests import get


def find_links(url):
    res = get(url).content.decode()

    extractor = URLExtract()
    full_urls = extractor.find_urls(res)
    print(full_urls)



if __name__ == '__main__':
    find_links('http://localhost/index.html')

