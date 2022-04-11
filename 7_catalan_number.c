#include<stdio.h>
long long int catalan(long long int n)
{
  long long int catalan[n+1],i,j;
  catalan[0]=1;
  catalan[1]=1;

  for(i=2;i<=n;i++)
  {
      catalan[i]=0;
      for(j=0;j<i;j++)
      {
         catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1];
      }
  }

  printf("First %d Catalan numbers are : \n",n);
  for(i=0;i<=n;i++)
    printf("%d  ",catalan[i]);
  printf("\n\n%dth Catalan number is : ",n);

  return catalan[n];

}
int main()
{
    long long int n;

    printf("Enter n : ");
    scanf("%d",&n);

    printf("%d\n",catalan(n));

}
