import re
from bs4 import BeautifulSoup
from pickle import load, dump

def get_hs(text):
	titles = []
	soup = BeautifulSoup(text, "html.parser")
	titles = titles + soup.find_all("h1")
	titles = titles + soup.find_all("h2")
	titles = titles + soup.find_all("h3")
	titles = titles + soup.find_all("h4")
	titles = titles + soup.find_all("h5")
	return titles

def clear_tags(tags):
	return [t.text for t in tags]
def make_dic_titles(titles):
	dic_titles = {}
	i = 0
	for t in titles:
		dic_titles[i] = t
		i = i + 1
	return dic_titles

if __name__ == '__main__':
	f = open("e961024.htm", encoding = "utf-8")
	text = f.read()
	f.close()
	titles = get_hs(text)
	titles = clear_tags(titles)

	dic = make_dic_titles(titles)
	ftitlepk = open("titles.dat","wb")
	dump(dic,ftitlepk)
	ftitlepk.close()

	ftitles = open("titles.txt","w")
	for t in titles:
		ftitles.write(t)
	ftitles.close()
