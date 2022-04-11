#include <stdio.h>
unsigned int countSetBits(int n)
{
    unsigned int count = 0;
    while (n)
    {
        n = n & (n - 1);
        count++;
    }
    return count;
}

int main()
{
    int n;
    printf("Enter number : ");
    scanf("%d",&n);

    printf("Number of set bits in %d is %d\n",n,countSetBits(n));

    return 0;
}
