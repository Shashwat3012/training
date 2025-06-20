package JDBC;

import java.sql.*;

public class JdbcExample {
    static final String DB_URL = "jdbc:mysql://localhost:3306/shashwat_db";
    static final String USER = "root";
    static final String PASS = "admin";

    public static void main(String[] args) {
        try (
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            Statement stmt = conn.createStatement();
        ) {
            // Insert
            stmt.executeUpdate("INSERT INTO students VALUES (1, 'Shashwat', 21, 'VESIT')");
            stmt.executeUpdate("INSERT INTO students VALUES (2, 'Harkirat', 22, 'VESIT')");
            stmt.executeUpdate("INSERT INTO students VALUES (3, 'Piyush', 21, 'VESIT')");
            stmt.executeUpdate("INSERT INTO students VALUES (4, 'Kunal', 23, 'VESIT')");
            System.out.println("Inserted records.");

            // Select
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            System.out.println("\n--- Students ---");
            while (rs.next()) {
                System.out.println(
                    rs.getInt("id") + ", " +
                    rs.getString("name") + ", " +
                    rs.getInt("age") + ", " +
                    rs.getString("college")
                );
            }

            // Update
            stmt.executeUpdate("UPDATE students SET age = 22 WHERE name = 'Shashwat'");
            System.out.println("\nUpdated Shashwat's age to 22.");

            // Delete
            stmt.executeUpdate("DELETE FROM students WHERE name = 'Kunal'");
            System.out.println("Deleted Kunal from records.");

            // Select again
            rs = stmt.executeQuery("SELECT * FROM students");
            System.out.println("\n--- Final Students ---");
            while (rs.next()) {
                System.out.println(
                    rs.getInt("id") + ", " +
                    rs.getString("name") + ", " +
                    rs.getInt("age") + ", " +
                    rs.getString("college")
                );
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
