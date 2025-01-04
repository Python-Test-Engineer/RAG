from flair.data import Sentence
from flair.models import EntityMentionLinker
from flair.nn import Classifier


# https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR.md - for more

# make a sentence
sentence = Sentence("I love Berlin .")

# load the NER tagger
tagger = Classifier.load("ner")

# run NER over sentence
tagger.predict(sentence)

# print the sentence with all annotations
print(sentence)

from flair.data import Sentence
from flair.nn import Classifier

# make a sentence
sentence = Sentence(
    "Behavioral abnormalities in the Fmr1 KO2 Mouse Model of Fragile X Syndrome"
)

# load biomedical NER tagger
tagger = Classifier.load("hunflair2")

# tag sentence
tagger.predict(sentence)



# make a sentence
sentence = Sentence(
    "Behavioral abnormalities in the Fmr1 KO2 Mouse Model of Fragile X Syndrome"
)

# load biomedical NER tagger + predict entities
tagger = Classifier.load("hunflair2")
tagger.predict(sentence)

# load gene linker and perform normalization
gene_linker = EntityMentionLinker.load("gene-linker")
gene_linker.predict(sentence)

# load disease linker and perform normalization
disease_linker = EntityMentionLinker.load("disease-linker")
disease_linker.predict(sentence)

# load species linker and perform normalization
species_linker = EntityMentionLinker.load("species-linker")
species_linker.predict(sentence)
