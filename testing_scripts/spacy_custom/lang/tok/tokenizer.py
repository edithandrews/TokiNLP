import spacy
from spacy.tokens import Doc
import re
from spacy.tokenizer import Tokenizer

class TokiPonaTokenizer(Tokenizer):
    def __init__(self, vocab):
        # Initialize the base Tokenizer with the vocab  
        super().__init__(vocab) 

    def __call__(self, text):
        
        # Use regex to split text into words and punctuation  
        tokens = re.findall(r'\w+|[.,!?:;\'"]', text)  

        return Doc(self.vocab, words=tokens)

@spacy.registry.tokenizers("tokipona_tokenizer")
def create_tokipona_tokenizer():
    def create_tokenizer(nlp):
        return TokiPonaTokenizer(nlp.vocab)

    return create_tokenizer

# nlp = spacy.blank("en")
# nlp.tokenizer = TokiPonaTokenizer(nlp.vocab)
# doc = nlp("jan Susan anu jan Lisa li moku e suwi?")
# print([token.text for token in doc])

# nlp = spacy.load("en_core_web_sm")
# tokens = nlp("dog cat banana afskfsd")

# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)

# nlp_latin = spacy.load(r"C:\Users\eandrews\Personal\TP\spacy_testing\tok_spacy\nimi2vec-main\nimi2vec-main\models\tmp\tok_vectors")
# doc1 = nlp_latin("mi moku.")
# doc2 = nlp_latin("mi moku.")
# print(doc1.similarity(doc2))
