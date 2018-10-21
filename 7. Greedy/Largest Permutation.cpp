#include <bits/stdc++.h>
using namespace std;


void swap(long* a,long* b)
{
    long temp=*a;
    *a=*b;
    *b=temp;
}


int main() {
    long n,k;
    cin>>n>>k;
    vector<long> a(n);
   
    for(int i=0;i<n;i++)
        {
        cin>>a[i];
        
    }
    if(k>=n)
    {
        for(long i=n;i>0;i--)
        {
            cout<<i<<" ";
        }
        return 0;
    }
    long s=0,j;
   for(long i=0;i<n&&s<k;i++)
   {   if(a[i]!=n-i)
       {  j=i+1;
       while(a[j]!=n-i)
           j++;
         swap(&a[i],&a[j]);
    s++;}
   }
    for(long i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    
       
    
 
    return 0;
}
