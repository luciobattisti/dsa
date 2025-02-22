from libs.trackers import UserTracker, BookTracker, LoanTracker

class ServiceLocator:
    _services = {}

    @classmethod
    def register(cls, name: str, service):
        """Register a service with a name."""
        cls._services[name] = service

    @classmethod
    def get(cls, name: str):
        """Retrieve a service by name."""
        return cls._services.get(name)


class LoanPrinter:
    def __init__(self):
        self.loan_tracker = ServiceLocator.get("loan_tracker")
        self.user_tracker = ServiceLocator.get("user_tracker")
        self.book_tracker = ServiceLocator.get("book_tracker")

    def print_loans(self):
        for k,v in self.loan_tracker.loans.items():
            user = self.user_tracker.users[v.user_id]
            book = self.book_tracker.books[v.book_id]
            print(f"User {user.id}:{user.name} borrowed book {book.id}:{book.title}")


user_tracker = UserTracker()
book_tracker = BookTracker()
loan_tracker = LoanTracker()

ServiceLocator.register("user_tracker", user_tracker)
ServiceLocator.register("book_tracker", book_tracker)
ServiceLocator.register("loan_tracker", loan_tracker)

loan_printer = LoanPrinter()


