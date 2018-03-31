import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static String solve(int year){
        // Complete this function
        String date="";//fdate="";
        
        boolean isLeapYear;
        if(year <= 1917)
            isLeapYear = (year % 4 == 0);
        else
            isLeapYear = ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0));
        
        if (year == 1918)
            date = "26.09";
        else if(isLeapYear){
            date="12.09";
        }
        else
            date="13.09";
        
        return date+"."+year;
        
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int year = in.nextInt();
        String result = solve(year);
        System.out.println(result);
    }
}
