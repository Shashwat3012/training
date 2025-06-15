package OOP.Abstraction;


// Abstraction using Abstract Classes and Methods

// Abstract class - cannot be instantiated
abstract class Vehicle {
    String name;
    String owner;
    
    // Constructor in abstract class
    public Vehicle(String name, String owner) {
        this.name = name;
        this.owner = owner;
    }
    
    // Concrete method - can be inherited as is
    public void displayInfo() {
        System.out.println("Vehicle: " + name + ", Owner: " + owner);
    }
    
    // Abstract methods - must be implemented by subclasses
    public abstract void start();
    public abstract void stop();
    public abstract void accelerate();
    public abstract double getMaxSpeed();
}

// Concrete class extending abstract class
class Car extends Vehicle {
    String model;
    int year;
    
    public Car(String name, String owner, String model, int year) {
        super(name, owner);
        this.model = model;
        this.year = year;
    }
    
    // Implementing abstract methods
    @Override
    public void start() {
        System.out.println(owner + "'s " + name + " car is starting with ignition");
    }
    
    @Override
    public void stop() {
        System.out.println(name + " car is stopping using brakes");
    }
    
    @Override
    public void accelerate() {
        System.out.println(name + " car is accelerating using gas pedal");
    }
    
    @Override
    public double getMaxSpeed() {
        return 180.0; // km/h
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Model: " + model + ", Year: " + year);
    }
}

class Motorcycle extends Vehicle {
    String type;
    
    public Motorcycle(String name, String owner, String type) {
        super(name, owner);
        this.type = type;
    }
    
    @Override
    public void start() {
        System.out.println(owner + "'s " + name + " motorcycle is starting with kick/electric start");
    }
    
    @Override
    public void stop() {
        System.out.println(name + " motorcycle is stopping using hand brakes");
    }
    
    @Override
    public void accelerate() {
        System.out.println(name + " motorcycle is accelerating using throttle");
    }
    
    @Override
    public double getMaxSpeed() {
        return 200.0; // km/h
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Type: " + type);
    }
}

// Abstract class for Student example
abstract class Student {
    String name;
    int age;
    String college;
    
    public Student(String name, int age, String college) {
        this.name = name;
        this.age = age;
        this.college = college;
    }
    
    // Concrete methods
    public void displayBasicInfo() {
        System.out.println("Student: " + name + ", Age: " + age + ", College: " + college);
    }
    
    public void attendLecture() {
        System.out.println(name + " is attending lecture at " + college);
    }
    
    // Abstract methods
    public abstract void study();
    public abstract void takeExam();
    public abstract String getDegree();
    public abstract void practicalWork();
}

class ComputerStudent extends Student {
    String specialization;
    
    public ComputerStudent(String name, int age, String college, String specialization) {
        super(name, age, college);
        this.specialization = specialization;
    }
    
    @Override
    public void study() {
        System.out.println(name + " is studying computer science subjects and " + specialization);
    }
    
    @Override
    public void takeExam() {
        System.out.println(name + " is taking computer science exam at " + college);
    }
    
    @Override
    public String getDegree() {
        return "Bachelor of Engineering in Computer Science";
    }
    
    @Override
    public void practicalWork() {
        System.out.println(name + " is doing programming practicals in " + specialization);
    }
    
    public void code() {
        System.out.println(name + " is coding in " + specialization);
    }
}

class MechanicalStudent extends Student {
    String stream;
    
    public MechanicalStudent(String name, int age, String college, String stream) {
        super(name, age, college);
        this.stream = stream;
    }
    
    @Override
    public void study() {
        System.out.println(name + " is studying mechanical engineering and " + stream);
    }
    
    @Override
    public void takeExam() {
        System.out.println(name + " is taking mechanical engineering exam at " + college);
    }
    
    @Override
    public String getDegree() {
        return "Bachelor of Engineering in Mechanical Engineering";
    }
    
    @Override
    public void practicalWork() {
        System.out.println(name + " is doing workshop practicals in " + stream);
    }
    
    public void designMachine() {
        System.out.println(name + " is designing machines in " + stream);
    }
}

// Abstract class with some implemented methods
abstract class Shape {
    String color;
    
    public Shape(String color) {
        this.color = color;
    }
    
    // Concrete method
    public void setColor(String color) {
        this.color = color;
        System.out.println("Color set to: " + color);
    }
    
    // Abstract methods
    public abstract double calculateArea();
    public abstract double calculatePerimeter();
    public abstract void draw();
}

class Circle extends Shape {
    double radius;
    
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " circle with radius: " + radius);
    }
}

public class Abstraction {
    public static void main(String[] args) {
        // Vehicle Abstraction Example 
        
        // Cannot instantiate abstract class: Vehicle v = new Vehicle(); // Error
        
        Car car = new Car("Honda", "Shashwat Tripathi", "Civic", 2022);
        Motorcycle bike = new Motorcycle("Yamaha", "Shashwat Tripathi", "Sport");
        
        car.displayInfo();
        car.start();
        car.accelerate();
        System.out.println("Max speed: " + car.getMaxSpeed() + " km/h");
        car.stop();
        
        System.out.println();
        
        bike.displayInfo();
        bike.start();
        bike.accelerate();
        System.out.println("Max speed: " + bike.getMaxSpeed() + " km/h");
        bike.stop();
        System.out.println();
        
        
        //  Student Abstraction Example 
        ComputerStudent compStudent = new ComputerStudent("Shashwat Tripathi", 21, "VESIT", "AI & ML");
        MechanicalStudent mechStudent = new MechanicalStudent("Shashwat Tripathi", 21, "VESIT", "Robotics");
        
        compStudent.displayBasicInfo();
        compStudent.attendLecture();
        compStudent.study();
        compStudent.practicalWork();
        compStudent.takeExam();
        System.out.println("Degree: " + compStudent.getDegree());
        compStudent.code();
        
        System.out.println();
        
        mechStudent.displayBasicInfo();
        mechStudent.attendLecture();
        mechStudent.study();
        mechStudent.practicalWork();
        mechStudent.takeExam();
        System.out.println("Degree: " + mechStudent.getDegree());
        mechStudent.designMachine();
        System.out.println();
        
        
        
        // Shape Abstraction Example
        Circle circle = new Circle("Red", 5.0);
        circle.draw();
        System.out.println("Area: " + circle.calculateArea());
        System.out.println("Perimeter: " + circle.calculatePerimeter());
        circle.setColor("Blue");
        circle.draw();
        System.out.println();
        
        
        // Polymorphism with Abstract Classes
        Vehicle[] vehicles = {car, bike};
        
        for (Vehicle vehicle : vehicles) {
            vehicle.displayInfo();
            vehicle.start();
            System.out.println("Max Speed: " + vehicle.getMaxSpeed() + " km/h");
            vehicle.stop();
            System.out.println();
        }
    }
}