package StringAndArray;

public class StringsAndArrays {
    public static void main(String[] args) {
        String name = "Shashwat Tripathi";
        int age = 21;
        
        // Basic string operations
        System.out.println("Name: " + name);
        System.out.println("Name length: " + name.length());
        System.out.println("Upper case: " + name.toUpperCase());
        System.out.println("Lower case: " + name.toLowerCase());
        
        // String methods
        System.out.println("First character: " + name.charAt(0));
        System.out.println("Contains 'Shashwat': " + name.contains("Shashwat"));
        System.out.println("Starts with 'Shash': " + name.startsWith("Shash"));
        
        // String splitting
        String[] nameParts = name.split(" ");
        System.out.println("First name: " + nameParts[0]);
        System.out.println("Last name: " + nameParts[1]);
        
        // String concatenation
        String info = name + " is " + age + " years old";
        System.out.println(info);
        
        // String comparison
        String name2 = "shashwat tripathi";
        System.out.println("Equal (case sensitive): " + name.equals(name2));
        System.out.println("Equal (ignore case): " + name.equalsIgnoreCase(name2));
        
        
        // Integer array
        int[] ages = {21, 22, 20, 23, 21};
        System.out.println("Ages array:");
        for (int i = 0; i < ages.length; i++) {
            System.out.println("Person " + (i+1) + " age: " + ages[i]);
        }
        
        // String array
        String[] friends = {"Shashwat Tripathi", "Rahul Sharma", "Priya Singh"};
        System.out.println("\nFriends list:");
        for (String friend : friends) {
            System.out.println("- " + friend);
        }
        
        // Find Shashwat in array
        for (int i = 0; i < friends.length; i++) {
            if (friends[i].equals("Shashwat Tripathi")) {
                System.out.println("Found " + name + " at position " + i);
            }
        }
        
        // Array operations
        System.out.println("\nArray operations:");
        System.out.println("Array length: " + ages.length);
        
        // Find max age
        int maxAge = ages[0];
        for (int currentAge : ages) {
            if (currentAge > maxAge) {
                maxAge = currentAge;
            }
        }
        System.out.println("Maximum age: " + maxAge);
        
        // Count how many people are 21
        int count21 = 0;
        for (int currentAge : ages) {
            if (currentAge == 21) {
                count21++;
            }
        }
        System.out.println("People aged 21: " + count21);
        
        // 2D array example
        System.out.println("\n2D Array example:");
        int[][] marks = {
            {85, 90, 88}, // Shashwat's marks
            {78, 82, 85}, // Friend 1's marks  
            {92, 88, 91}  // Friend 2's marks
        };
        
        System.out.println("Shashwat Tripathi's marks:");
        for (int i = 0; i < marks[0].length; i++) {
            System.out.println("Subject " + (i+1) + ": " + marks[0][i]);
        }
    }
}