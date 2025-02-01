import spacy  
from spacy import displacy  
  
# Load your trained model  
nlp = spacy.load("./output/model-best")  
  
# Sample Toki Pona text  
# text = "akesi pi mije Mawen li utala e ijo ni."
text = "mi toki pona"  
  
# Process the text  
doc = nlp(text)  
  
# ==============================  
# Testing the Tokenizer  
# ==============================  
print("=== Tokens ===")  
for token in doc:  
    print(f"Token: {token.text}")  
  
# ==============================  
# Testing the Token Vectors (tok2vec)  
# ==============================  
print("\n=== Token Vectors (tok2vec) ===")  
for token in doc:  
    print(f"Token: {token.text}")  
    print(f"Vector (shape {token.vector.shape}): {token.vector}")  
    print("-" * 40)  
  
# ==============================  
# Testing the POS Tagger  
# ==============================  
print("\n=== Part-of-Speech Tags ===")  
for token in doc:  
    print(f"Token: {token.text}\tPOS: {token.pos_}\tTag: {token.tag_}")  
  
# ==============================  
# Testing the Dependency Parser  
# ==============================  
print("\n=== Dependency Parse ===")  
for token in doc:  
    print(f"Token: {token.text}\tDep: {token.dep_}\tHead: {token.head.text}")  
  
# ==============================  
# Testing the Entity Ruler  
# ==============================  
print("\n=== Named Entities ===")  
if doc.ents:  
    for ent in doc.ents:  
        print(f"Entity: {ent.text}\tLabel: {ent.label_}")  
else:  
    print("No named entities found.")  
  
# ==============================  
# Generating Dependency Tree Visualization  
# ==============================  
# Set options for the visualization  
options = {  
    "compact": True,  
    "bg": "#ffffff",  
    "color": "#000000",  
    "font": "Source Sans Pro"  
}  
  
# Render the dependency parse and save it as an SVG file  
svg = displacy.render(doc, style='dep', options=options, jupyter=False)  
output_path = "dependency_tree.svg"  
with open(output_path, "w", encoding="utf-8") as f:  
    f.write(svg)  
  
print(f"\nDependency tree visualization saved as '{output_path}'.")