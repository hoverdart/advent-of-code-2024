// import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Arrays;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class PartTwo {
    public static void main(String[] args) {
        int size = 1000;
        int[] firstColumn = new int[size];
        int[] secondColumn = new int[size];
        int similarityScoreSum = 0;
        try {
            File myObj = new File("src/main/java/tooMuchText.txt");
            Scanner myReader = new Scanner(myObj);
            int count = 0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                firstColumn[count] = Integer.valueOf(data.substring(0, 5)); //0, 5
                secondColumn[count] = Integer.valueOf(data.substring(8)); //8
                Arrays.sort(firstColumn);
                Arrays.sort(secondColumn);
            }
            myReader.close();
        }catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        for(int eachNum = 0; eachNum < size; eachNum++){
            int similarityMultiplier = 0;
            //Method 1 - Classic Nested List
            for (int numEach = 0; numEach < size; numEach++){
                if(firstColumn[eachNum] == secondColumn[numEach]){
                    similarityMultiplier++;
                }
            }      
            similarityScoreSum += similarityMultiplier*firstColumn[eachNum];
        }
        System.out.println(similarityScoreSum);
    }
}
