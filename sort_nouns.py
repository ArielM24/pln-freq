import operator
import math

def get_freq(tups):
	nouns_freq = {}
	for n in tups:
		if n[0] not in nouns_freq:
			nouns_freq[n[0]] = 1
		nouns_freq[n[0]] = nouns_freq[n[0]] + 1
	return nouns_freq

def get_ifdt(dict_freq,k):
	tokens = dict_freq.keys()
	n = len(tokens)

	tf_idf = {}
	for token in tokens:
		x = dict_freq[token]
		tf_idf[token] = (((k + 1)*x)/(x+k))*math.log(n/x,2)

	return tf_idf

def print_file_tups(file, tups):
	f = open(file,"w")
	for t in tups:
		f.write(t[0]+" "+str(t[1])+"\n")
	f.close()

if __name__ == '__main__':
	fnouns = open("lemma_nouns.txt","r")
	nouns = []
	for line in fnouns:
		l = line.split()
		nouns.append((l[0],l[1]))
	fnouns.close()

	nouns_freq = get_freq(nouns)
	sorted_nouns = sorted(nouns_freq.items(), key=operator.itemgetter(1), reverse=True)
	print_file_tups("sorted_freq_nouns.txt",sorted_nouns)
	

	tf_idf = get_ifdt(nouns_freq,1.2)
	sorted_tf = sorted(tf_idf.items(),key=operator.itemgetter(1), reverse=True)
	print_file_tups("sorted_ifd.txt",sorted_tf)
