package Bank;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class Main {
    static Scanner console = new Scanner(System.in);
    static Bank bank = new Bank("SBI");

    public static void main(String[] args) {
        while (true) {

            bank.printMenu();
            int choice = console.nextInt();
            switch (choice) {
                case 1:
                    handleRegister();
                    break;
                case 2:
                    handleDeposit();
                    break;
                case 3:
                    handleWithdraw();
                    break;
                case 4:
                    handleCheckBalance();
                    break;
                case 5:
                    handleMiniStatement();
                    break;
                case 6:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid Choice");
            }
        }

    }

    private static void handleMiniStatement() {
        System.out.println("Enter the account number");
        String accno = console.next();
        var user = bank.getUser(accno);
        if (user == null) {
            System.out.println("Invalid Account Number");
            return;
        }
        user.printBankStatement();
    }

    private static void handleCheckBalance() {
        System.out.println("Enter the account number");
        String accno = console.next();
        var user = bank.getUser(accno);
        if (user != null) {
            System.out.println("Your balance is " + user.getBalance());
        } else {
            System.out.println("Invalid Account Number");
        }
    }

    private static void handleWithdraw() {
        System.out.println("Enter the account number");
        String accno = console.next();
        System.out.println("Enter the amount to withdraw");
        double amount = console.nextDouble();
        bank.withdraw(accno, amount);
    }

    private static void handleDeposit() {
        System.out.println("Enter the account number");
        String accno = console.next();
        System.out.println("Enter the amount to deposit");
        double amount = console.nextDouble();
        bank.deposit(accno, amount);
    }

    private static void handleRegister() {
        System.out.println("Enter the first name: ");
        String firstName = console.next();
        System.out.println("Enter the last name: ");
        String lastName = console.next();
        System.out.println("Enter the mobile number: ");
        String mobileNo = console.next();
        System.out.println("Enter the email id: ");
        String emailId = console.next();
        System.out.println("Enter the address: ");
        String address = console.next();
        System.out.println("Enter the account type(Savings / Current): ");
        String type = console.next();
        AccountType accountType;
        if (type.toLowerCase().startsWith("s")) {
            accountType = AccountType.Savings;
        } else if (type.toLowerCase().startsWith("c")) {
            accountType = AccountType.Current;
        } else {
            System.out.println("Invalid Account Type");
            return;
        }
        bank.register(firstName, lastName, mobileNo, emailId, address, accountType);
    }
}

class Bank {
    private String name;
    private ArrayList<User> users;

    public Bank(String name) {
        this.name = name;
        users = new ArrayList<User>();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String generateAccountNumber() {
        var random = new Random();
        var alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        String accountNo = "";
        for (int i = 0; i < 12; i++) {
            accountNo += alpha.charAt(random.nextInt(0, alpha.length() - 1));
        }
        return accountNo;
    }

    public void register(String firstName, String lastName, String mobileNo, String emailId, String address,
            AccountType type) {
        double balance;
        switch (type) {
            case Savings:
                balance = 0;
                break;
            case Current:
                System.out.println("Enter the initial balance:");
                Scanner console = new Scanner(System.in);
                balance = console.nextDouble();
                if (balance < 0) {
                    System.out.println("Invalid Balance");
                    return;
                }
                if (balance < 10000) {
                    System.out.println("Minimum balance is 10000");
                    return;
                }
                break;
            default:
                balance = 0;
                break;
        }
        var user = new User(firstName, lastName, mobileNo, emailId, address, balance, generateAccountNumber());

        users.add(user);
        System.out.println("Account Created Successfully");
        System.out.println("Your account number is " + user.getAccno());

    }

    public void deposit(String accno, double amount) {
        var user = getUser(accno);
        if (user == null) {
            System.out.println("Invalid Account Number");
            return;
        }
        var transaction = new Transactions(TransactionType.DEPOSIT, amount);
        user.addTransaction(transaction);
        user.setBalance(user.getBalance() + amount);
    }

    public void withdraw(String accno, double ammount) {
        var user = getUser(accno);
        if (user == null) {
            System.out.println("Invalid Account Number");
            return;
        }
        if (user.getBalance() < ammount) {
            System.out.println("Insufficient Balance");
            return;
        }
        var transaction = new Transactions(TransactionType.WITHDRAWAL, ammount);
        user.addTransaction(transaction);
        user.setBalance(user.getBalance() - ammount);
        System.out.println("You have withdrawed " + ammount);
    }

    User getUser(String accno) {
        for (var user : users) {
            if (user.getAccno().equals(accno)) {
                return user;
            }
        }
        return null;
    }

    void printMenu() {
        System.out.println("==============================");
        System.out.println("Welcome to " + name + " Bank");
        System.out.println("==============================");
        System.out.println("1. Register");
        System.out.println("2. Deposit");
        System.out.println("3. Withdraw");
        System.out.println("4. Check Balance");
        System.out.println("5. Mini Statement");
        System.out.println("6. Exit");
    }

}

enum AccountType {
    Savings, Current
}

class Transactions {
    TransactionType type;
    double amount;

    public Transactions(TransactionType type, double amount) {
        this.type = type;
        this.amount = amount;
    }

    public TransactionType getType() {
        return type;
    }

    public void setType(TransactionType type) {
        this.type = type;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }
}

enum TransactionType {
    DEPOSIT, WITHDRAWAL
}

class User {
    private String firstName;
    private String lastName;
    private String mobileNo;
    private String emailId;
    private String address;
    private double balance;
    private String accno;
    private ArrayList<Transactions> transactions;

    public User(String firstName, String lastName, String mobileNo, String emailId, String address, double balance,
            String accno) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.mobileNo = mobileNo;
        this.emailId = emailId;
        this.address = address;
        this.balance = balance;
        this.accno = accno;
        transactions = new ArrayList<Transactions>();
    }

    public void addTransaction(Transactions transaction) {
        transactions.add(transaction);
    }

    public void printBankStatement() {
        System.out.println("Account Number: " + accno);
        System.out.println("Name: " + firstName + " " + lastName);
        System.out.println("Mobile Number: " + mobileNo);
        System.out.println("Email Id: " + emailId);
        System.out.println("Address: " + address);
        System.out.println("Balance: " + balance);
        System.out.println("Transactions: ");
        for (var transaction : transactions) {
            System.out.println(transaction.getType() + " " + transaction.getAmount());
        }
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getMobileNo() {
        return mobileNo;
    }

    public void setMobileNo(String mobileNo) {
        this.mobileNo = mobileNo;
    }

    public String getEmailId() {
        return emailId;
    }

    public void setEmailId(String emailId) {
        this.emailId = emailId;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public String getAccno() {
        return accno;
    }

    public void setAccno(String accno) {
        this.accno = accno;
    }
}