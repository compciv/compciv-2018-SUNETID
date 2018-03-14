from pathlib import Path
from bs4 import BeautifulSoup

import csv

OUTPUT_HEADERS = [
    'first_name',
    'last_name',
    'category',
    'report_type',
    'url',
    'date',
]



def make_senate_csv(html):

    soup = BeautifulSoup(html, 'lxml')
    tags = soup.select('tbody tr' ) 


    ofile = output_filepath.open('w')
    cfile = csv.DictWriter(ofile, fieldnames=OUTPUT_HEADERS)
    cfile.writeheader()

    for row in tags:
        cols = row.select('td')
        d = { }
        d['first_name'] = cols[0].text.strip()
        d['last_name'] = cols[1].text.strip()
        d['category'] = cols[2].text.strip()
        d['report_type'] = cols[3].text.strip()
        link = cols[3].select_one('a')
        d['url'] = link.attrs['href'] 
        d['date'] = cols[4].text.strip()

        cfile.writerow(d)

    ofile.close()

