# Importing spaCY library
import spacy

# Loading/specifying the English model for spaCY manipulation later on
nlp = spacy.load("en_core_web_sm")

# list created to store 5 examples of garden path sentences
gardenpathSentences = ["When Fred eats food gets thrown.","The dog that I had really loved bones.","Helen is expecting tomorrow to be a bad day.",
                       "That Jill is never here hurts.","The sour drink from the ocean."]

# Loop through each sentence in gardenpathSentences list                       
for token in gardenpathSentences:
    # Assigning string for spaCY manipulation
    token = nlp(token)
    # Printing out the tokenisation of all the sentences as they appear in the list
    print([token.orth_ for token in token])
    # Printing out the entity recognition of all the sentences as they appear in the list
    print([(i, i.label, i.label_) for i in token.ents])

'''
    I firstly expected more words to be categorised.
    The first strange entity categorisation was 'Helen', which was classified as a GPE: geo-political entity.
    I also found it strange that the phrase, 'a bad day' was classified as a DATE entity
'''
