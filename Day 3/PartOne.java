import java.util.Arrays;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class PartOne{
    public static void main(String[] args) {
        int sum=0;
        try {
            File myObj = new File("src/main/java/sampleText.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                for(int i = 0; i < data.length()-3; i++){
                    int error = 0;
                    if(data.substring(i, i+4).equals("mul(")){
                        String[] saveThing = data.substring(i+4, data.indexOf(")", i+4)).split(",");
                        String everythingBehind = data.substring(0, data.indexOf(")", i+4)+1);
                        if(saveThing.length == 2){
                            try{
                                sum+=Integer.valueOf(saveThing[0])*Integer.valueOf(saveThing[1]);
                            }catch (Exception e){
                                error+=1;
                            }
                        }
                    }
                }
            }
            myReader.close();
        }catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println(sum);
    }
}
