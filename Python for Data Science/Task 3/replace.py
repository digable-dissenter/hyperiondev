# Assuming that the output required is from last character through to first character
long_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
long_sentence = long_sentence.replace("!"," ")
long_sentence = long_sentence.upper()
# Extra argument is used when slicing string backwards
# Source: https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python 
long_sentence1 = long_sentence[:: -1]
print (long_sentence1)
