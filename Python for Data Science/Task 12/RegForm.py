# Open file to write to
# Request user input for number of students
ofile = open('RegForm.txt','w')
nr_students = int(input("How many students will be registering? \n"))

# Range takes into account actual number of students for each ID number to be entered
for i in range (1, nr_students+1):
    id_number = int(input("Please enter your ID number: "))
    ofile.write("Student " + str(i) + " ID number: " + str(id_number) + "\n" )
    
ofile.close()
