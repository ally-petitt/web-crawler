from urlextract import URLExtract
from requests import get
from re import sub, compile


def find_links(url, find_relative_paths=False):
    res = get(url).content.decode()

    extractor = URLExtract()
    full_urls = extractor.find_urls(res)
    print(full_urls)

    if find_relative_paths:
    # pattern = '[\\\/].*\.[\w:]+' this one only gets files with extensions
        pattern = '[\.\\\/].*[\w:]+'
        reg = compile(pattern)
        paths = reg.findall(res)
        # get domain name (look at everything before 3rd slash

        # prepend domain name to the relative paths

        #full_urls += new_paths

    print("full url is {}".format(full_urls))
    [find_links(tmp_url, find_relative_paths=find_relative_paths) for tmp_url in full_urls if tmp_url != url]



if __name__ == '__main__':
    find_links('http://localhost/test.txt', find_relative_paths=True)

