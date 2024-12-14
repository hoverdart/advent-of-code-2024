import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PartTwo {
    public static void main(String[] args) {
        int sum = 0;
        boolean isEnabled = true; // Initial state: mul() instructions are enabled.
        try {
            File myObj = new File("src/main/java/sampleText.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                Pattern pattern = Pattern.compile("do\\(\\)|don't\\(\\)|mul\\((\\d+),(\\d+)\\)");
                // Lemme Explain this Regex Funstuff; It's essentially a search pattern that looks for specific words and/or complex sequences. To add a paranthesis, you add a backslash and then the paranthesis. To add a backslash, you add a backslash, as Java requires double slashes -> \\( == (, \\) = ) -> 
                // The mul(digit 1, digit 2) is a bit different; mul\\((\\d+),(\\d+)\\) -> The "\\(" captures the first parenthesis of the expression, the second ( is a "capturing" parenthesis and, combined with the \\d+ makes the d+ experssion, then the closing parenthesis closes that expression [this expression checks for 1+ digits], the comma is the regular comma, same exact thing with the next capturing parenthesis, and then the closing parenthesis \\).
                Matcher matcher = pattern.matcher(data);
                while (matcher.find()) {
                    String match = matcher.group();
                    if (match.equals("do()")) {
                        isEnabled = true; // Enable future mul()
                    } else if (match.equals("don't()")) {
                        isEnabled = false; // Disable future mul()
                    } else if (match.startsWith("mul(") && isEnabled) {
                        int a = Integer.parseInt(matcher.group(1)); // Capture digit1
                        int b = Integer.parseInt(matcher.group(2)); // Capture digit2
                        sum += a * b; // Add the result of the multiplication
                    }
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println(sum);
    }
}
