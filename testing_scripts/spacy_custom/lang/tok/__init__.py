from spacy.language import Language  
from tokenizer import TokiPonaTokenizer  
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
from stop_words import STOP_WORDS
from ner_pattern import ENTITY_PATTERNS
from spacy.pipeline import EntityRuler  
import spacy 
  
class TokiPonaDefaults(Language.Defaults):  
    tokenizer_exceptions = BASE_EXCEPTIONS  
    stop_words = set(STOP_WORDS)
  
@spacy.registry.languages("tok")
class TokiPona(Language):  
    lang = 'tok'  
    Defaults = TokiPonaDefaults
    # default_config = "Path/To/Defatult_Config/After TRaining"
  
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)  
        self.tokenizer = TokiPonaTokenizer(self.vocab)

        # Add EntityRuler to the pipeline  
        ruler = self.add_pipe("entity_ruler", last=True)  
        ruler.add_patterns(ENTITY_PATTERNS)

# nlp = TokiPona()  
  
# # Sample text  
# text = "ni li jan Pona mi. nimi ona li jan Sina."  

# # Process the text  
# doc = nlp(text)  

# # Print tokens  
# print("Tokens:")  
# for token in doc:  
#     print(f"'{token.text}'", end=', ')  
# print()  

# # Print named entities  
# print("\nNamed Entities:")  
# for ent in doc.ents:  
#     print(f"Entity: {ent.text}, Label: {ent.label_}")  



