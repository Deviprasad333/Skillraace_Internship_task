class Book:
    def __init__(self, title="", author="", publisher="", price=0, copies=0):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.copies = copies
        self.royalty = 0

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_price(self, price):
        self.price = price

    def set_copies(self, copies):
        self.copies = copies

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_price(self):
        return self.price

    def royalty_method(self):
        if self.copies <= 500:
            self.royalty = 0.1 * self.price * self.copies
        elif 500 < self.copies <= 1500:
            self.royalty = 0.1 * self.price * 500 + 0.125 * self.price * (self.copies - 500)
        else:
            self.royalty = 0.1 * self.price * 500 + 0.125 * self.price * 1000 + 0.15 * self.price * (self.copies - 1500)
        return self.royalty


class Ebook(Book):
    def __init__(self, title="", author="", publisher="", price=0, copies=0, format=""):
        super().__init__(title, author, publisher, price, copies)
        self.format = format

    def set_format(self, format):
        self.format = format

    def get_format(self):
        return self.format

    def royalty_method(self):
        royalty_amount = super().royalty_method()
        return 0.88 * royalty_amount  # Apply 12% GST deduction for ebooks
