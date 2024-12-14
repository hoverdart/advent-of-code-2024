import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.ArrayList;
import java.util.Hashtable;

public class PartOne {
    public static void main(String[] args) {
        boolean checkForCorrectUpdates = false;
        int sum = 0;
        Dictionary<Integer, ArrayList<Integer>> keyValue = new Hashtable<>();
        try {
            File myObjj = new File("src/main/java/sample.txt");
            Scanner newReader = new Scanner(myObjj);
            while (newReader.hasNextLine()) {
                String data = newReader.nextLine(); // X|Y -> Y must come AFTER X -> 47|53: 47, blah, blah, 53
                //y is the key, x is added to the list of its values -> key must come AFTER values
                if (checkForCorrectUpdates){
                    String[] updates = data.split(","); // has the update string: 75, 97, 47, 61, 53
                    boolean correct = true;
                    Enumeration<Integer> keys = keyValue.keys(); //has keys: 75, 53, 29, 61, 47, 13
                    while (keys.hasMoreElements()) {
                        int key = keys.nextElement();
                        int indexInUpdate=0;
                        for(int i=0; i<updates.length; i++){
                            if(String.valueOf(key).equals(updates[i])){ // if the key is in the update string
                                for(int j=0; j<keyValue.get(key).size(); j++){ // go through all the key's values (the numbers that should be BEHIND key)
                                    for(int k=i; k<updates.length; k++){ //go through the rest of the update string
                                        if(String.valueOf(keyValue.get(key).get(j)).equals(updates[k])){ // check if any of the values are ahead of the key
                                            correct=false;
                                            break;
                                        }
                                    }
                                }
                            }
                        } // if keys values are behind key or arent in the update string at all at all
                    }
                    if (correct){
                        int middleNum = updates.length/2;
                        sum+=Integer.valueOf(updates[middleNum]);
                    }
                }else if (data.indexOf("|") > 0){ //if its not at the breaking point, switch to getting the X/Y values
                    int X = Integer.parseInt(data.substring(0, data.indexOf("|")));
                    int Y = Integer.parseInt(data.substring(data.indexOf("|")+1));
                    if (keyValue.get(Y)!= null){
                        keyValue.get(Y).add(X);
                    }else{
                        keyValue.put(Y, new ArrayList<Integer>());
                        keyValue.get(Y).add(X);
                    }
                }else{
                    checkForCorrectUpdates = true;
                }
            }
            newReader.close();
            System.out.println(sum);
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
