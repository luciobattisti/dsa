from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def get_id(self):
        pass


class Book(Entity):
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def get_id(self):
        return self.id


class User(Entity):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id


class Loan(Entity):
    def __init__(self, user_id: int, book_id: int):
        self.id = 0
        self.user_id = user_id
        self.book_id = book_id

    def get_id(self):
        return self.id
