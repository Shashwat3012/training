package OOP;


// Parent Class
class Student {
    String name;
    int age;
    String college;
    
    public Student(String name, int age, String college) {
        this.name = name;
        this.age = age;
        this.college = college;
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("College: " + college);
    }
    
    public void study() {
        System.out.println(name + " is studying");
    }
}

// Single Inheritance Example
// Engineering student inherits from Student
class EngineeringStudent extends Student {
    String branch;
    
    public EngineeringStudent(String name, int age, String college, String branch) {
        super(name, age, college); // Call parent constructor
        this.branch = branch;
    }
    
    public void displayInfo() {
        super.displayInfo(); // Call parent method
        System.out.println("Branch: " + branch);
    }
    
    public void code() {
        System.out.println(name + " from " + college + " is coding in " + branch);
    }
}

// Multilevel Inheritance Example
class ComputerStudent extends EngineeringStudent {
    String specialization;
    
    public ComputerStudent(String name, int age, String college, String branch, String specialization) {
        super(name, age, college, branch);
        this.specialization = specialization;
    }
    
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Specialization: " + specialization);
    }
    
    public void developSoftware() {
        System.out.println(name + " is developing software in " + specialization);
    }
}

// Hierarchical Inheritance - Another class extending Student
class MedicalStudent extends Student {
    String medicalField;
    
    public MedicalStudent(String name, int age, String college, String medicalField) {
        super(name, age, college);
        this.medicalField = medicalField;
    }
    
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Medical field: " + medicalField);
    }
    
    public void diagnose() {
        System.out.println(name + " is diagnosing patients in " + medicalField);
    }
}

public class Inheritance {
    public static void main(String[] args) {
        // Single Inheritance Object Creation
        EngineeringStudent engStudent = new EngineeringStudent("Shashwat Tripathi", 21, "VESIT", "Computer Engineering");
        engStudent.displayInfo();
        engStudent.study();
        engStudent.code();
        
        // Multilevel Inheritance Object Creation
        ComputerStudent compStudent = new ComputerStudent("Shashwat Tripathi", 21, "VESIT", "Computer Engineering", "AI & ML");
        compStudent.displayInfo();
        compStudent.study();
        compStudent.code();
        compStudent.developSoftware();
        
        // Hierarchical Inheritance Object Creation
        MedicalStudent medStudent = new MedicalStudent("Shashwat Tripathi", 21, "VESIT", "Cardiology");
        medStudent.displayInfo();
        medStudent.study();
        medStudent.diagnose();
        
        // Finding the class of the objects
        System.out.println("engStudent instanceof Student: " + (engStudent instanceof Student));
        System.out.println("compStudent instanceof EngineeringStudent: " + (compStudent instanceof EngineeringStudent));
        System.out.println("compStudent instanceof Student: " + (compStudent instanceof Student));
    }
}