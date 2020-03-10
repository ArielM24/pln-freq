import re
from prettytable import PrettyTable
from bs4 import BeautifulSoup

def get_articles(file):
	f = open(file, encoding="utf-8")
	text_string = f.read()
	f.close()
	articles_segments = re.split("<h3>",text_string)
	articles = []
	for art in articles_segments:
		soup = BeautifulSoup(art,"lxml")
		text = soup.get_text()
		articles.append(text)
	return articles

def mine_topics(topics, articles):
	sz = len(topics)
	num = 0
	freq = {}
	for art in articles:
		cw = []
		for topic in topics:
			a = art.split()
			count = a.count(topic)
			count = (count/sz)*100
			cw.append(count)
		freq[a[0] + " " +str(num)] = cw
		num = num + 1
	return freq

if __name__ == '__main__':
    articles = get_articles("e961024.htm")
    topics = ["crisis","privatización","contaminación","politica","economía","tecnología","televisa"]
    freq = mine_topics(topics, articles)
    arts = freq.keys()
    t = ["id_articulo","crisis","privatización","contaminación","politica","economía","tecnología","televisa"]
    table= PrettyTable(t)
    for i in arts:
        table.add_row([i,freq[i][0],freq[i][1],freq[i][2],freq[i][3],freq[i][4],freq[i][5],freq[i][6]])
    print(table)