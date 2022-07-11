# Importing ElementTree module
import xml.etree.ElementTree as ET

# Reading in movie xml file and assigning object to root
tree = ET.parse('movie.xml')
root = tree.getroot()

# elements list consists of all the tags in the XML document gotten from .iter() method
elements = [elem.tag for elem in root.iter()]

# using child_movie_tags function to go through each tag in elements
# list and find the child elements of the 'movie' tag in particular
# Since it's only necessary to print the child tags once, I've added another
# list so we can retrieve a range between the first 2 movie tags
# Reference: https://docs.python.org/3/library/xml.etree.elementtree.html
def child_movie_tags(elem_list):
    movie_pos = []
    for e in range(len(elem_list)):    
        if elem_list[e] == 'movie':
            movie_pos.append(e)
    return elements[movie_pos[0]+1:movie_pos[1]]

# using movie_desc to merely return each of the movie descriptions
# .join() and .itertext() methods called together in this context in order 
# to fetch the text value in between the description tag
# Reference #1: https://docs.python.org/3/library/xml.etree.elementtree.html
# Reference #2: https://www.datacamp.com/community/tutorials/python-xml-elementtree#comments
def movie_desc():
    descrip = ''
    for description in root.iter('description'):
        descrip += ''.join(description.itertext()) + '\n' + '\n'
    return descrip.strip()

# I noticed favorites attribute values were not consistent across the XML document
# format_correct() method simly reads in the XML doc, finds the favorite attrib,
# and standardizes the attrib value text
# FUnction returns a new root object to be used whereever it's called
# Reference: https://www.datacamp.com/community/tutorials/python-xml-elementtree#comments
def format_correct(rt):
    # Call the findall() function that will look for every instance of the movie tag
    for correct_format in rt.findall("./genre/decade/movie"):

        # Look for value of the favorite attribute
        favourite = correct_format.attrib["favorite"]

        if favourite.lower() == 'true':
            correct_format.set('favorite','True')
        else:
            correct_format.set('favorite','False')

    tree.write('movie.xml')

    new_tree = ET.parse('movie.xml')
    new_root = new_tree.getroot()
    return new_root

# favs() method calls the format_correct() and uses the find_all() method
# to count the favourites and non-favourites respectively
# Reference for findall() method: https://www.datacamp.com/community/tutorials/python-xml-elementtree#comments
def favs():
    favs = 0
    non_favs = 0
    new_root = format_correct(root)        
    for movie in new_root.findall("./genre/decade/movie/[@favorite='True']"):   
        favs += 1
    for movie in new_root.findall("./genre/decade/movie/[@favorite='False']"):   
        non_favs += 1

    return str(favs)  + ' movies are favourites and ' + str(non_favs) + ' movies are not favourites.'

# Print out the functions specified above to meet requirements of this task

print(child_movie_tags(elements))

print(movie_desc())

print(favs())
