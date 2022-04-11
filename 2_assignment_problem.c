#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<limits.h>
#define MAX 10

int countSetBit(int n)
{
    int c=0;
    while(n)
    {
        n = n & (n-1);
        c++;
    }
    return c;
}

int checkJthBit(int mask,int j)
{
    if (mask &(1<<j))
        return 1;
    else
        return 0;
}
int minimum(int a,int b)
{
    if(a<b)
        return a;
    else
        return b;
}
int assignmentProb(int cost[MAX][MAX],int n)
{
   int i,j,mask,x,a=pow(2,n),dp[a];

   dp[0]=0;
   for(i=1;i<a;i++)
      dp[i]=INT_MAX;


   for(mask=0; mask < a; mask++)
   {

     x=countSetBit(mask);


     for(j=0; j < n ; j++)
     {
         if(checkJthBit(mask,j)==0)
            dp[mask|(1<<j)] = minimum(dp[mask|(1<<j)],(dp[mask]+cost[x][j]));


     }
   }

   printf("DP array : ");
   for(i=0;i<pow(2,n);i++)
      printf("%d  ",dp[i]);
   printf("\n");


   return dp[a-1];
}


int main()
{
    int cost[MAX][MAX],n;
    printf("Enter the value of n : ");
    scanf("%d",&n);
    printf("\nEnter the values of cost matrix : ");
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
            scanf("%d",&cost[i][j]);
    }

    printf("Result : %d\n",assignmentProb(cost,n));
}
