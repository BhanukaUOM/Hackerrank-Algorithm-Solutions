import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution 
{
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        int item=sc.nextInt();
        int length=sc.nextInt();
        int[] array=new int[length];
        for(int i=0;i<length;i++)
        {
            array[i]=sc.nextInt();    
        }
        int first  = 0;
        int last   = length - 1;
        int middle = (first + last)/2;
 
    while( first <= last )
    {
      if ( array[middle] < item )
        first = middle + 1;    
      else if ( array[middle] == item ) 
      {
        System.out.println(middle);
        break;
      }
      else
         last = middle - 1;
 
      middle = (first + last)/2;
   }
   if ( first > last )
      System.out.println(item + " is not present in the list.\n");
            
    }
}
