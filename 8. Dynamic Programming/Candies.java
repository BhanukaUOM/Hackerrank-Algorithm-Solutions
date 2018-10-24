/*
 * Link to Problem:- https://www.hackerrank.com/challenges/candies/problem 
 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++)
            a[i]=s.nextInt();
        Long[] dp=new Long[n];
        dp[0]=(long)1;
        for(int i=1;i<n;i++)
        {
            if(a[i]>a[i-1])
                dp[i]=dp[i-1]+1;
            else
                dp[i]=(long)1;
        }
        for(int i=n-2;i>=0;i--)
        {
            if(a[i]>a[i+1])
                dp[i]=Math.max(dp[i],dp[i+1]+1);
            else
                dp[i]=Math.max(dp[i],1);
        }
       long sum=0;
        for(int i=0;i<n;i++)
        {//System.out.print(dp[i]+" ");
            sum+=dp[i];
        }
        System.out.println(sum);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    }
}

