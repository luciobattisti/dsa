
## **📌 Code Challenge: Bank Account Management System**
### **Objective**  
Create a simple **bank account system** where users can:  
✅ Create an account with an initial balance  
✅ Deposit money  
✅ Withdraw money (with overdraft protection)  
✅ View account details  

---

### **📌 Requirements**
1️⃣ **Create a `BankAccount` class** with:  
   - `account_number`: Unique identifier for the account  
   - `holder_name`: Name of the account holder  
   - `balance`: The current balance of the account  

2️⃣ **Implement the following methods**:
   - `deposit(amount)`: Adds money to the account  
   - `withdraw(amount)`: Deducts money **only if the balance is sufficient**  
   - `display_balance()`: Prints the current balance  

3️⃣ **Create an interface for user interaction**:
   - Allow users to **create an account**  
   - Allow deposits, withdrawals, and balance checks  
   - Prevent withdrawals that exceed the available balance  

---

### **📌 Example Execution**
```plaintext
Welcome to the Bank Account Management System!

1. Create a new account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit

Choose an option: 1
Enter your name: John Doe
Your account number is: 12345
Account successfully created!

Choose an option: 2
Enter amount to deposit: 500
Deposit successful! New balance: $500.00

Choose an option: 3
Enter amount to withdraw: 600
Insufficient balance!

Choose an option: 4
Your current balance is: $500.00

Choose an option: 5
Goodbye!
```

### **⏳ Time: 30 minutes**