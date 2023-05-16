import requests as req
from bs4 import BeautifulSoup as bs
import json

def get_html(url):
    html = req.get(url)
    html.encoding = 'utf8'
    return html.text

def get_records(html):
    soup = bs(html, 'html.parser')  # 'lxml'

    trs = soup.find('div', class_='stats-tournament-table').find_all('tr')
    
    records = []
    for tr in trs:
        try:
            tds = tr.find_all('td')
            record = [int(tds[0].text), tds[1].text.replace('\n',''), int(tds[3].text), int(tds[4].text), int(tds[5].text), int(tds[6].text)]
            records.append( record )
        except:
            continue
    
    return records


def to_json(filename, records, sep=','):
    dst = ['num', 'name', 'game', 'win', 'draw', 'defeat']
    lst = []
    for rec in records:
        lst.append(dict(zip(dst, rec)))

    with open('./parsing/results.json', 'w', encoding='utf8') as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)

    f.close()


url = 'https://premierliga.ru/tournament-table'

html = get_html(url)
records = get_records(html)
to_json('./parsing/results.json', records, ';')


