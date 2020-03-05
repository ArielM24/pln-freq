import nltk
from bs4 import BeautifulSoup

def erase_sym(str, sym):
	strings = []
	aux = []
	added = False
	for symbol in sym:
		f = str.find(symbol)
		if f > -1:
			strings = strings + str.split(symbol)
			added = True
			for s in strings:
				aux = aux + erase_sym(s,sym)
			return aux

	if not added:
		strings.append(str)

	return strings

def erase_size(str,size):
	aux = []
	for s in str:
		if len(s) > size:
			aux.append(s)
	return aux

def get_clean_text(name):
	f = open("e961024.htm", encoding = "utf-8")
	text = f.read()
	f.close()

	soup = BeautifulSoup(text,"lxml")
	words = soup.get_text()

	return words

def clean_words(words, file):
	fsw = open(file,"r")
	stop_words = fsw.read()
	fsw.close()	
	clean_words = []
	for w in words:
		if w not in stop_words:
			clean_words.append(w)
	return clean_words

def get_vocabulary(words, lower = True):
	vocabulary = sorted(set(words))
	if lower:
		vocabulary = [w.lower() for w in vocabulary]
		return sorted(set(vocabulary))
	else:
		return vocabulary

def clean_chars(words, chars, size = 1):
	clean_words = []
	for w in words:
		clean_words = clean_words + erase_size(erase_sym(w, chars), size)
	return clean_words

if __name__ == '__main__':
	words = get_clean_text("e961024.htm")
	tokens_nltk = nltk.word_tokenize(words)

	text = clean_words(tokens_nltk,"spanish_stop_words.txt")
	text = clean_words(text,"spanish_punctuation_signs.txt")

	sym = ["-","/","'","*","?","¿","!","¡",".",",",";",":","¦","#","&","%","$","(",")","=","_","[","]","{","}","~","+","—","\\"]
	num = ["0","1","2","3","4","5","6","7","8","9"]

	text = clean_chars(text, sym + num,size=2)
	vocabulary = get_vocabulary(text)

	print(len(text), len(vocabulary))

	ft = open("clean_text.txt","w")
	for word in text:
		ft.write(word + "\n")
	ft.close()

	fv = open("clean_vocabulary.txt","w")
	for word in vocabulary:
		fv.write(word + "\n")
	fv.close()
