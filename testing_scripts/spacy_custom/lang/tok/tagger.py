# tagger.py  
from spacy.tokens import Token  
from spacy.language import Language  
from toki_pona_vocab import TOKI_PONA_VOCAB, TOKI_PONA_PUNCT  
  
# Register extension  
Token.set_extension('is_known', default=False)  
  
@Language.component('toki_pona_tagger')
def toki_pona_tagger(doc):  
    for token in doc:  
        text = token.text.lower()  
        if text in TOKI_PONA_VOCAB or text in TOKI_PONA_PUNCT:  
            token._.is_known = True  
        else:  
            token._.is_known = False  
    return doc  