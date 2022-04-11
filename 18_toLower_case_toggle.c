#include<stdio.h>

int main()
{
    char ch;
    int t;

    printf("Enter a character : ");
    scanf("%c",&ch);
    printf("Lowercase of %c is %c\n",ch,((int)ch|(32)));

}
