import requests
from datetime import datetime

from bs4 import BeautifulSoup


URL = "http://travaux.ovh.net/?project=31&status=all&perpage=50"
MATCH_STRING = "ex-mail.biz"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


def to_date(match):
    """Convertie un string en objet date"""
    return datetime.strptime(match.string, "%Y-%m-%d, %H:%M")

def last_update(matchs):
    """Retourne la date la plus récente"""
    return max([to_date(date) for date in matchs])

def list_of_matchs(soup):
    """Retourne une lsite de match"""
    matchs = []
    for tr in soup.find_all('tr', class_="severity1"):
        task_sum = tr.find("td", class_="task_summary")
        if task_sum.a.string == MATCH_STRING:
            match = tr.find("td", class_="task_lastedit")
            matchs.append(match.string)
    return matchs


matchs_pars = list_of_matchs(soup)
print(last_update(matchs_pars))