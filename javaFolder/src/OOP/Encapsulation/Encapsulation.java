package OOP.Encapsulation;


// Encapsulation Example 

// Student class demonstrating encapsulation
class Student {
    // Private variables - data hiding
    private String name;
    private int age;
    private String college;
    private double gpa;
    private String studentId;
    
    // Default constructor
    public Student() {
        this.name = "Unknown";
        this.age = 0;
        this.college = "Unknown";
        this.gpa = 0.0;
        this.studentId = "000000";
    }
    
    // Parameterized constructor
    public Student(String name, int age, String college, double gpa, String studentId) {
        this.name = name;
        this.age = age;
        this.college = college;
        this.gpa = gpa;
        this.studentId = studentId;
    }
    
    // Public getter methods - controlled access to private data
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getCollege() {
        return college;
    }
    
    public double getGpa() {
        return gpa;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    // Public setter methods - controlled modification of private data
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name;
        } else {
            System.out.println("Invalid name provided!");
        }
    }
    
    public void setAge(int age) {
        if (age > 0 && age < 120) {
            this.age = age;
        } else {
            System.out.println("Invalid age! Age must be between 1 and 119.");
        }
    }
    
    public void setCollege(String college) {
        if (college != null && !college.trim().isEmpty()) {
            this.college = college;
        } else {
            System.out.println("Invalid college name provided!");
        }
    }
    
    public void setGpa(double gpa) {
        if (gpa >= 0.0 && gpa <= 10.0) {
            this.gpa = gpa;
        } else {
            System.out.println("Invalid GPA! GPA must be between 0.0 and 10.0.");
        }
    }
    
    public void setStudentId(String studentId) {
        if (studentId != null && studentId.length() == 6) {
            this.studentId = studentId;
        } else {
            System.out.println("Invalid student ID! ID must be 6 characters long.");
        }
    }
    
    // Method to display student information
    public void displayStudentInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("College: " + college);
        System.out.println("GPA: " + gpa);
        System.out.println("Student ID: " + studentId);
    }
    
    // Method to check if student is eligible for honors
    public boolean isEligibleForHonors() {
        return gpa >= 8.5;
    }
    
    // Method to calculate years until graduation
    public int yearsUntilGraduation() {
        int currentYear = java.time.LocalDate.now().getYear();
        int admissionYear = currentYear - (age - 18); // Assuming admission at 18
        int graduationYear = admissionYear + 4;
        return Math.max(0, graduationYear - currentYear);
    }
}

// BankAccount class - another example of encapsulation
class BankAccount {
    private String accountNumber;
    private String accountHolderName;
    private double balance;
    private String bankName;
    
    // Constructor
    public BankAccount(String accountNumber, String accountHolderName, String bankName) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = 0.0;
        this.bankName = bankName;
    }
    
    // Getter methods
    public String getAccountNumber() {
        return accountNumber;
    }
    
    public String getAccountHolderName() {
        return accountHolderName;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public String getBankName() {
        return bankName;
    }
    
    // Method to deposit money
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount);
            System.out.println("Current Balance: $" + balance);
        } else {
            System.out.println("Invalid deposit amount!");
        }
    }
    
    // Method to withdraw money
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
            System.out.println("Current Balance: $" + balance);
            return true;
        } else {
            System.out.println("Invalid withdrawal amount or insufficient funds!");
            return false;
        }
    }
    
    // Method to display account info
    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Holder: " + accountHolderName);
        System.out.println("Bank: " + bankName);
        System.out.println("Balance: $" + balance);
    }
}

// Main class to demonstrate encapsulation
public class Encapsulation {
    public static void main(String[] args) {
        // Java Encapsulation Example
        
        // Creating a student object using parameterized constructor
        Student student1 = new Student("Shashwat", 21, "VESIT", 9.2, "123456");
        
        // Display student information
        student1.displayStudentInfo();
        
        // Check if eligible for honors
        if (student1.isEligibleForHonors()) {
            System.out.println(student1.getName() + " is eligible for honors!");
        }
        
        // Calculate years until graduation
        System.out.println("Years until graduation: " + student1.yearsUntilGraduation());
        System.out.println();
        
        // Creating another student using default constructor
        Student student2 = new Student();
        System.out.println("Student with default constructor:");
        student2.displayStudentInfo();
        
        // Using setter methods to modify student information
        student2.setName("Rahul");
        student2.setAge(20);
        student2.setCollege("IIT Bombay");
        student2.setGpa(8.7);
        student2.setStudentId("654321");
        
        System.out.println("\nAfter setting values:");
        student2.displayStudentInfo();
        
        System.out.println();
        
        // Demonstrating data validation in setters
        // Testing Data Validation 
        student2.setAge(-5);  // Invalid age
        student2.setGpa(15.0); // Invalid GPA
        student2.setName("");  // Invalid name
        
        System.out.println();
        
        // Bank Account Encapsulation example 
        BankAccount account = new BankAccount("ACC001", "Shashwat", "State Bank of India");
        
        account.displayAccountInfo();
        
        // Perform transactions
        account.deposit(5000);
        account.withdraw(2000);
        account.withdraw(4000); // This should fail due to insufficient funds
        
        account.displayAccountInfo();
    }
}