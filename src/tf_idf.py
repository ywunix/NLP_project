from keras.layers.embeddings import Embedding
from keras.preprocessing.text import Tokenizer

class TF_IDF(object):
    def __init__(self, words=None):
        self.words = words
	self.tokenizer = Tokenizer()

    def convert_word2index(self, text):
	tokenizer.fit_on_texts(text)
	tokens = tokenizer.texts_to_sequences(text)
	return tokens

if __name__ == "main":
    
