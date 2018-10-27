// Problem Link :- https://www.hackerrank.com/challenges/even-tree/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static int ans;
    
    public static int dfs(int[][] adj,int source,int flag,int[] visited) 
        {
        visited[source]=1;
      int child=0;
        for(int i=1;i<adj[0].length;i++)
            {
            if(adj[source][i]==1&&visited[i]==0)
                {
                child++;
                child+=dfs(adj,i,flag,visited);
                
            }
        }
        //System.out.println(source+" "+child);
        if(child%2!=0&&child!=0&&source!=1)
                    ans++;
        return child;
    }

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int m=s.nextInt();
        int[][] adj=new int[n+1][n+1];
        int[] visited=new int[n+1];
        int u,v,f;
        for(int i=1;i<=m;i++)
            {
            u=s.nextInt();
            v=s.nextInt();
            adj[u][v]=1;
            adj[v][u]=1;
         }
        visited[1]=1;
                dfs(adj,1,0,visited);
    
        System.out.println(ans);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
