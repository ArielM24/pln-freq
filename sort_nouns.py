import operator

if __name__ == '__main__':
	fnouns = open("lemma_nouns.txt","r")
	nouns = []
	for line in fnouns:
		l = line.split()
		nouns.append((l[0],l[1]))
	fnouns.close()

	nouns_freq = {}
	for n in nouns:
		if n[0] not in nouns_freq:
			nouns_freq[n[0]] = 1
		nouns_freq[n[0]] = nouns_freq[n[0]] + 1

	sorted_nouns = sorted(nouns_freq.items(), key=operator.itemgetter(1), reverse=True)
	
	fsorted = open("sorted_nouns.txt","w")
	for n in sorted_nouns:
		fsorted.write(n[0]+" "+str(n[1])+"\n")
	fsorted.close()