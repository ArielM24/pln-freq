def filter(tups, pos):
	pass

if __name__ == '__main__':
	ftext = open("lemmatizated_text.txt","r")
	tups = []
	for line in ftext:
		t = line.split()
		tups.append((t[0],t[1]))
	ftext.close()