from libs.trackers import LoanTracker, UserTracker, BookTracker


class LoanPrinter:
    def __init__(self,
            loan_tracker: LoanTracker,
            user_tracker: UserTracker,
            book_tracker: BookTracker
        ):
        self.loan_tracker = loan_tracker
        self.user_tracker = user_tracker
        self.book_tracker = book_tracker

    def print_loans(self):
        for k,v in self.loan_tracker.loans.items():
            user = self.user_tracker.users[v.user_id]
            book = self.book_tracker.books[v.book_id]
            print(f"User {user.id}:{user.name} borrowed book {book.id}:{book.title}")

