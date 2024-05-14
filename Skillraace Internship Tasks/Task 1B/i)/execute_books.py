from book_classes import Book, Ebook

def main():
    # Create an instance of Book
    B1 = Book()
    B1.set_title("Mahanayak")
    B1.set_author("Vishwas Patil")
    B1.set_publisher("Rajahans")
    B1.set_price(500)
    print("Title of the book is:", B1.get_title())
    print("Author of the book is:", B1.get_author())
    print("Publisher of the book is:", B1.get_publisher())
    print("Price of the book is:", B1.get_price())

    B1.set_copies(2000)
    print("Royalty of the book is:", B1.royalty_method())

    # Create an instance of Ebook
    EB1 = Ebook()
    EB1.set_title("Panipat")
    EB1.set_author("Vishwas Patil")
    EB1.set_publisher("Rajahans")
    EB1.set_price(500)
    EB1.set_format("PDF")
    print("Title of the book is:", EB1.get_title())
    print("Author of the book is:", EB1.get_author())
    print("Publisher of the book is:", EB1.get_publisher())
    print("Price of the book is:", EB1.get_price())
    print("Format of the book is:", EB1.get_format())

    EB1.set_copies(2000)
    print("Royalty of the ebook is:", EB1.royalty_method())

if __name__ == "__main__":
    main()
