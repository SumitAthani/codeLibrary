/*program to find number of ways to reach destination
  using 3's, 5's and 10's
*/

#include<stdio.h>
int main()
{
    int num,i;
    printf("Enter number : ");
    scanf("%d",&num);
    int steps[num+1];
    for(i=0;i<=num;i++)
        steps[i]=0;
    steps[0]=1;
    // using 3's
    for(i=3;i<=num;i++)
        steps[i]=steps[i]+steps[i-3];

    //using 5's
    for(i=5;i<=num;i++)
        steps[i]=steps[i]+steps[i-5];

    //using 10's
    for(i=10;i<=num;i++)
        steps[i]=steps[i]+steps[i-10];


    printf("\nNumber of ways to reach %d using 3's, 5's and 10's is %d\n",num,steps[num]);
}
