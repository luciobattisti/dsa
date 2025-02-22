from libs.entities import User, Book, Loan
from libs.trackers import UserTracker, BookTracker, LoanTracker
from libs.utils import LoanPrinter

if __name__ == "__main__":

    user_tracker = UserTracker()
    book_tracker = BookTracker()

    print("Add Books")
    book_tracker.add(Book(1, "I Promessi Sposi"))
    book_tracker.add(Book(2, "I Miserabili"))
    book_tracker.add(Book(3, "On the Road"))
    book_tracker.add(Book(4, "Wuthering Heights"))

    print("Add Users")
    user_tracker.add(User(1, "Roberto"))
    user_tracker.add(User(2, "Alex"))
    user_tracker.add(User(3, "Valentino"))

    print("Instantiate Loan Tracker and Printer")
    loan_tracker = LoanTracker()
    loan_printer = LoanPrinter(
        loan_tracker,
        user_tracker,
        book_tracker
    )

    print(
        """
        Case 1:
        User 1 gets Book 2
        """
    )

    user = user_tracker.users[1]
    book = book_tracker.books[2]

    loan_tracker.add(Loan(user.id, book.id))
    loan_printer.print_loans()













