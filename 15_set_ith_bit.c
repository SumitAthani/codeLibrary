#include<stdio.h>
int setIthBit(int n, int i)
{
    return ((1 << i) | n);
}
int main()
{
    int n,i;
    printf("Enter a number : ");
    scanf("%d",&n);
    printf("Enter bit to be set : ");
    scanf("%d",&i);

    printf("Number obtained after setting %dth bit in %d is %d\n\n",i,n,setIthBit(n,i));
}
