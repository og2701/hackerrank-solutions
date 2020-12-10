import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Solution {

    static String timeConversion(String s) throws ParseException{
        
        SimpleDateFormat output = new SimpleDateFormat("HH:mm:ss");
        SimpleDateFormat input = new SimpleDateFormat("hh:mm:ssaa");
        
        Date time = input.parse(s);
        return output.format(time);
        
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException,ParseException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
