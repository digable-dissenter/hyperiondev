import sqlite3
import json
import PyInquirer

def populate_db(filename):
    '''
        This function dumps the contents of the books .json file and creates
        a table named books ready for usage, granted the contents of the .json file
        are correct.

        Parameters: .json filename
    '''
    # Opening, saving, and closing the .json file and saving its contents as data
    with open(filename, "r") as j:
        json_data = json.load(j)

    # Setting db and cursor as global variables to be used throughout
    # the script without redefining every time.
    global db
    global cursor
    
    # Creating db file
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()

    # Creating table named books with columns as seen below
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
            "id" INTEGER PRIMARY KEY,
            "Title" TEXT,
            "Author" TEXT,
            "Qty" INTEGER)''')
    db.commit()

    # Parsing through json_data variable (which contains contents from books.json file) 
    # and dumping data into matching columns
    for child in json_data:
        cursor.execute('''
                INSERT OR REPLACE INTO books                
                VALUES (?,?,?,?)''',
                (child['id'], child['Title'],
                 child['Author'], child['Qty'], ))
        db.commit()

def main():
    '''
        The main function calls the books.json file and displays the table results
        to the user; thereafter, presenting the user with options on how they'd
        like to proceed.
        
    '''
    # Call populate_db() function with books.json filename
    filename = 'books.json'
    populate_db(filename)

    # Sorting by primary key and returning all books from database
    cursor.execute('''SELECT * FROM books ORDER BY id''')
    db.commit()
    book_rows = cursor.fetchall()

    # Call format_books() function to display results in a more legible way
    books_table = format_books(cursor, book_rows, 1)
    print(books_table)

    # User presented with options on how to proceed
    user_options()

def exit():
    '''
        The exit() function is invoked when the user chooses to leave the program by
        terminating the process and closing the database.
        i.e. drops the books table and closes the database connection
    '''
    print('Goodbye!')

    cursor.execute('''DROP TABLE books''')
    db.commit()
    db.close()
    print('Connection to database closed')

    quit()

def format_books(cursor, data=None, rowlens=0):
    '''
        The format_book() function presents the books table data in a legible way.
        It is called whenever any output needs to be displayed with appropriate column
        widths.      
        Reference: (Holden,2021)
        Link: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch08s11.html

        Parameters: cursor, data, rowlens
        cursor description attribute used for appropriate headings and column widths based on table output rows
        data determines column lengths
        rowlens applies the tabbed formatting structure based on the previous two arguments
    '''
    d = cursor.description

    # In this instance, there'd be no results
    # i.e. table from query result is empty
    if not d:
        return

    names = []
    lengths = []
    rules = []

    if not data:
        data = cursor.fetchall()

    # iterate over description    
    for dd in d:
        l = dd[1]
        if not l:
            # or default arg ...
            l = 12
        # Handle long names
        l = max(l, len(dd[0]))
        names.append(dd[0])
        lengths.append(l)

    for col in range(len(lengths)):
        if rowlens:
            rls = [len(str(row[col])) for row in data if row[col]]
            lengths[col] = max([lengths[col]] + rls)
        rules.append('-' * lengths[col])

    # format is a variable of concatenated dashes applied underneath headers
    # that is the length of the longest value in the column (for each column)
    format = ' '.join(['%%-%ss' % l for l in lengths])
    # result outputs the appropriate headings, columns, and rows of the table
    # dataset in legible way
    result = [format % tuple(names)]
    result.append(format % tuple(rules))
    for row in data:
        result.append(format % row)
    return '\n'.join(result)

def user_options():
    '''
        Once the user has the .db file set, this function then presents the user with a set of options, 
        each with its own sub options except for the exit function.        
    '''
    question = {

            'type': 'list',
            'name': 'user_choice',
            'message': 'What would you like to do?',
            'choices': ['Add book', 'Update book', 'Delete book', 'Search book', 'Exit']
        }

    global user_choice
    user_choice = PyInquirer.prompt(question)['user_choice']
        
    user_menu()

def user_menu():
    '''
        This function consists of a loop and within it conditional statements
        which direct the user to sub menus (functions of the main menu based on
        user input). If the user enters exit instead of choosing one of the other
        options the loop breaks. The database will close and the window will
        terminate
    '''
    while user_choice != 'Exit':
        if user_choice == None:
            pass
        if user_choice == 'Add book':
            add_book()
            user_options()            
        elif user_choice == 'Update book':
            update_options()
            user_options() 
        elif user_choice == 'Delete book':
            delete_options()
            user_options() 
        elif user_choice == 'Search book':
            search_options()
            user_options() 
        elif user_choice == 'Exit':
            exit()

def add_book():
    '''
        Sub function of the user_menu() add book option.
        This function spawns a multi-enterbox interface where new book details
        can be entered which then gets added to the database.

        I used the PyInquirer library to generate the command line user interface throughout
        the project to minimise input mistakes as much as possible.
        Reference: (CITGuru, 2018)
        Link: https://github.com/CITGuru/PyInquirer
    '''
    print('Enter new book information:\n')    

    # For each of the below input interfaces, validation is
    # applied after input user. The title and author inputs
    # validate length and the Qty validates that input is numeric
    title_add = [
            {
                'type': 'input',
                'name': 'title',
                'message': 'Book title:',
                'validate': lambda val: True if len(val)
                else 'Book title should be not be empty'
            }
        ]
    author_add = [
            {
                'type': 'input',
                'name': 'author',
                'message': 'Book author:',
                'validate': lambda val: True if len(val)
                else 'Book author should be not be empty'
            }
        ]
    qty_add = [
            {
                'type': 'input',
                'name': 'qty',
                'message': 'Book quantity:',
                'validate': lambda val: True if val.isdigit()
                else 'Book quantity should be numeric only'
            }
        ]
    # In order to eliminate duplicate entries of IDs being entered, this is auto-generated
    # so user doesn't have to supply the book ID
    id_new = cursor.execute('''SELECT MAX(id) + 1 FROM books''').fetchone()
    id_new = int(str(id_new).replace('(', '').replace(')', '').replace(',', ''))
        
    title_new = PyInquirer.prompt(title_add)['title']
    author_new = PyInquirer.prompt(author_add)['author']
    qty_new = PyInquirer.prompt(qty_add)['qty']

    # Unique book entries are inserted into books table
    cursor.execute('''SELECT * from books WHERE Title =? AND Author=?''',
                    (title_new,author_new,)) 
    result = cursor.fetchall()
    if result:
        print('Book already exists. Add another book.')            
    else:
        cursor.execute('''INSERT OR REPLACE INTO books(id,Title,Author,Qty)
            VALUES(?,?,?,?)''', (id_new, title_new, author_new, qty_new))
        db.commit()
        print('New book ' + '"' + title_new + '"' + ' by ' + author_new + ' has been added.')    

def update_options():
    '''
        This functions serves as a sub menu of the user menu -> Update book
        option. It prompts the user with 2 options:
            Update book title
            Update book author
            Update book quantity
    '''
    
    print('Update book information:\n')

    update_choice = {

            'type': 'list',
            'name': 'update_choice',
            'message': 'Choose an option:',
            'choices': ['Update title', 'Update author', 'Update quantity']
        }
    
    update_answer = PyInquirer.prompt(update_choice)['update_choice']

    if update_answer == None:
        pass
    elif update_answer == 'Update title':
        update_title()
    elif update_answer == 'Update author':
        update_author()
    elif update_answer == 'Update quantity':
        update_quantity()

def update_title():
    '''
        This function prompts the user to enter the old book title which is to be updated.
        It then updates the books table with the updated title accordingly.
    '''
    print('Fill in the fields\nTitle editor\n')

    # Instead of the user typing out the book's title, went with approach of presenting
    # the list of titles to the user from which user can select as input    
    title_list = []
    title_result = cursor.execute('''SELECT Title FROM books ORDER BY Title''').fetchall()
    for row in title_result:
        title_list.append(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace('"', ''))

    old_title = {

            'type': 'list',
            'name': 'old_title',
            'message': 'Choose book title:',
            'choices': title_list
        }

    new_title = [
            {
                'type': 'input',
                'name': 'new_title',
                'message': 'New book title:',
                'validate': lambda val: True if len(val)
                else 'New book title should be not be empty'
            }
        ]

    title_old = PyInquirer.prompt(old_title)['old_title']
    title_new = PyInquirer.prompt(new_title)['new_title']

    # If old and new titles are different, save in books table
    if title_new != old_title:
        cursor.execute('''UPDATE books SET Title =? WHERE Title =?''',
                        (title_new, title_old))
        db.commit()
        print('"' + title_old + '"' + ' has been updated to ' + '"' + title_new + '"')
    else:
        print('You haven''t updated the book''s title.\n Please consider doing so.')

def update_author():
    '''
        This function prompts the user to enter the book author which is to be updated.
        It then updates the books table with the updated author name accordingly.
    '''
    print('Fill in the fields\nAuthor editor\n')

    # Instead of the user typing out the book's author, went with approach of presenting
    # the list of author to the user from which user can select as input    
    author_list = []
    author_result = cursor.execute('''SELECT Author FROM books ORDER BY Author''').fetchall()
    for row in author_result:
        author_list.append(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace('"', ''))

    old_author = {

            'type': 'list',
            'name': 'old_author',
            'message': 'Choose book author:',
            'choices': author_list
        }

    new_author = [
            {
                'type': 'input',
                'name': 'new_author',
                'message': 'New book author:',
                'validate': lambda val: True if len(val)
                else 'New book author should be not be empty'
            }
        ]

    author_old = PyInquirer.prompt(old_author)['old_author']
    author_new = PyInquirer.prompt(new_author)['new_author']

    # If previous and new authors are different, save in books table
    if author_new != author_old:
        cursor.execute('''UPDATE books SET Author =? WHERE Author =?''',
                        (author_new, author_old))
        db.commit()
        print('"' + author_old + '"' + ' has been updated to ' + '"' + author_new + '"')
    else:
        print('You haven''t updated the book''s author.\nPlease consider doing so.')

def update_quantity():
    '''
        This function is a sub function of the update menu. 
        This function prompts the user to enter the book's author and title 
        which is to be updated. It then updates the books table with the
        updated quantity accordingly.
    '''
    print('Fill in the fields\nQuantity editor\n')

    author_list = []
    title_list = []
    
    # Instead of the user typing out the book's title, went with approach of presenting
    # the list of titles to the user from which user can select as input    
    author_result = cursor.execute('''SELECT DISTINCT Author FROM books ORDER BY Author''').fetchall()
    for row in author_result:
        author_list.append(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace('"', ''))
        
    author = {

            'type': 'list',
            'name': 'author',
            'message': 'Choose book author:',
            'choices': author_list
        }
    
    author_choice = PyInquirer.prompt(author)['author']
    # Instead of the user typing out the book's title, went with approach of presenting
    # the list of titles to the user from which user can select as input
    # This is a filtered list of titles based on the previous selection of the authors in the
    # books table
    title_result = cursor.execute('''SELECT Title FROM books WHERE Author =? ORDER BY Title''',
                        (author_choice,)).fetchall()    
    for row in title_result:
        title_list.append(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace('"', ''))
        
    title = {

            'type': 'list',
            'name': 'title',
            'message': 'Choose book title:',
            'choices': title_list
        }
     
    new_qty = [
            {
                'type': 'input',
                'name': 'new_qty',
                'message': 'New book quantity:',
                'validate': lambda val: True if val.isdigit()
                else 'Book quantity should be numeric only'
            }
        ]
        
      
    title_choice = PyInquirer.prompt(title)['title']
    qty_new = PyInquirer.prompt(new_qty)['new_qty']
    
    cursor.execute('''UPDATE books SET Qty =? WHERE Title =? AND Author =?''', (qty_new, title_choice, author_choice))
    db.commit()
    print('"' + title_choice + '"' + ' by ' + author_choice + 's quantity has been updated to ' + str(qty_new) + '.')
 
def delete_options():
    '''
        This functions serves as a sub menu of the user menu -> Delete book
        option. It prompts the user with 2 options:
            Delete by book title
            Delete all books from author
    '''
    print('Delete Menu:\n')
    
    delete_choice = {

            'type': 'list',
            'name': 'delete_choice',
            'message': 'Choose an option:',
            'choices': ['Delete by book title','Delete all books from author']
        }

    delete_answer = PyInquirer.prompt(delete_choice)['delete_choice']

    # Conditional statement which will call the appropriate function based
    # on user input/choice.
    if delete_answer == None:
        pass
    elif delete_answer == 'Delete by book title':
        delete_title()
    elif delete_answer == 'Delete all books from author':
        delete_author()

def delete_title():
    '''
        This function is a sub function of the delete menu. This is where
        the removal of the database entry/s occur/s based on (book title) user input
    '''
    print('Fill in the fields\nTitle editor\n')

    # Instead of the user typing out the book's title, went with approach of presenting
    # the list of titles to the user from which user can select as input
    title_list = []
    title_result = cursor.execute('''SELECT DISTINCT Title FROM books ORDER BY Title''').fetchall()
    for row in title_result:
        title_list.append(str(row).replace('(','').replace(')','').replace(',','').replace("'","").replace('"',''))
    
    title_choice = {

            'type': 'list',
            'name': 'title_choice',
            'message': 'Choose book title:',
            'choices': title_list
        }

    title_delete = PyInquirer.prompt(title_choice)['title_choice']

    # Delete book data from applicable title
    cursor.execute('''DELETE FROM books WHERE Title =?''',
                   (title_delete,))
    db.commit()
    print('"' + title_delete + '"' + ' has been deleted.')

def delete_author():
    '''
        This function is a sub function of the delete menu. This is where
        the removal of the database entry/s occur/s based on (book author) user input
    '''

    print('Fill in the fields\nAuthor editor\n')

    # Instead of the user typing out the book's author, went with approach of presenting
    # the list of authors to the user from which user can select as input
    author_list = []
    author_result = cursor.execute('''SELECT DISTINCT Author FROM books ORDER BY Author''').fetchall()
    for row in author_result:
        author_list.append(str(row).replace('(','').replace(')','').replace(',','').replace("'","").replace('"',''))

    author_choice = {

            'type': 'list',
            'name': 'author_choice',
            'message': 'Choose book author:',
            'choices': author_list
        }
   
    author_delete = PyInquirer.prompt(author_choice)['author_choice']
    
    # Delete book data from applicable author
    cursor.execute('''DELETE FROM books WHERE Author =?''',
                   (author_delete,))
    db.commit()
    print('All books by ' + author_delete + ' have been deleted.')

def search_options():
    '''
        This functions serves as a sub menu of the user menu -> Search book
        option. It prompts the user with 2 options:
            Search book by its author
            Search only for books which are low on stock
    '''

    print('Search Menu\n')

    search_choice = {

            'type': 'list',
            'name': 'search_choice',
            'message': 'Choose an option:',
            'choices': ['Search all','Search by author','Low stock checker']
        }

    search_answer = PyInquirer.prompt(search_choice)['search_choice']

    # Conditional statement which will call the appropriate function based
    # on user input/choice.
    if search_answer == None:
        pass
    elif search_answer == 'Search all':
        search_all()
    elif search_answer == 'Search by author':
        search_author()
    elif search_answer == 'Low stock checker':
        search_low_volume()
    
def search_all():
    cursor.execute('''SELECT DISTINCT * FROM books ORDER BY id''')
    db.commit()
    book_rows = cursor.fetchall()
    books_table = format_books(cursor,book_rows,1)
    print(books_table)
    
def search_author():
    '''
        This function is a sub function of the search book menu. This is where
        the retrieval of the database entry/s occurs based on user input (book author)
    '''
    # Instead of the user typing out the book's author, went with approach of presenting
    # the list of authors to the user from which user can select as input
    author_list = []
    author_result = cursor.execute('''SELECT DISTINCT Author FROM books ORDER BY Author''').fetchall()
    for row in author_result:
        author_list.append(str(row).replace('(','').replace(')','').replace(',','').replace("'","").replace('"',''))
        
    author = {

            'type': 'list',
            'name': 'author',
            'message': 'Choose book author:',
            'choices': author_list
        }

    author_search = PyInquirer.prompt(author)['author']
   
    # Add updated book data quantity to database
    cursor.execute('''SELECT * FROM books WHERE Author =?''',
                   (author_search,))
    db.commit()
    book_rows = cursor.fetchall()
    books_table = format_books(cursor, book_rows, 1)
    print('Books by ' + author_search + ':\n')
    print(books_table)

def search_low_volume():
    '''
        This functions checks the database for any books that have a stock/quantity
        level of less than 10 and displays it to the user.
    '''
    # low_mark variable is the quantity to be checked for against database quantities
    low_stock_mark = 10
    # Return database entry/s to user based on low_mark
    cursor.execute('''SELECT * FROM books WHERE Qty <?''',
                   (low_stock_mark,))
    db.commit()
    book_rows = cursor.fetchall()
    books_table = format_books(cursor, book_rows, 1)
    print('\nBooks with low stock:\n')
    print(books_table)
    

try:
    # main() function invoked which is the root of the program
    if __name__ == '__main__':
        main()
# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    exit()
