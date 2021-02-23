import requests
from bs4 import BeautifulSoup
import pprint
import sys
from itertools import chain


inputs = sys.argv[1:]


# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
def multiple_res(URL_list):
    
    reses = []

    for URL in URL_list:
        res = requests.get(URL)
        reses.append(res)

    return reses
        
# soup = BeautifulSoup(res1.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
def multiple_soup(res_list, parser = 'html.parser'):

    soups = []

    for res in res_list:
        soup = BeautifulSoup(res.text, parser)
        soups.append(soup)
    return soups


#links = soup.select('.storylink')
def multiple_links(soup_list):

    links = []

    for soup in soup_list:
        link = soup.select('.storylink')
        links.append(link)
    return links


#subtext = soup.select('.subtext')
def multiple_subtext(soup_list):
    
    subtexts = []
    print(soup_list[0])
    for soup in soup_list:
        subtext = soup.select('.subtext')
        subtexts.append(subtext)
    return subtexts


res_list = multiple_res(inputs)
soup_list = multiple_soup(res_list)
link_list = multiple_links(soup_list)
subtext_list = multiple_subtext(soup_list)

def chain_func(arg):
    mega_chain = list(chain.from_iterable(arg))
    return mega_chain

mega_links = chain_func(link_list)
mega_subtext = chain_func(subtext_list)

# mega_links = link_list[0] + link_list[1]
# mega_subtext = subtext_list[0] + subtext_list[1]


print(len(mega_links))
print(len(mega_links))


