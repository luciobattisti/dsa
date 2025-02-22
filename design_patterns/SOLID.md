### **What are the SOLID Principles?**  
SOLID is an acronym for five design principles that help in creating flexible and robust software. They were introduced by Robert C. Martin (Uncle Bob) and are widely used in software engineering.

---
## 🔹 **S - Single Responsibility Principle (SRP)**
> **A class should have only one reason to change.**  

### **Explanation**  
Each class should only have **one responsibility** or **one job**. If a class is handling multiple unrelated tasks, it's harder to maintain and modify.  

### **Bad Example (Violating SRP)**
```python
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate_report())
```
🔴 **Problem:** The `Report` class is responsible for **both** generating a report and saving it to a file. If file saving logic changes (e.g., switching to a database), we must modify this class.

### **Good Example (Following SRP)**
```python
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
```
✅ **Now,** `Report` is only responsible for **report generation**, and `ReportSaver` is responsible for **saving** the report.

---
## 🔹 **O - Open/Closed Principle (OCP)**
> **Software entities should be open for extension but closed for modification.**  

### **Explanation**  
A class should be easily **extended** without modifying its existing code.

### **Bad Example (Violating OCP)**
```python
class Discount:
    def __init__(self, customer_type):
        self.customer_type = customer_type

    def get_discount(self, amount):
        if self.customer_type == "regular":
            return amount * 0.1
        elif self.customer_type == "vip":
            return amount * 0.2
```
🔴 **Problem:** Every time we add a new customer type, we must modify the class.

### **Good Example (Following OCP)**
```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def get_discount(self, amount):
        pass

class RegularDiscount(Discount):
    def get_discount(self, amount):
        return amount * 0.1

class VIPDiscount(Discount):
    def get_discount(self, amount):
        return amount * 0.2
```
✅ **Now,** we can add new discount types without modifying existing code.

---
## 🔹 **L - Liskov Substitution Principle (LSP)**
> **Subtypes must be substitutable for their base types.**  

### **Explanation**  
A subclass should be a drop-in replacement for its superclass without breaking functionality.

### **Bad Example (Violating LSP)**
```python
class Bird:
    def fly(self):
        print("I can fly!")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
```
🔴 **Problem:** A `Penguin` **is-a** `Bird`, but it breaks the expected behavior (since it can’t fly).

### **Good Example (Following LSP)**
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly!")

class Penguin(Bird):
    def swim(self):
        print("I can swim!")
```
✅ **Now,** `Penguin` doesn’t incorrectly inherit flying behavior.

---
## 🔹 **I - Interface Segregation Principle (ISP)**
> **Clients should not be forced to depend on methods they do not use.**  

### **Explanation**  
A class shouldn’t be forced to implement methods that it doesn’t need.

### **Bad Example (Violating ISP)**
```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("I am working.")

    def eat(self):
        raise Exception("Robots don't eat!")
```
🔴 **Problem:** `Robot` is forced to implement `eat()`, which it doesn’t need.

### **Good Example (Following ISP)**
```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("I am working.")

    def eat(self):
        print("I am eating.")

class Robot(Workable):
    def work(self):
        print("I am working.")
```
✅ **Now,** `Robot` is not forced to implement `eat()`.

---
## 🔹 **D - Dependency Inversion Principle (DIP)**
> **Depend on abstractions, not on concrete implementations.**  

### **Explanation**  
High-level modules should not depend on low-level modules. Both should depend on **abstractions**.

### **Bad Example (Violating DIP)**
```python
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class Application:
    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling

    def start(self):
        self.db.connect()
```
🔴 **Problem:** `Application` is tightly coupled to `MySQLDatabase`. If we want to use PostgreSQL, we must modify `Application`.

### **Good Example (Following DIP)**
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()
```
✅ **Now,** we can switch databases without modifying `Application`.

---
## 🔥 **Summary Table**
| Principle | Definition | Key Benefit |
|-----------|------------|------------|
| **S** | **Single Responsibility** – A class should have only one reason to change. | Increases maintainability. |
| **O** | **Open/Closed** – Open for extension, closed for modification. | Allows adding new features without breaking existing code. |
| **L** | **Liskov Substitution** – Subtypes must be replaceable for their base types. | Prevents unexpected behavior in inheritance. |
| **I** | **Interface Segregation** – No class should be forced to implement unused methods. | Reduces unnecessary dependencies. |
| **D** | **Dependency Inversion** – Depend on abstractions, not concrete implementations. | Makes code more flexible and testable. |

Great choice! **Service Locators** and **Factories** are powerful patterns that work well with **Dependency Injection (DI)** to manage dependencies dynamically.  

---

## **🔹 Service Locator Pattern**
The **Service Locator** acts as a **central registry** where dependencies (trackers, services, etc.) are stored and retrieved when needed.  
Instead of injecting dependencies manually into each class, you **ask the Service Locator** for what you need.

---

### **✅ Step 1: Implement a Service Locator**
```python
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
```

---

### **✅ Step 2: Modify the Main Code to Use the Service Locator**
```python
# Register Trackers in ServiceLocator
ServiceLocator.register("user_tracker", UserTracker())
ServiceLocator.register("book_tracker", BookTracker())
ServiceLocator.register("loan_tracker", LoanTracker())

# Retrieve services when needed
user_tracker = ServiceLocator.get("user_tracker")
book_tracker = ServiceLocator.get("book_tracker")
loan_tracker = ServiceLocator.get("loan_tracker")

# Register LoanPrinter using the retrieved services
ServiceLocator.register("loan_printer", LoanPrinter(loan_tracker, user_tracker, book_tracker))

# Retrieve LoanPrinter
loan_printer = ServiceLocator.get("loan_printer")
```

---

### **🔹 Why Use a Service Locator?**
✅ **Centralized Dependency Management**:  
  - You register all dependencies in one place and retrieve them when needed.  

✅ **More Flexible than Constructor Injection**:  
  - No need to pass dependencies to every constructor—classes request what they need.  

✅ **Useful for Large Applications**:  
  - In complex systems, DI frameworks (like Spring in Java) use Service Locators to manage dependencies.  

---

## **🔹 Factory Pattern**
A **Factory** is responsible for **creating objects** without exposing instantiation logic.  
This is useful when object creation is **complex** or **varies based on conditions**.

---

### **✅ Step 1: Create a Factory for Trackers**
```python
class TrackerFactory:
    _trackers = {
        "user": UserTracker,
        "book": BookTracker,
        "loan": LoanTracker
    }

    @classmethod
    def create(cls, tracker_type: str):
        """Create and return a new tracker instance."""
        if tracker_type in cls._trackers:
            return cls._trackers[tracker_type]()
        raise ValueError(f"Unknown tracker type: {tracker_type}")
```

---

### **✅ Step 2: Use the Factory Instead of Instantiating Manually**
```python
# Create Trackers using Factory
user_tracker = TrackerFactory.create("user")
book_tracker = TrackerFactory.create("book")
loan_tracker = TrackerFactory.create("loan")

# Register in ServiceLocator
ServiceLocator.register("user_tracker", user_tracker)
ServiceLocator.register("book_tracker", book_tracker)
ServiceLocator.register("loan_tracker", loan_tracker)
```

---

## **🔹 Combining Service Locator & Factory**
Instead of manually creating trackers and registering them, we can **automate** it:
```python
# Automatically register Trackers using Factory
for tracker_type in ["user", "book", "loan"]:
    ServiceLocator.register(f"{tracker_type}_tracker", TrackerFactory.create(tracker_type))

# Retrieve Loan Tracker dynamically
loan_tracker = ServiceLocator.get("loan_tracker")
```

---

## **🔹 Key Benefits**
| Pattern              | Benefit |
|----------------------|---------|
| **Factory**         | Centralized object creation, flexible instantiation |
| **Service Locator** | Centralized dependency resolution, reduces constructor injection overhead |

---
