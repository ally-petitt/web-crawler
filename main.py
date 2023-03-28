from urlextract import URLExtract
from requests import get
from re import compile
from urllib.parse import urlparse


def valid_uri(uri):
    pattern = '^(http|https)://'
    reg = compile(pattern)
    if reg.search(uri):
        return True
    else:
        return False


def find_links(uri, find_relative_paths=False, recursion_depth=10, counter=0):
    if counter > recursion_depth: return
    if not valid_uri(uri): return


    print("depth = " + str(counter))

    res = get(uri).content.decode()

    extractor = URLExtract()
    full_uris = extractor.find_urls(res)

    if find_relative_paths:
    # pattern = '[\\\/].*\.[\w:]+' this one only gets files with extensions
        pattern = '[\.\\\/].*[\w:]+'
        reg = compile(pattern)
        paths = reg.findall(res)

        # get domain name (look at everything between 2nd and 3rd slash
        parsed_uri = urlparse(uri)
        url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        for path in paths:
            full_uris += [f"{url}/{path}"]


        # prepend domain name to the relative paths

        #full_uris += new_paths

    print("full uri is {}".format(full_uris))
    counter += 1
    [find_links(tmp_uri, find_relative_paths=find_relative_paths, counter=counter, recursion_depth=recursion_depth) for tmp_uri in full_uris if tmp_uri != uri]



if __name__ == '__main__':
    find_links('http://localhost/test.txt', find_relative_paths=True)

