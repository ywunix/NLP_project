import requests
import string
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords

class Parser(object):
    def __init__(self, req):
        self.soup = BeautifulSoup(req.text, "lxml")

    def html_reformat(self):
        '''
        Extract words from html format
        '''
        soup = self.soup
        self.content = soup.get_text(separator='\n')

    def text_modify(self):
        # split into words
        tokens = word_tokenize(self.content.lower())
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        self.token_text = words

    def text_stem(self):
        # Stemming the words to root form
        from nltk.stem.porter import PorterStemmer
        porter = PorterStemmer()
        self.stem_text = [porter.stem(word) for word in self.token_text]

    def text_process(self):
        self.html_reformat()
        self.text_modify()
        self.text_stem()

    def get_text(self, text_type="stem"):
        if text_type == "html":
            return self.soup.prettify()
        elif text_type == "post_html":
            return self.content
        elif text_type == "token":
            return self.token_text
        elif text_type == "stem":
            return self.stem_text
        else:
            return None

if __name__ == "__main__":
    # url = "https://greatergood.berkeley.edu/article/item/how_to_become_a_friend_to_yourself?utm_source=pocket-newtab"
    url = "https://www.nytimes.com/2021/02/06/business/economy/housing-insecurity.html?action=click&module=Spotlight&pgtype=Homepage"
    req = requests.get(url)
    html_content = req.text
    parser = Parser(req)
    parser.text_process()
    text = parser.get_text('token')
    print(text)
