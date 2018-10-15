from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "Helo My name is aashir and i lives in multan, pkistan "

stop_words = set(stopwords.words("english"))

words =word_tokenize(example)

filtered_sentence = []

#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)

#filtered_sentence = [w for w in words if not w in stop_words ]

filtered_sentence = [w for w in words if not w.lower() in stop_words ]
print(filtered_sentence)
