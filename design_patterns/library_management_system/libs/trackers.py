from abc import ABC, abstractmethod
from libs.entities import Entity, User, Book, Loan


class Tracker(ABC):
    @abstractmethod
    def add(self, entity: Entity):
        pass

    def remove(self, _id: int):
        pass


class UserTracker(Tracker):
    def __init__(self):
        self.users = {}

    def add(self, user: User):
        self.users[user.get_id()] = user

    def remove(self, _id: int) -> int:
        return self.users.pop(_id)


class BookTracker(Tracker):
    def __init__(self):
        self.books = {}

    def add(self, book: Book):
        self.books[book.get_id()] = book

    def remove(self, _id: int) -> int:
        return self.books.pop(_id)


class LoanTracker(Tracker):
    def __init__(self):
        self.loans = {}
        self.next_id = 1

    def add(self, loan: Loan):
        loan.id = self.next_id
        self.loans[self.next_id] = loan
        self.next_id += 1

    def remove(self, _id: int):
        return self.loans.pop(_id)
