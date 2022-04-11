#include<stdio.h>
int checkJthBit(int num,int j)
{
    if (num & (1 <<j))
        return 1;
    else
        return 0;
}
int main()
{
    int n,j;

    printf("Enter a number : ");
    scanf("%d",&n);

    printf("Enter j : ");
    scanf("%d",&j);

    if(checkJthBit(n,j))
        printf("%d bit is SET in %d\n",j,n);
    else
        printf("%d bit is NOT SET in %d\n",j,n);

}
