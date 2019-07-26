import spacy
import sys

nlp = spacy.load("en_core_web_sm")

doc = nlp(sys.argv[1])

for ent in doc.ents:
    print(ent.label_, ent.text)