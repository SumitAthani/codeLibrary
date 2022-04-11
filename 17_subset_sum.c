#include<stdio.h>
#include<stdlib.h>
int main()
{
    int sum,n,i,j;
    printf("Enter number of elements in array : ");
    scanf("%d",&n);

    int a[n];
    printf("Enter the %d elements of array : ",n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);

    printf("Enter sum of subset : ");
    scanf("%d",&sum);

    int ss[n+1][sum+1];

    // initialising zeroth coloumn
    j=0;
    for(i=0;i<=n;i++)
        ss[i][j]=1;

    // initialising zeroth row
    i=0;
    for(j=1;j<=sum;j++)
        ss[i][j]=0;

    //dynamic programming
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=sum;j++)
        {
            if(ss[i-1][j]==1)
                ss[i][j]=1;
            else
            {
                if(a[i-1] > j)
                    ss[i][j]=0;
                else
                    ss[i][j]=ss[i-1][j-a[i-1]];
            }
        }
    }


    // printing result
    printf("Resulting Array : \n\n");
    printf("  | ");
    for(j=0;j<=sum;j++)
        printf("%d ",j);
    printf("\n");

    printf("------");
    for(j=0;j<=sum;j++)
        printf("--",j);
    printf("\n");

    for(i=0;i<=n;i++)
    {
        printf("%d | ",i);
        for(j=0;j<=sum;j++)
        {
           printf("%d ",ss[i][j]);
        }
        printf("\n");
    }

}
