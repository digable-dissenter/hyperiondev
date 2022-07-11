# Retrieving SQLite3 DB module
import sqlite3

# Assigning variables to be inserted into the python_programming table
id1 = 55
id2 = 66
id3 = 77
id4 = 12
id5 = 2

name1 = 'Carl Davis'
name2 = 'Dennis Fredrickson'
name3 = 'Jane Richards'
name4 = 'Peyton Sawyer'
name5 = 'Lucas Brooke'

grade1 = 61
grade2 = 88
grade3 = 78
grade4 = 45
grade5 = 99

try:
    # Creates or opens a file called student_db with a SQLite3 DB
    db = sqlite3.connect('student_db')
    # Get a cursor object
    cursor = db.cursor()
    # Check if table python_programming does not exist and create it
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
        python_programming(id INTEGER PRIMARY KEY, name TEXT,
        grade INTEGER)''')  
    print('Users inserted')   

    # Because we are inserting several students, we create a list with tuples
    # The tuples consist of the variables declared above
    python_students = [(id1,name1,grade1),(id2,name2,grade2),(id3,name3,grade3),(id4,name4,grade4),(id5,name5,grade5)]
    # Invoke executemany() function and    
    cursor.executemany( '''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', python_students)

    # Select all records with a grade between 60 and 80.
    first_grade = 60
    second_grade = 80
    cursor.execute( '''SELECT * FROM python_programming WHERE grade >=? AND grade <=?''', (first_grade,second_grade))
    student = cursor.fetchall()
    print('Data retrieved about students with a grade between 60 and 80')
    print(student)

    # Change Carl Davis’s grade to 65.
    grade = 65
    name = 'Carl Davis'
    cursor.execute( '''UPDATE python_programming SET grade = ? WHERE name = ? ''' , (grade,name))
    print('Carl Davis’s grade updated to 65.')

    # Delete Dennis Fredrickson’s row.
    name = 'Dennis Fredrickson'
    cursor.execute( '''DELETE FROM python_programming WHERE name = ? ''' , (name,))
    print('Dennis Fredrickson’s record has been deleted.')

    # Change the grade of all students with an id below than 55.
    grade = 75
    cursor.execute('''SELECT * FROM python_programming WHERE id < 55''')
    # Loop through each cursor object and update students' grades
    for row in cursor:
        cursor.execute( '''UPDATE python_programming SET grade = ? WHERE id < 55 ''' , (grade,))
    print('Students with an id below than 55''s grades have been updated.')

    # This select is purely to show that changes above have been applied
    cursor.execute('''SELECT * FROM python_programming''')
    student = cursor.fetchall()
    print(student)
    # Commit all the changes made
    db.commit()    
# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e 
finally:
    # Optional, dropping python_programming table from student_db
    cursor.execute( '''DROP TABLE python_programming''' )
    # Close the db connection
    db.close()    
    print('Connection to database closed')
