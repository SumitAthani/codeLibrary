/*  Problem Description
   There are n houses built in a line, each of which contain some value in it.
   A thief is going to steal in these houses.
   But he cannot steal in two adjacent houses.
   What is maximum value he can steal?
*/

#include<stdio.h>

int maximum(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}
int main()
{
    int n,i;
    printf("Enter the number of houses : ");
    scanf("%d",&n);
    int val[n];
    printf("Enter the values in %d houses : ");
    for(i=0;i<n;i++)
        scanf("%d",&val[i]);

    int stolenVal[n+1];
    stolenVal[0]=0;
    stolenVal[1]=maximum(stolenVal[0],val[0]);
    for(i=2;i<=n;i++)
        stolenVal[i]=maximum(stolenVal[i-2]+val[i-1],stolenVal[i-1]);

    printf("\nMaximum Thief can steal is %d\n",stolenVal[n]);
}
