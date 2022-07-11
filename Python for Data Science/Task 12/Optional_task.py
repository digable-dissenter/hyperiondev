# Open two text files to read from
f = open('numbers1.txt', 'r')
g = open('numbers2.txt', 'r')

# Open text file to write to
ofile = open('allNumbers.txt','w')

# Instantiate list which accepts all the numbers from both numbers1 and numbers2
allNumbers = []

# Read each line in both text files, split string by whitespace and assign to row_delimiter
# Important to note in second for loop that we are adding to previous loop
for line in f:
    row_delimiter = line.split()
    for line in g:        
        row_delimiter = row_delimiter + line.split()

# Go through entire range of row_delimiter numbers (converted to int) and add to allNumbers        
for i in range(0,len(row_delimiter)):
    numbers = int(row_delimiter[i])    
    allNumbers.append(numbers)

# Sort through list      
# Reference: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-42.php  
allNumbers.sort()
    
# For each number, write to file now that numbers are sorted
for line in allNumbers:
    ofile.write(str(line) + "\n")

# Close all files
f.close()
g.close()
ofile.close()
