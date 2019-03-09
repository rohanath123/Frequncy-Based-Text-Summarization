#TEXT SUMM ALGORITHM

import spacy 
from spacy.lang.en.stop_words import STOP_WORDS 
from heapq import nlargest

#BUILDING A LIST OF STOPWORDS

stopwords = list(STOP_WORDS)
punctuation = [".", ",", "$", "-", "--", "'", ";", ":", "(", ")", "!", "@", "#", "%", "^", "&", "*", "=", "+"]
#TEXT 
text = #ENTER YOUR OWN TEXT HERE 

nlp = spacy.load('en_core_web_lg')
doc = nlp(text)

tokens = [token.text for token in doc if token.text not in punctuation and token.text not in stopwords]
token_freq = {}

for word in tokens:
	if word not in token_freq.keys():
		token_freq[word] = 1
	else:
		token_freq[word] += 1

max_freq = max(token_freq.values())

for word in token_freq.keys():
	token_freq[word] = token_freq[word]/max_freq

sentences = [sentence for sentence in doc.sents]

sent_scores = {}

for sent in sentences:
	for word in sent:
		if word.text.lower() in token_freq.keys():
			if sent not in sent_scores.keys():
				sent_scores[sent] = 1
			else:
				sent_scores[sent] += 1


summ = nlargest(4, sent_scores, key=sent_scores.get) #CHANGE FIRST ARGUMENT TO ALTER NUMBER OF SENTENCES IN SUMMARY OUTPUT 
print(summ)
