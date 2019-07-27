import spacy
import sys

nlp = spacy.load("en_core_web_sm")

doc = nlp("--text--")

for ent in doc.ents:
    print(ent.label_ + "---" +ent.text)