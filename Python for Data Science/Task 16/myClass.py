class Book(object):
        def __init__(book,isbn,author,publisher,pages,movietv):
                book.isbn = isbn
                book.author = author
                book.publisher = publisher
                book.pages = pages
                book.movietv = movietv
        
        def return_author(book):
                return book.author
        
        def is_movie(book):
                movietv = book.movietv
                if movietv == "N/A":
                        print("False")
                else:
                        print("True")
            
        def tough_read(book):
                no_pages = book.pages
                if no_pages > 500:
                        print("This is a tough read!")
                else:
                        print("This should be a breeze to read!")
            
            
            
asoiaf = Book("0553588486","George R.R. Martin","Bantam",835,"Game of Thrones")
shades = Book("0140244158","Marguerite Poland","The Penguin Group (SA) (Pty) Ltd",444,"N/A")
tournament = Book("1409147193","Matthew Reilly","Orion",432,"N/A")

books = [asoiaf,shades,tournament]

for b in books:
        b.return_author()
        b.is_movie()
        b.tough_read()
