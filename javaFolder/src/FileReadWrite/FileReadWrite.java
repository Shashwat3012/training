package FileReadWrite;


import java.io.*;

public class FileReadWrite {
    static final String fileName = "./src/FileReadWrite/shashwat_info.txt";

    public static void main(String[] args) {
        // Data to write
        String aboutMe = "Name: Shashwat\nAge: 21\nCollege: VESIT";

        // Write to file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write(aboutMe);
            System.out.println("✅ Data written to file: " + fileName);
        } catch (IOException e) {
            System.out.println("❌ Error writing file: " + e.getMessage());
        }

        // Read from file
        System.out.println("\n📖 Reading from file:");
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("❌ Error reading file: " + e.getMessage());
        }
    }
}
