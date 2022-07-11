class Student(object):

        def __init__(self, age, name, gender, grades):
                self.age = age
                self.name = name
                self.gender = gender
                self.grades = grades

        def compute_average(self):
                average = sum(self.grades)/len(self.grades)
                print("The average for student " + self.name + " is " + str(average))
        
        def check_male(self):
                stud_gender = self.gender
                if stud_gender == 'Male':
                        print("True")
                else:
                        print("False")


mike = Student(20, "Philani Sithole", "Male", [64,65])
sarah = Student(19, "Sarah Jones", "Female", [82,58])

# Add in your new objects and logic here, and above.
kenneth = Student(30, "Kenneth Ssekimpi", "Male",[88,62])

students = [mike,kenneth,sarah]

for s in students:
    s.compute_average()
    s.check_male()