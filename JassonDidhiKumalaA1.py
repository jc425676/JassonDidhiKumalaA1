"""
Name: Jasson Didhi Kumala
3 January 2017
This program will load a list of items from books
User can choose to check required books, completed books, add new books and mark a book as completed.
The program will end by saving all the current situation to book.csv.
https://github.com/jc425676/JassonDidhiKumalaA1
"""


from operator import itemgetter
FILENAME = "books.csv"
file_list = []
list_books = []

def count():#this function counts the number of books with the given criteria 'r'
    books = 0
    file = open("books.csv", "r")
    for x in range(0, len(file_list)):
        books += 1
    return books

def inputChoice(option): #this function is will check what the user enter for the options given
    option = option.upper()
    while option != "R" and option != "C" and option != "A" and option != "M" and option != "Q":
        print("Invalid Choice")
        print("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
        option = input(">>>")
        option.upper()
        return option



def main():#the main function will let the user enter the option
    read_file() #call function from read file
    while True:
        print("""Reading List 1.0 - by Jasson Didhi Kumala\n{} books loaded from books.csv""".format(len(file_list))) #display number of books from the csv file
        print("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
        option = input(">>>") #user input
        option = option.upper() #user input uppercase
        while option != "R" and option != "C" and option != "A" and option != "M" and option != "Q":
            print("Invalid Choice")
            print(
                "Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
            option = input(">>>")
            option.upper()
        if option == "R": #if optionrun  is equal to R function will run the function list_required_books
            list_required_books()
        if option == "C":#if optionrun  is equal to C function will run the function list_completed_books
            list_completed_books()
        if option == "A":#if optionrun  is equal to A function will run the function add_new_book
            add_new_book()
        if option == "M":#if optionrun  is equal to M function will run the function mark_a_book
            mark_a_book()
        if option== "Q":#if optionrun  is equal to Q it will quit the program and display total books on csv file
            print("{} books saved to books.csv".format(len(file_list)))
            print("Have a nice day!")
            file_write = open("books.csv", "w")
            for data in file_list:
                output = "{},{},{},{}".format(data[0], data[1], data[2], data[3]) +"\n"
                file_write.write(output)
            file_write.close()
            break


def list_required_books(): #this function will check the required books in the csv file
    page = 0 #declare the variable to count the totl page
    count = 0
    for index, data in enumerate(file_list):
        if data[3] =="r":#if the data in the list is r it will display the book
            print(index, "{:40s} by {:20s} {} pages".format(data[0], data[1], data[2]))
            page += int(data[2])
            count += 1
    print("Total pages for {} book(s): {} pages".format(count, page))



def list_completed_books(): #this function will check the completed books in the csv file
    page = 0
    count = 0
    for index, data in enumerate(file_list):
        if data[3] =="c":#if the data in the list is c it will display the book
            print(index, "{:40s} by {:20s} {} pages".format(data[0], data[1], data[2]))
            page += int(data[2])
            count += 1
    print("Total pages for {} book(s): {} pages".format(count, page))


def add_new_book(): #this function will add new books
    while True:
        title = input("Title: ")
        if len(title)<1:
            print("Input blank")
        else:
            break
    while True:
        author = input("Author: ")
        if len(author)<1:
            print("Input blank")
        else:
            break
    while True:
        try:
            page_number = int(input("Number of pages: "))
            if page_number < 0:
                print("Invalid page number")
            else:
                break
        except ValueError:
            print("Enter a valid page number")
    list_books.append(title)
    list_books.append(author)
    list_books.append(page_number)
    list_books.append("r")
    file_list.append(list_books)
    file_list.sort(key=itemgetter(1, 2))
    print("{} By {}, ({} Pages) added to the reading list.".format(title, author,page_number))



def mark_a_book(): #this function will mark books complete
    list_required_books()
    if count ==0:
        print("Required Books:\n No Books")
    else:
        print("Enter the number of a book to mark as completed ")
    while True:
        try:
            mark = int(input(">>>"))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    for index, each in enumerate(file_list):
        if index == mark:
            if each[3] == "r":
                each[3] = "c"
                print("{} by {} marked as completed".format(each[0], each[1]))
            else:
                print("That book is already completed")
            print("")


def read_file(): #this function reads the item in the csv file
    global file_list
    file_pointer= open(FILENAME, "r")
    for data in file_pointer.readlines():
        data = data.strip()
        datum = data.split(",")
        file_list.append(datum)
        file_list.sort(key=itemgetter(1,2))
    file_pointer.close()
    return file_list

main()
