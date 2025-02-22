# Single responsibility principle
# A class should have only one reason to change
# Bad example
# The class is responsible for both generating and saving a report
# If we want to change the saving logic (e.g. switching to a DB),
# we need to change the class
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate_report())

# Improvement
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, "w") as file:
            file.write(report.generate_report())


# Open Close Principle
# Class should be open for extension but closed for modifications
# Bad Example
# Violates OCP because anytime we add a new discount type, we have to modify the Discount class
class Discount:
    def __init__(self, customer_type):
        self.customer_type = customer_type

    def get_discount(self, amount):
        if self.customer_type == "regular":
            return amount * 0.1
        elif self.customer_type == "vip":
            return amount * 0.2

# Improvement
from abc import ABC, abstractmethod


class DiscountBase(ABC):
    @abstractmethod
    def get_discount(self, amount):
        pass

class DiscountRegular(DiscountBase):
    def get_discount(self, amount):
        return amount * 0.1

class DiscountVip(DiscountBase):
    def get_discount(self, amount):
        return amount * 0.2


# Liskov substitution principle
# A subclass should be a drop-in replacement for its superclass without breaking functionality
# Bad example
# Functionality is broken because penguins cannot fly
class Bird:
    def fly(self):
        print("I can fly.")

class Penguin(Bird):
    def fly(self):
        raise "Penguins can't fly"

# Improvement
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly.")

class Penguin(Bird):
    def swim(self):
        print("I can swim.")

# Interface Segregation Principle (ISP)
# Clients should not be forced to depend on methods that don't use
# Bad example
# Robot is forced to implement the eat method even if it doesn't it
class Worker:
    def work(self):
        pass

    def ear(self):
        pass

class Robot(Worker):
    def work(self):
        print("I can work")

    def eat(self):
        raise "I cannot eat."

# Improvement
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("I can work.")

    def eat(self):
        print("I need to eat.")

class Robot(Workable):
    def work(self):
        print("I can work.")

# Dependency Inversion Principle
# Depend on abstractions, not on concrete implementations
# If we want to change the database to PostgreSQL we need to modify Application
# Bad example
class MySQLDataBase:
    def connect(self):
        print("Connect to MySQL")

class Application:
    def __init__(self):
        self.db = MySQLDataBase()

    def start(self):
        self.db.connect()

# Improvement
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connect to MySQL.")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connect to PostgreSQL.")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def connect(self):
        self.db.connect()









