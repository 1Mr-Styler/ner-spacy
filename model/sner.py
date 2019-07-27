import spacy
import sys

nlp = spacy.load("en_core_web_sm")

doc = nlp("All i like Jerry is for USD1000 or MYR2000 on 12/07/2019 at Google Inc in Kuala Lumpur")

for ent in doc.ents:
    print(ent.label_ + "---" +ent.text)