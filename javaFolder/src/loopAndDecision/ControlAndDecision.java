package loopAndDecision;


public class ControlAndDecision {
    public static void main(String[] args) {
        String name = "Shashwat Tripathi";
        int age = 21;
        
        // Decision making with if-else
        if (age >= 18) {
            System.out.println(name + " is an adult");
        } else {
            System.out.println(name + " is a minor");
        }
        
        // Check voting eligibility
        if (age >= 18) {
            System.out.println(name + " can vote");
        }
        
        // Multiple conditions
        if (age >= 21 && age <= 30) {
            System.out.println(name + " is in their twenties");
        }
        
        // Switch case example
        int day = 3;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday - " + name + " has class today");
                break;
            default:
                System.out.println("Other day");
        }
        

	    // Loop Control
        // For loop
        System.out.println("Using for loop:");
        for (int i = 1; i <= 3; i++) {
            System.out.println(i + ". Hello " + name);
        }
        
        // While loop
        System.out.println("\nUsing while loop (countdown from age):");
        int count = age;
        while (count >= 18) {
            System.out.println("Count: " + count);
            count--;
            if (count == 18) break; // Stop at 18
        }
        
        // Do-while loop
        System.out.println("\nUsing do-while loop:");
        int num = 1;
        do {
            System.out.println(name + " - Attempt " + num);
            num++;
        } while (num <= 2);
        
        // Nested loops
        System.out.println("\nNested loops - Simple pattern:");
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
