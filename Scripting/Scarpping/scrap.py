import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')


#this is a listlike
links = soup.select('.storylink')

#this is a listlike
subtext = soup.select('.subtext')

#this is a listlike
links2 = soup2.select('.storylink')

#this is a listlike
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def most_important_news(hnlist):
    return sorted(hnlist, key = lambda k: k['points'], reverse = True)

def create_custom_hn(links, subtext):

    hn = []

    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        

        if len(vote):

            points = int(vote[0].getText().replace(' points', ''))

            if points > 99:
            

                hn.append({'title': title, 'link': href, 'points': points})
        
    return most_important_news(hn)


pprint.pprint(create_custom_hn(links, subtext))