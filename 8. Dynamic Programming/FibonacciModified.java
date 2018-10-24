/*
Problem Link : -https://www.hackerrank.com/challenges/fibonacci-modified/problem
*/
import java.io.*;
import java.util.*;
import java.math.*;
public class Solution {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        BigInteger t1=new BigInteger(s.next());
        BigInteger t2=new BigInteger(s.next());
        int n=s.nextInt();
        BigInteger[] dp=new BigInteger[n];
        dp[0]=t1;
        dp[1]=t2;
        for(int i=2;i<n;i++)
            {
            dp[i]=dp[i-2].add(dp[i-1].multiply(dp[i-1]));
        }
        System.out.println(dp[n-1]);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
