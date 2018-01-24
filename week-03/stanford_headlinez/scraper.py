import requests


def print_hedz(url='https://www.stanford.edu/news/'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for h in htags:
        hedtxt = extract_headline(h)
        print(hedtxt)


def extract_headline(txt):
    return txt.split('<')[2].split('>')[1]


def parse_headline_tags(txt):
    htags = []
    lines = txt.splitlines()

    for line in lines:
        if '<h3><a' in line:
            htags.append(line)
    return htags



def fetch_html(url):
    resp = requests.get(url)
    return resp.text

