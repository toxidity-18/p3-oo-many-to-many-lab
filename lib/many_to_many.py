class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def __str__(self):
        return f"Book: {self.title}"

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if royalties < 0 or royalties > 100:
            raise Exception("Royalties must be between 0 and 100")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __str__(self):
        return f"Contract: {self.author.name} - {self.book.title} - {self.date} - {self.royalties}%"