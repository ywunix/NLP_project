from keras.layers.embeddings import Embedding
from keras.preprocessing.text import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

class TF_IDF(object):
    def __init__(self, words=None, vocab_size=100000):
        self.words = words
        self.vocab_size = vocab_size
        self.tokenizer = Tokenizer()

    def convert_word2index(self, text_tokens):
        self.tokenizer.fit_on_texts(text_tokens)
        index_tokens = self.tokenizer.texts_to_sequences(text_tokens)
        self.index_rep = index_tokens
        return index_tokens
    '''
    def get_embedding(self, dimension=32):
        if not self.index_rep:
            return None

        embedding = Embedding(self.vocab_size, dimension)(self.index_rep)
        return embedding
    '''

if __name__ == "__main__":
    sample_text = "Convolutional Neural Networks are very similar to ordinary Neural Networks " \
                  "from the previous chapter: they are made up of neurons that have learnable " \
                  "weights and biases. Each neuron receives some inputs, performs a dot product " \
                  "and optionally follows it with a non-linearity."
    text_tokens = sample_text.split()
    tfidf = TF_IDF()
    tokens = tfidf.convert_word2index(text_tokens)
    print(tokens)
    print(tfidf.tokenizer.word_index)

    count_vectorizer = TfidfVectorizer(ngram_range=(1,1), max_df=0.65,
                        tokenizer=nltk.word_tokenize,
                        strip_accents='unicode',
                        lowercase =True, analyzer='word', token_pattern=r'\w+',
                        use_idf=True, smooth_idf=True, sublinear_tf=False, 
                        stop_words = 'english')
    bag_of_words = count_vectorizer.fit_transform(text_tokens)
    print(bag_of_words)

