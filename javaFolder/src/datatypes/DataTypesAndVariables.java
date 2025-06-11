package datatypes;

public class DataTypesAndVariables {

    // Primitive types
    public static int intValue = 100;
    public static double doubleValue = 99.99;
    public static char charValue = 'A';
    public static boolean boolValue = true;

    // Reference types
    public String name = "Shashwat";
    public int[] scores = {90, 80, 85};

    // Modifiers
    private int age = 21;
    protected String email = "shashwat@example.com";
    public static String university = "Mumbai University";
    public final String STUDENT_ID = "64";

    // Final initialized in constructor
    private final String enrollmentNo;

    // Constructor
    public DataTypesAndVariables(String name, int age) {
        this.name = name;
        this.age = age;
        this.enrollmentNo = "ENR" + System.currentTimeMillis();
    }

    // Demonstrate local variables
    public void showLocalVars() {
        int local = 10;
        final String CONST = "Fixed";
        System.out.println("Local: " + local + ", Final: " + CONST);
    }

    // Demonstrate type conversion
    public void showConversions() {k
        int a = 50;
        double b = a;             // Implicit
        int c = (int) b;          // Explicit
        System.out.println("Int to Double: " + b + ", Double to Int: " + c);
    }

    // Show data
    public void showInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
        System.out.println("University: " + university + ", ID: " + STUDENT_ID);
    }

    public static void main(String[] args) {
        DataTypesAndVariables student = new DataTypesAndVariables("Shashwat", 21);
        student.showLocalVars();
        student.showConversions();
        student.showInfo();
    }
}
