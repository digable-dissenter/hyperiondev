# Importing spaCY library
import spacy

# Specifying which spaCY model to load
nlp = spacy.load('en_core_web_md')

# Assigning the description of Planet Hulk to a string which will be compared
# to each of the movies in the movies.txt file 
planet_hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
planet_hulk = nlp(planet_hulk)

# Reading from movies.txt file
f = open('movies.txt', 'r')
# movies_desc list will contain all the movies contained in the movies.txt file
movies_desc = []
# Appending the movies_desc list with each movie in the movies.txt file
movies_desc = f.readlines()

def return_movie(md):
    # Instantiating each variable for comparison later on
    movie = ""
    score = 0 
    movie_count = 0
    # movies_sim_score list will contain the similarity scores for each as compared to Planet Hulk
    movies_sim_score = []
    # We will now compare the similarity of the movie descriptions to ascertain spaCy's similarity to Planet Hulk
    # We'll also store each similarity score in the movies_sim_score list
    for token in md:
        token = nlp(token)
        movies_sim_score.append(token.similarity(planet_hulk))
        # Now, we'll compare each score from the movies.txt file to determine which has 
        # the most similarity to Planet Hulk
        if movies_sim_score[movie_count] > score:
            score = movies_sim_score[movie_count]
            movie = movies_desc[movie_count]
        else:
            score
            movie
        movie_count += 1
    # Display output
    print(movie[0:7] + ' is the most similar movie to Planet Hulk')

# Call return_movie function 
return_movie(movies_desc)

