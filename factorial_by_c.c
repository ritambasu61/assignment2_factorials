#include <stdio.h>
long int f(int n)
{
  if (n>=1)
    return n*f(n-1);
  else
    return 1;
}
int main()
{
  int n;printf("Give a positive integer: ");scanf("%d",&n);
  if (n<0)
      printf("Give a positive integer");
  else
    printf("The value of factorial %d is %ld",n,f(n));
  return 0;
}
