#An SMS Simulation

# 1. Email class as a template to create objects
class Email(object):
    # This is the class definition including all the variables specified
    # To note: has_been_read and is_spam are set to False
    def __init__(self,has_been_read,email_contents,is_spam,from_address):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
    # As per note above, the following two methods set the has_been_read and is_spam to True 
    def mark_as_read(self):
        self.has_been_read = True
        return

    def mark_as_spam(self):
        self.is_spam = True
        return
        
inbox = []        
# 2. Utility functions to operate on the list of objects
def add_email(has_been_read,email_contents,is_spam,from_address):
    email = Email(has_been_read,email_contents,is_spam,from_address)
    inbox.append(email)

# Emails are instantiated as new objects.    
add_email(False,'Data Science Bootcamp Registration',False,'admissions@hyperiondev.com')
add_email(False,'Data Science Bootcamp Funding',False,'students@hyperiondev.com')
add_email(False,'Buy some Dogecoin',False,'doge@crypto.com')
add_email(False,'Clicks ClubCard Exclusives!',False,'clubcard@clicks.co.za')
    
# get_count the number of items in the inbox
def get_count(): 
    return len(inbox)
            
# get_email accepts a user's input which will then be used as an index
# for which specific email in inbox will be shown
def get_email(user_input_index):
    inbox[user_input_index].mark_as_read()
    return inbox[user_input_index].email_contents

# get_unread_emails parses through each index in the inbox list
# and finds emails where the has_been_read attribute is set to False  
def get_unread_emails():
    unread = ''
    for i in inbox:
        if i.has_been_read == False:
            unread += i.email_contents + '\t'
        else:
            unread
    return unread.strip()

# Similar logic to get_unread_emails method above except it pulls through
# any emails marked as spam
def get_spam_emails():
    spam = ''
    for i in inbox:
        if i.is_spam:
            spam += i.email_contents + '\t'
        else:
            spam
    return spam.strip()
    
# delete simply uses the input index to find a specific email in the inbox list
# and deletes it from the inbox list
def delete(index):
    for i in range(len(inbox)):
        if inbox[i] == index:
            del inbox[i]                
      
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    # If user's choice is to read an email, a couple of things happen here:
    # 1. A list of unread emails is displayed
    # 2. The user enters a number for which email he/she'd like to read
    # 3. The email contents are shown and
    # 4. The chosen email is marked as read
    if user_choice == "read":
        for i in range(len(inbox)):
            print(get_unread_emails())
            email_choice = int(input("Enter which email index you'd like to read: "))
            chosen_email = get_email(email_choice)
            print(chosen_email + ' has been read')        
    # If user's choice is to mark an email as spam, a couple of things happen here:
    # 1. Each email is displayed in order
    # 2. The user enters whether he/she'd like to mark the email as spam
    # 3. If yes, the email is marked as spam
    # 4. The list of emails marked as spam should be shown
    elif user_choice == "mark spam":
        for i in range(len(inbox)):
            print(get_email(i))
            mark_spam = input("Would you like to mark this email as spam Y/N?")
            if mark_spam.upper() == "Y":
                inbox[i].mark_as_spam()
        print(get_spam_emails())
    # Send here simply requests the recipient's address and email content and displays a message that the email has been sent
    # I wasn't sure which of the functions above to call
    elif user_choice == "send":
        senders_address = ("Enter the recipients' address")
        content = ("Enter emails' content: ")
        add_email(False,content,False,senders_address)
        print("Email sent!")
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
