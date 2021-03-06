def filter(tups, pos):
	filtered = []
	for t in tups:
		if t[1] == pos:
			filtered.append(t)
	return filtered

if __name__ == '__main__':
	ftext = open("lemmatizated_text.txt","r")
	tups, aux = [], []
	for line in ftext:
		t = line.split()
		aux.append((t[0],t[1]))
	ftext.close()

	tups = filter(aux, "NOUN")
	tups = tups + filter(aux, "PROPN")

	fnouns = open("lemma_nouns.txt","w")
	for t in tups:
		fnouns.write(t[0] +" "+ t[1] +"\n")
	fnouns.close()