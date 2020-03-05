import spacy

def get_lemmas(tokens):
	tag_tokens = []
	nlp = spacy.load("es_core_news_sm")

	for token in tokens:
		doc = nlp(token)
		pos = doc[0].text, doc[0].pos_
		tag_tokens.append(pos)
	return tag_tokens

if __name__ == '__main__':
	ftext = open("clean_text.txt","r")
	text = ftext.read().split()
	ftext.close()

	fvocabulary = open("clean_vocabulary.txt","r")
	vocabulary = fvocabulary.read().split()
	fvocabulary.close()


	lem_text = get_lemmas(text)
	flemtext = open("lemmatizated_text.txt","w")
	for w in lem_text:
		flemtext.write(w[0]+ " "+ w[1] + "\n")
	flemtext.close()

	lem_voc = sorted(set(get_lemmas(vocabulary)))
	flemvoc = open("lemmatizated_voc.txt","w")
	for w in lem_voc:
		flemvoc.write(w[0]+ " "+ w[1]  + "\n")
	flemvoc.close()	