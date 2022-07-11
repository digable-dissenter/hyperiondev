# Importing spaCY library
import spacy
# Specifying/loading model to work with
nlp = spacy.load("en_core_web_md")

# Assigning words for later comparison
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Displaying similarity score as outputs
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Similar to above, except all words constitute one string
tokens = nlp('cat apple monkey banana')

# Looping for string twice to compare each word to another and display similarity
# score
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''
    Cat and monkey have a similarity score above 0.5, presumably because both
    are animals
    Similarly, both fruits, apple and banana have a a score above 0.5
    Monkey and banana have a moderate score of 0.45, indicating some association
    Cat and either fruit yields low scores (about 0.28), indicating almost
    no association
'''


'''
    Error message appears when simpler language model ‘en_core_web_sm’ ('en' no
    longer used from spaCY 3.0).
    The error message has to do with the fact the ‘en_core_web_sm’ model can't
    deal with loaded word vectors, hence comprimising the judgments. Context-sensitive
    tensors are instead used.
    The similarities are completely different from using the ‘en_core_web_md’ model
    For instance, apple-monkey comparison yields a 0.2929498 in ‘en_core_web_md’ model
    whereas in ‘en_core_web_sm’, same comparison yields 0.68913907
'''
# Own example
tokens = nlp('school university bootcamp')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
